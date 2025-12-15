import streamlit as st
import datetime

#修改标签页文字和图标
st.set_page_config(page_title="个人简历生成器",page_icon="📃",layout="wide")

#标题和文字
st.title("个人简历生成器")
st.text("使用streamlit创建你的个性化简历")

#自定义多选下拉按钮函数
def my_format_func(option):
    return f'{option}'

def my_format_func1(option):
    return f'{option}'

def my_format_func2(option):
    return f'{option}'

#文字分割函数，用英文,为分割符号
def split_text_by_comma(text):
    if not text:  # 空值判断，避免报错
        return []
    # 拆分逗号、去空格 +和过滤空项
    return [item.strip() for item in text.split(',') if item.strip()]

#分列容器，把整个页面1：2分成两列
c1,c2=st.columns([1,2])

#左边列，填写信息
with c1:
     st.markdown("##### 🖋︎个人信息表单")
     #分割线
     st.markdown("***")
     #单行文本输入框组件，输入信息并赋值
     user_name=st.text_input('姓名')
     user_position=st.text_input('职位')
     user_phone=st.text_input('电话')
     user_email=st.text_input('邮箱')
     # 日期选择，value参数默认为None
     date = st.date_input(
        "出生日期",
        value=None,  # 初始无默认值
        min_value=datetime.date(1900, 1, 1),  # 最早可选1900年1月1日（可按需调整，比如1950年）
        max_value=datetime.date.today()  # 最晚可选今天（可选，避免选未来日期）
    )
     st.write('性别')
     # 设置标签为“hidden”
     # 设置水平排列
     lunch = st.radio(
     '',
     ['女', '男', '其他'],
     horizontal=True,
     label_visibility='hidden'
     )
     #数值滑块组件
     user_age=st.slider('年龄',0,150,22)

     #下拉按钮选项
     xl = st.selectbox('最高学历：', ['博士', '硕士', '本科', '高中', '中职','初中'], format_func=my_format_func, index=2)
     #多选下拉按钮
     options_1 = st.multiselect(
     '语言能力(可多选)',
     ['中文', '英语', '俄语', '日语', '法语', '德语'],
     format_func=my_format_func1,
     )
     options_2 = st.multiselect(
     '技能(可多选)',
     ['JAVA', 'HTML/CSS', '机器学习', 'Python', 'C语言', '数据挖掘', '大数据分析', 'PS','SQL Server'],
     format_func=my_format_func2,
     )
     #多行文本输入框组件
     user_awards=st.text_area(label='获奖情况(英文,间隔)', placeholder='请输入您的获奖情况')
     user_certificates=st.text_area(label='技能证书(英文,间隔)', placeholder='请输入您的技能证书')

     #数值滑块组件
     user_job=st.slider('工作经验(年)',0,40,0)
     user_salary=st.slider('期望薪资范围(元)',0,300000,4000)
     #多行文本输入框组件
     user_intro=st.text_area(label='个人简介', placeholder='请输入您的个人简介')
     #时间选择组件
     w2=st.time_input("每日最佳联系时间段")
     # 创建图片上传组件（限制格式：JPG/PNG）
     uploaded_img = st.file_uploader(
     "上传个人照片",
     type=["jpg", "jpeg", "png"],  # 仅允许图片格式
     help="支持JPG、PNG格式的图片文件"
     )

#右边简历预览列
with c2:
    st.markdown("##### 📄简历实时预览")
    st.markdown("***")
    #再分成两列显示信息
    c3,c4=st.columns(2)
    #左边列
    with c3:
         # 判断图片是否上传，避免None值报错
        if uploaded_img is not None:
            st.image(uploaded_img, width=150)
        else:
            # 未上传时显示占位提示（可选：也可以用st.write("未上传照片")）
            st.image("https://gss0.baidu.com/-fo3dSag_xI4khGko9WTAnF6hhy/zhidao/wh%3D600%2C800/sign=dc9e82874dfbfbeddc0c3e7948c0db0e/32fa828ba61ea8d37b2e67bc910a304e251f587d.jpg", width=150, caption="请上传个人照片")
        #写入信息
        st.title(user_name)
        st.write(f"💼职位：{user_position}")
        st.write(f"📞电话：{user_phone} ")
        st.write(f"📧 邮箱：{user_email}")
        st.write(f"🎂出生日期：{date}")
    #右边列，写入信息
    with c4:
        st.write(f"⚥ 性别：{lunch}")
        st.write(f"🎓 最高学历：{xl}")
        st.write(f"📅年龄:{user_age}")
        st.write(f"🗣 语言能力：{', '.join(options_1) if options_1 else '未选择'}")
        st.write(f"💻 工作经验：{user_job} 年")
        st.write(f"💰 期望薪资：{user_salary} 元/月")
        st.write(f"⏰ 最佳联系时间：{w2.strftime('%H:%M')}")

    st.markdown("***")
    
    #再分成两列显示信息，左列显示专业技能/证书，右列显示语言能力/获奖情况
    c5,c6=st.columns(2)
    with c5:
        st.markdown("#### 🗄️专业技能")
        # 显示专业技能，若未选择则提示，否则用方块符号逐行显示
        if options_2:
            for skill in options_2:
                st.write(f"◽ {skill}")
        else:
            st.write("请在左侧选择您的专业技能")

        st.markdown("#### 📝 技能证书")
        # 调用文本拆分函数，将英文逗号分隔的证书拆分为列表
        certificates_list = split_text_by_comma(user_certificates)
        if certificates_list:
            for cert in certificates_list:
                st.write(f"◽ {cert}")  # 带项目符号换行
        else:
            st.write("请在左侧填写技能证书（英文逗号分隔）")


    with c6:
        st.markdown("#### 🔔语言能力")
        # 显示语言能力，若未选择则提示，否则用方块符号逐行显示
        if options_1:
            for skill in options_1:
                st.write(f"◽{skill}")
        else:
            st.write("请在左侧选择您的语言能力")

        st.markdown("#### 📎获奖情况")
         # 调用文本拆分函数，将英文逗号分隔的获奖情况拆分为列表
        awards_list = split_text_by_comma(user_awards)
        if awards_list:
            for award in awards_list:
                st.write(f"◽ {award}")  # 带项目符号换行
        else:
            st.write("请在左侧填写获奖情况（英文逗号分隔）")

    st.markdown("***")
    # 个人简介板块
    st.markdown("#### 个人简介")
    if user_intro:
        st.write(f"{user_intro}")
    else:
        st.write("请在左侧填写您的个人简介")














        
