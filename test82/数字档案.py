import streamlit as st # 导入Streamlit并用st代表它
import pandas as pd # 导入Pandas并用pd代替

st.set_page_config(page_title="数字档案",page_icon="📔",layout="wide")
# 自定义CSS，修改整个页面背景色为浅蓝色
st.markdown("""
    <style>
    .stApp {
    background-color: #f0f8ff !important;  
    }
    </style>
""", unsafe_allow_html=True)

# 大标题
st.title("学生 小羊🐐 - 数字档案",help="了解更多")
# 第二标题
st.header("🔔基础信息")
# 蓝色粗体文本
st.markdown(':blue[**学生ID:22053060166**]')
# 文本并调整特定文本为绿色
st.markdown('*注册时间：<span style="color:green;">2022-09-13</span> | 健康状态：良好*', unsafe_allow_html=True)
st.markdown('*当前教室：<span style="color:green;">实训楼108</span>  | 安全等级：<span style="color:green;">绝密</span>*',unsafe_allow_html=True)
# 分割线
st.markdown('***')
# 第二标题
st.header("🔋课程矩阵")
# 定义列布局，分成3列
c1,c2,c3=st.columns(3)
# 输入各列信息
c1.metric(label="C语言",help="C语言程序设计", value="90%", delta="-6%")
c2.metric(label="Python", value="94%", delta="3%")
c3.metric(label="Java",help="Java项目实训", value="70%", delta="-10%")
# 小标题
st.subheader('Streamlit课程进度')
# 进度配置
course=0.3  # 进度值：0~1
# 普通文本
st.text("进度条展示")
# 创建进度条
progress=st.progress(0)
progress.progress(course)

# 分割线
st.markdown('***')
st.header("📝任务日志")


# 定义数据,以便创建数据框
data = {
    '日期':['2025-12-1-9','2025-12-1-9' ,'2025-12-1-9'],
    '任务':['学生数字档案', '课程管理系统', '数据图表展示'],
    '状态':['✅完成', '🕘进行中','❌️未完成'],
    '难度':['⭐⭐⛤⛤⛤', '⭐⛤⛤⛤⛤', '⭐⭐⭐⛤⛤'],
}

# 定义数据框所用的索引
index = pd.Series(['0', '1', '2',])

# 根据上面创建的data和index，创建数据框
df = pd.DataFrame(data, index=index)
# 静态表
st.table(df)

st.header("🔐最新代码成果")

# 创建要显示的Python代码块的内容
python_code='''def matrix_breach():
    while True:
        if deletect_vulnerability():
            exploit()
             return "ACCESS GRANTED"
         else:
             stealth_evade()'''
# 创建一个代码块，用于展示python_code的内容
st.code(python_code)

#分割线
st.markdown('***')

#最后的文字部分
st.markdown(':green[>> SYSTEN MESSAGE]'':下一个任务目标已解锁...')
st.markdown(':green[>> TARGET]'':课程管理系统')
st.markdown(':green[>> COUNTDOWN]'':2025-06-03 17:21:36')
st.markdown('系统状态:在线 连接状态:已加密')

