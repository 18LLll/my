# 导入streamlit库，简称为st，这是构建Python Web应用的核心库
import streamlit as st
# 导入pickle库，用于加载预训练的机器学习模型文件（.pkl格式）
import pickle
# 导入pandas库，简称为pd，用于数据处理（如创建DataFrame、数据格式化）
import pandas as pd


# 设置Streamlit页面的配置参数，自定义页面外观和布局
st.set_page_config(
    page_title="医疗费用预测",  # 设置浏览器标签页的标题
    page_icon="🏥",  # 可选：添加页面图标（医院图标），更直观
    layout="wide"    # 可选：设置页面为宽布局，提升视觉体验
)

# 定义简介页面的函数，用于展示应用的介绍信息
def introduce_page():
    # 在页面上显示一级标题“欢迎使用！”
    st.write("# 欢迎使用！")
     
    # 在侧边栏显示成功提示信息，引导用户点击预测医疗费用选项
    st.sidebar.success("单击预测医疗费用")
    # 使用markdown语法在页面上显示富文本内容，介绍应用的背景和使用指南
    st.markdown(
        """
        # 医疗费用预测应用
        这个应用利用机器学习模型来预测医疗费用，为保险公司的保险定价提供参考。
        
        ## 背景介绍
        - 开发目标：帮助保险公司合理定价保险产品，控制风险。
        - 模型算法：利用随机森林回归算法训练医疗费用预测模型。
        
        ## 使用指南
        - 输入准确完整的被保险人信息，可以得到更准确的费用预测。
        - 预测结果可以作为保险定价的重要参考，但需审慎决策。
        - 有任何问题欢迎联系我们的技术支持。
        技术支持：email：support@example.com
        """
        )

    
# 定义预测页面的函数，用于接收用户输入并输出医疗费用预测结果
def predict_page():
    # 使用markdown语法显示预测页面的使用说明
    st.markdown(
        """
        ## 使用说明
        这个应用利用机器学习模型来预测医疗费用，为保险公司的保险定价提供参考。
        - **输入信息**：在下面输入被保险人的个人信息，疾病信息等。
        - **费用预测**：应用会预测被保险人的未来医疗费用支出。
        """
        )

    # 创建一个表单组件，命名为'user_inputs'，用于统一收集用户输入
    with st.form('user_inputs'):
        # 创建数字输入框，标签为“年龄”，最小值为0，用于接收用户输入的年龄
        age=st.number_input('年龄',min_value=0)
        # 创建单选框，标签为“性别”，选项为['女性','男性']，用于接收用户选择的性别
        sex=st.radio('性别',options=['女性','男性'])
        # 创建数字输入框，标签为“BMI”，最小值为0.0（浮点数），用于接收用户输入的BMI值
        bmi=st.number_input('BMI',min_value=0.0)

        # 创建数字输入框，标签为“子女数量：”，步长为1（只能输入整数），最小值为0，用于接收子女数量
        children=st.number_input("子女数量：",step=1,min_value=0)
        # 创建单选框，标签为“是否吸烟”，选项为("是","否")，用于接收用户选择的吸烟状态
        smoke=st.radio("是否吸烟",("是","否"))
        # 创建下拉选择框，标签为“区域”，选项为('东南部', '西南部', '东北部', '西北部')，用于接收用户选择的区域
        region = st.selectbox('区域', ('东南部', '西南部', '东北部', '西北部'))
        # 创建表单提交按钮，标签为“预测费用”，点击后触发表单提交事件
        submitted=st.form_submit_button('预测费用')

    # 判断用户是否点击了提交按钮，如果是则执行后续的数据处理逻辑
    if submitted:
        # 临时存储用户输入的原始数据（未编码）
        format_data=[age,sex,bmi,children,smoke,region]

        # 初始化性别相关的哑变量（用于将分类变量转换为数值变量）
        sex_female,sex_male=0,0
        # 如果用户选择“女性”，则将sex_female设为1
        if sex=='女性':
         sex_female=1
        # 如果用户选择“男性”，则将sex_male设为1
        elif sex=='男性':
             sex_male=1

        # 初始化吸烟状态相关的哑变量
        smoke_yes,smoke_no=0,0
        # 如果用户选择“是”（吸烟），则将smoke_yes设为1
        if smoke=='是':
             smoke_yes=1
        # 如果用户选择“否”（不吸烟），则将smoke_no设为1
        elif smoke=='否':
             smoke_no=1

        # 初始化区域相关的哑变量
        region_northeast,region_southeast,region_northwest,region_southwest=0,0,0,0
        # 根据用户选择的区域，将对应的哑变量设为1
        if region =='东北部':
             region_northeast=1
        # 东南部对应的哑变量设为1
        elif region =='东南部':
             region_southeast=1
        # 西北部对应的哑变量设为1
        elif region =='西北部':
             region_northwest=1
        # 西南部对应的哑变量设为1
        elif region =='西南部':
             region_southwest=1

        # 整理编码后的特征数据（所有分类变量已转换为数值变量），用于输入模型预测
        format_data=[
             age,bmi,children,sex_female,sex_male,
             smoke_no,smoke_yes,
             region_northeast,region_southeast,region_northwest,region_southwest]

    # 以二进制读取模式打开预训练的随机森林回归模型文件（rfr_model.pkl）
    with open('rfr_model.pkl','rb') as f:
        # 加载模型文件到内存中，赋值给rfr_model变量
        rfr_model=pickle.load(f)

    # 再次判断用户是否点击了提交按钮，执行预测逻辑
    if submitted:
        # 将编码后的特征数据转换为DataFrame格式（模型输入要求的格式），列名与模型训练时的特征名一致
        format_data_df=pd.DataFrame(data=[format_data],columns=rfr_model.feature_names_in_)

        # 使用加载的模型对输入数据进行预测，取第一个预测结果（因为只有一条数据）
        predict_result =rfr_model.predict(format_data_df)[0]
        # 在页面上显示成功提示，展示四舍五入保留两位小数的预测费用结果
        st.success(f'✅ 根据您输入的数据，预测该客户的医疗费用是：{round(predict_result, 2)} 元')

    # 在页面上添加水平分割线，美化页面布局
    st.markdown("---")  # 分割线，更美观
    # 在页面底部显示技术支持的联系方式
    st.write("技术支持：email：support@example.com")

# 在侧边栏创建单选导航栏，标签为“导航”，选项为["简介", "预测医疗费用"]，用户选择后赋值给nav变量
nav=st.sidebar.radio("导航", ["简介", "预测医疗费用"])
# 根据选择的导航选项，展示对应页面
if nav == "简介":
    # 如果用户选择“简介”，调用introduce_page函数展示简介页面
    introduce_page()
else:
    # 如果用户选择“预测医疗费用”，调用predict_page函数展示预测页面
    predict_page()
