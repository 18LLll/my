import streamlit as st
import pandas as pd
import pickle

# 页面配置
st.set_page_config(page_title="期末成绩预测", page_icon="🔮", layout="wide")

# 加载训练好的模型
with open("score_model.pkl", 'rb') as f:
    model = pickle.load(f)

with open("feature_cols.pkl", 'rb') as f:
    feature_cols = pickle.load(f)

# 页面标题 
st.title("🔮 期末成绩预测")
st.markdown("---")

# 匹配示例图的提示文本
st.markdown(":blue[✨请输入学生的学习信息，系统将预测其期末成绩并提供学习建议]")

# 输入表单
with st.form("predict_form"):
    col1, col2 = st.columns(2)
    
    with col1:
        sno = st.text_input("🆔学号")
        sex = st.selectbox("⚤性别", ["男", "女"])
        major = st.selectbox("🎓专业", ["财务管理", "大数据管理", "电子商务", "工商管理", "人工智能"])
    
    with col2:
        week_hours = st.slider("📚每周学习时长（小时）", 5, 40, 15)
        attendance = st.slider("🏫上课出勤率", 0.6, 1.0, 0.85)
        midterm = st.slider("📝期中考试分数", 0, 100, 70)
        homework = st.slider("✏️作业完成率", 0.7, 1.0, 0.85)
    
    submit_btn = st.form_submit_button("🔍预测期末成绩")

st.markdown("---")
st.subheader("📊 预测结果")
# 预测逻辑
if submit_btn:
    if not sno:
        st.error("⚠️请输入学号！")
    else:
        # 构建输入数据
        input_data = pd.DataFrame({
            '每周学习时长（小时）': [week_hours],
            '上课出勤率': [attendance],
            '期中考试分数': [midterm],
            '作业完成率': [homework],
            '性别_编码': [0 if sex == "男" else 1]
        })
        
        # 处理专业编码
        for col in feature_cols:
            if col.startswith("专业_"):
                input_data[col] = 1 if col == f"专业_{major}" else 0
        
        # 预测分数
        final_score = model.predict(input_data[feature_cols])[0]
        final_score = round(final_score, 2)
        is_pass = final_score >= 60
        
        # 用列布局实现居中显示
        col_left, col_mid, col_right = st.columns([1, 2, 1])  # 左右列宽度为1，中间列宽度为2
        with col_mid:  # 中间列显示结果
            st.write(f"🆔**学号**：{sno}")
            st.write(f"⚥**性别**：{sex}")
            st.write(f"🎓**专业**：{major}")
            st.write(f"🌟**预测期末分数：{final_score} 分**")
            
            # 展示图片和提示
            if is_pass:
                st.success("🎉 恭喜！！预测结果能及格！")
                try:
                    st.image("jige.jpg", width=500)
                except:
                    st.write("🎉 继续保持优秀！")
            else:
                st.warning("💪 继续加油咯，争取能及格！")
                try:
                    st.image("bujige.jpeg", width=500)
                except:
                    st.write("💪 建议多花时间学习，巩固知识点！")
