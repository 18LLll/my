# 导入streamlit库，简称为st，这是构建Python Web应用的核心库
import streamlit as st
# 导入pickle库，用于加载预训练的机器学习模型文件和映射字典文件（.pkl格式）
import pickle
# 导入pandas库，简称为pd，用于数据处理（如创建DataFrame、数据格式化）
import pandas as pd

# 设置Streamlit页面的全局配置参数，自定义页面外观和布局
st.set_page_config(
    page_title="企鹅分类器",  # 设置浏览器标签页的标题为“企鹅分类器”
    page_icon="🐧",  # 设置页面图标为企鹅表情符号，更直观
    layout="wide",   # 设置页面为宽布局，提升视觉体验和内容展示空间
)

# 创建侧边栏区域，所有在with st.sidebar内的元素都会显示在页面左侧的侧边栏中
with st.sidebar:
    # 在侧边栏中显示本地图片文件rigth_logo.png，设置宽度为100像素
    st.image('rigth_logo.png',width=100)
    # 在侧边栏中显示一级标题“请选择页面”
    st.title('请选择页面')
    # 创建下拉选择框，标签为“请选择页面”，选项为["简介页面","预测分类页面"]
    # label_visibility="collapsed"表示隐藏选择框的标签（仅保留下拉选项）
    page=st.selectbox("请选择页面",["简介页面","预测分类页面"],label_visibility="collapsed")
    
# 判断用户是否选择了“简介页面”，若是则执行以下逻辑
if page == "简介页面":
    # 显示页面主标题“企鹅分类器”，并添加企鹅表情符号
    st.title("企鹅分类器:penguin:")
    # 显示二级标题“数据集介绍”
    st.header('数据集介绍')
    # 使用markdown语法显示富文本，介绍帕尔默群岛企鹅数据集的背景和内容
    st.markdown('''"帕尔默群岛企鹅数据集是用于数据探索和数据可视化的一个出色的数据集，也可以作为机器学习入门练习。
该数据集是由Gorman等收集，并发布在一个名为palmerpenguins的R语言包，以对南极企鹅种类进行分类和研究。
该数据集记录了344行观测数据，包含3个不同物种的企鹅：阿德利企鹅、巴布亚企鹅和帽带企鹅的各项信息。"''')
    # 显示二级标题“三种企鹅的卡通图像”
    st.header('三种企鹅的卡通图像')
    # 在页面中显示本地图片文件penguins.png（三种企鹅的卡通图）
    st.image('penguins.png')
    
# 若用户选择了“预测分类页面”，则执行以下逻辑
elif page == "预测分类页面":
    # 显示二级标题“预测企鹅分类”
    st.header("预测企鹅分类")
    # 使用markdown语法显示应用的使用说明，引导用户输入信息进行预测
    st.markdown("这个Web应用是基于帕尔默群岛企鹅数据集构建的模型。只需输入6个信息，就可以预测企鹅的物种，使用下面的表单开始预测吧！")

    # 划分页面列布局，比例为3:1:2（col_form占3份，col1占1份，col_logo占2份），用于排版优化
    col_form, col1, col_logo = st.columns([3, 1, 2])
    # 将元素放入col_form列中（主要的输入表单区域）
    with col_form:
        # 创建一个表单组件，命名为'user_input'，用于统一收集用户输入的企鹅特征数据
        with st.form('user_input'):
            # 创建下拉选择框，标签为“企鹅栖息的岛屿”，选项为三个岛屿名称
            island = st.selectbox('企鹅栖息的岛屿', options=['托尔斯森岛', '比斯科群岛', '德里马岛'])
            # 创建下拉选择框，标签为“性别”，选项为['雄性', '雌性']
            sex = st.selectbox('性别', options=['雄性', '雌性'])
            # 创建数字输入框，标签为“喙的长度（毫米）”，最小值为0.0（浮点数），用于输入喙长度
            bill_length = st.number_input('喙的长度（毫米）', min_value=0.0)
            # 创建数字输入框，标签为“喙的深度（毫米）”，最小值为0.0，用于输入喙深度
            bill_depth = st.number_input('喙的深度（毫米）', min_value=0.0)
            # 创建数字输入框，标签为“翅膀的长度（毫米）”，最小值为0.0，用于输入翅膀长度
            flipper_length = st.number_input('翅膀的长度（毫米）', min_value=0.0)
            # 创建数字输入框，标签为“身体质量（克）”，最小值为0.0，用于输入身体质量
            body_mass = st.number_input('身体质量（克）', min_value=0.0)
            # 创建表单提交按钮，标签为“预测分类”，点击后触发表单提交事件
            submitted = st.form_submit_button('预测分类')

    # 初始化岛屿相关的哑变量（用于将分类变量转换为数值变量，适配模型输入）
    island_biscoe, island_dream, island_torgerson = 0, 0, 0
    # 根据用户选择的岛屿，将对应的哑变量设为1（独热编码）
    if island == '比斯科群岛':
        island_biscoe = 1
    elif island == '德里马岛':
        island_dream = 1
    elif island == '托尔斯森岛':
        island_torgerson = 1

    # 初始化性别相关的哑变量（独热编码）
    sex_female, sex_male = 0, 0
    # 根据用户选择的性别，将对应的哑变量设为1
    if sex == '雌性':
        sex_female = 1
    elif sex == '雄性':
        sex_male = 1

    # 整理编码后的特征数据，按模型训练时的特征顺序排列，用于输入模型预测
    format_data = [bill_length, bill_depth, flipper_length, body_mass,
                   island_dream, island_torgerson, island_biscoe, sex_male, sex_female]

    # 以二进制读取模式打开预训练的随机森林分类器模型文件（rfc_model.pkl）
    with open('rfc_model.pkl', 'rb') as f:
            # 加载模型文件到内存中，赋值给rfc_model变量
            rfc_model = pickle.load(f)
    # 以二进制读取模式打开企鹅物种映射字典文件（output_uniques.pkl），用于将预测编码转换为物种名称
    with open('output_uniques.pkl', 'rb') as f:
            # 加载映射字典到内存中，赋值给output_uniques_map变量
            output_uniques_map = pickle.load(f)

    # 判断用户是否点击了提交按钮，如果是则执行预测逻辑
    if submitted:
        # 将编码后的特征数据转换为DataFrame格式（模型输入要求的格式），列名与模型训练时的特征名一致
        format_data_df =pd.DataFrame(data=[format_data],columns=rfc_model.feature_names_in_)
        # 使用加载的模型对输入数据进行预测，得到物种的编码结果（数组类型）
        predict_result_code = rfc_model.predict(format_data_df)
        # 通过映射字典将预测编码转换为企鹅物种名称，取第一个元素（因只有一条数据）
        predict_result_species = output_uniques_map[predict_result_code][0]
        # 在页面上显示预测结果，使用**加粗**突出物种名称
        st.write(f'根据您输入的数据，预测该企鹅的物种名称是：**{predict_result_species}**')

    # 将元素放入col_logo列中（图片展示区域）
    with col_logo:
        # 如果用户未点击提交按钮，显示logo图片rigth_logo.png，宽度为300像素
        if not submitted:
            st.image('rigth_logo.png',width=300)
        # 如果用户已提交，显示对应企鹅物种的图片（图片名与物种名称一致）
        else:
            st.image(f'{predict_result_species}.png',width=300)
