import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# 1. 全局页面配置（保持与原代码一致，宽布局适配数据分析）
st.set_page_config(
    page_title="学生成绩分析系统",
    page_icon="🎓",
    layout="wide",
)

# 2. 初始化session_state：存储当前选中的页面，默认显示“项目介绍”
if "current_page" not in st.session_state:
    st.session_state["current_page"] = "项目介绍"

# 3. 定义导航按钮点击事件：更新当前页面状态
def switch_page(page_name):
    st.session_state["current_page"] = page_name

# 4. 左侧导航栏（精简为两个核心按钮，无黑色背景，原生Streamlit样式）
with st.sidebar:
    # 导航栏标题（匹配图片的系统名称风格）
    st.title("系统导航栏")
    st.markdown("***")  # 分隔线提升可读性
    
    # 导航按钮1：项目介绍（核心页面1）
    st.button(
        label="📑 项目介绍",
        on_click=switch_page,
        args=("项目介绍",),
        use_container_width=True,  # 按钮宽度适配侧边栏
        help="查看项目目标和技术架构"
    )
    
    # 导航按钮2：专业数据分析（核心页面2）
    st.button(
        label="🔢 专业数据分析",
        on_click=switch_page,
        args=("专业数据分析",),
        use_container_width=True,
        help="查看各专业成绩、出勤率等分析"
    )
    
    # 导航按钮3：成绩预测（核心页面3）
    st.button(
        label="🔮 成绩预测",
        on_click=switch_page,
        args=("成绩预测",),
        use_container_width=True,
        help="根据特征，对期末成绩进行预测"
    )
    
    st.markdown("***")
    # 侧边栏额外说明（简化版，保持实用性）
    st.markdown("### 📌 使用说明")
    st.markdown("- 点击左侧按钮切换功能模块")
    st.markdown("- 专业数据分析模块支持多维度可视化")
    st.markdown("- 成绩预测模块：输入学习信息后，可获取期末成绩预测结果")

# 5. 读取数据（仅专业数据分析模块需要，添加异常处理）
try:
    data = pd.read_csv('student_data_adjusted_rounded.csv', encoding='utf-8')
except FileNotFoundError:
    st.error("数据文件未找到，请检查路径是否正确！")
    data = pd.DataFrame()  # 避免后续代码报错

# 6. 页面内容：仅保留项目介绍和专业数据分析
# ---------------------- 页面1：项目介绍 ----------------------
if st.session_state["current_page"] == "项目介绍":
    import streamlit as st


    # 设置Streamlit页面的全局配置参数，自定义页面外观和布局
    st.set_page_config(
        page_title="学生成绩分析预测系统",  # 设置浏览器标签页的标题
        page_icon="🎓",  # 设置页面图标为学士帽表情符号
        layout="wide",   # 设置页面为宽布局
    )
    st.title("👩‍🎓学生成绩分析与预测系统👨‍🎓")

    st.markdown("***")

    c1,c2=st.columns(2)
    with c1:
        st.header("📑项目概述")
        st.markdown("本系统是一个基于Streamlit的学生成绩分析平台，通过数据可视化和机器学习技术，帮助教育工作者和学生深入了解学业表现，并预测期末考试成绩。")
        st.subheader("主要特点")
        st.markdown("""
            - 📊 <span style="font-weight: bold; ">数据可视化</span>：多维展示学生学业数据
            - 🎯 <span style="font-weight: bold; ">专业分析</span>：按专业分类的详细统计分析
            - 🔮 <span style="font-weight: bold;">智能预测</span>：基于机器学习模型的成绩预测
            - 💡 <span style="font-weight: bold; ">学习建议</span>：根据预测结果提供个性化反馈
            """, unsafe_allow_html=True)

    with c2:
        st.image("system.png",use_container_width=True)



    st.markdown("***")

    st.header("🏆项目目标")

    c3,c4,c5=st.columns(3)

    with c3:
        st.subheader("🔍目标一")
        st.markdown("""
            ##### 分析影响因素
            - 识别关键学习指标
            - 探索成绩相关因素
            - 提供数据支持决策
            """, unsafe_allow_html=True)




    with c4:
        st.subheader("📊目标二")
        st.markdown("""
            ##### 可视化展示
            - 专业对比分析
            - 性别差异研究
            - 学习模式识别
            """, unsafe_allow_html=True)

    with c5:
        st.subheader("🔮目标三")
        st.markdown("""
            ##### 成绩预测
            - 机器学习模型
            - 个性化预测
            - 及时干预预警
            """, unsafe_allow_html=True)

    st.markdown("***")

    st.header("⚙️技术架构")

    c6,c7,c8,c9=st.columns(4)

    with c6:
        st.markdown("""
            #### 💻︎前端框架
            """, unsafe_allow_html=True)
        c6_code = '''Streamlit'''
        st.code(c6_code, language=None,line_numbers=True)

    with c7:
        st.markdown("""
            #### 🧹数据处理
            """, unsafe_allow_html=True)
        c7_code = '''Pandas
Numpy'''
        st.code(c7_code, language=None,line_numbers=True)

    with c8:
        st.markdown("""
            #### 📈可视化
            """, unsafe_allow_html=True)
        c8_code = '''Matplotlib
Plotly.express
Plotly.graph_objects'''
        st.code(c8_code, language=None,line_numbers=True)

    with c9:
        st.markdown("""
            #### 🎯机器学习
            """, unsafe_allow_html=True)
        c9_code = '''Scikit-learn'''
        st.code(c9_code, language=None,line_numbers=True)
    

# ---------------------- 页面2：专业数据分析（完整保留原data.py内容） ----------------------
elif st.session_state["current_page"] == "专业数据分析":
    # 导入所需的Python库
    import streamlit as st
    import pandas as pd
    # 用于快速绘制美观的交互式图表
    import plotly.express as px
    # 用于自定义更复杂的交互式图表
    import plotly.graph_objects as go

    # 配置Streamlit页面的全局参数
    # page_title：设置浏览器标签页显示的标题
    # page_icon：设置浏览器标签页的图标，使用emoji表情
    # layout：设置页面布局为宽屏模式（wide），充分利用页面宽度
    st.set_page_config(
        page_title="专业数据分析",
        page_icon="📊",
        layout="wide",
    )

    # 读取本地CSV格式的数据集
    # 路径：使用双反斜杠\\表示Windows系统的文件路径（避免转义字符问题）
    # encoding='utf-8'：指定文件编码为UTF-8，确保中文内容正常显示
    data = pd.read_csv('student_data_adjusted_rounded.csv', encoding='utf-8')

    # 设置页面的主标题，使用emoji增强视觉效果
    st.title("🔢专业数据分析")

    # 设置子标题，用于区分模块内容
    st.subheader("📋 各专业核心数据总览")

    # 计算各专业的男女人数、总人数及性别占比指标
    # groupby(["专业", "性别"])：按专业和性别对数据进行分组
    # size()：统计每个分组的行数（即对应人数）
    # reset_index(name="人数")：重置索引并将统计结果列命名为“人数”

    gender_count = data.groupby(["专业", "性别"]).size().reset_index(name="人数")

    # pivot_table：将性别列转换为列名，实现数据的宽表转换
    # index="专业"：行索引为专业
    # columns="性别"：列索引为性别
    # values="人数"：填充的数值为人数
    # fill_value=0：缺失值（如某专业无某性别）填充为0
    # reset_index()：重置索引，将专业从索引转为普通列

    gender_pivot = gender_count.pivot_table(index="专业", columns="性别", values="人数", fill_value=0).reset_index()

    # 处理列名缺失情况：若数据中无“男”或“女”列，手动添加并赋值为0，避免后续计算报错
    if "男" not in gender_pivot.columns:
        gender_pivot["男"] = 0
    if "女" not in gender_pivot.columns:
        gender_pivot["女"] = 0
        
    # 计算各专业总人数：男生人数+女生人数
    gender_pivot["总人数"] = gender_pivot["男"] + gender_pivot["女"]
    # 计算男生占比：(男生人数/总人数)*100，保留1位小数
    gender_pivot["男生占比(%)"] = (gender_pivot["男"] / gender_pivot["总人数"] * 100).round(1)
    # 计算女生占比：(女生人数/总人数)*100，保留1位小数
    gender_pivot["女生占比(%)"] = (gender_pivot["女"] / gender_pivot["总人数"] * 100).round(1)


    # 计算各专业的学习时长、成绩、出勤率等指标
    # groupby("专业")：按专业分组
    # agg()：聚合函数，对每个分组执行指定的统计操作
    # 键为自定义列名（无特殊字符，避免语法错误），值为(原数据列名, 聚合函数)
    # mean()：计算平均值，std()：计算标准差
    # round(1)：所有聚合结果保留1位小数
    # reset_index()：重置索引，将专业从索引转为普通列
    score_study = data.groupby("专业").agg(
        平均学习时长=("每周学习时长（小时）", "mean"),
        期中平均分=("期中考试分数", "mean"),
        期末平均分=("期末考试分数", "mean"),
        期末成绩标准差=("期末考试分数", "std"),
        平均出勤率原始=("上课出勤率", "mean")
    ).round(1).reset_index()


    # columns：字典，键为原列名，值为新列名
    # inplace=True：直接在原DataFrame上修改，不创建新对象
    score_study.rename(
        columns={
            "平均学习时长": "平均学习时长(小时)",
            "平均出勤率原始": "平均出勤率(原始)"
        },
        inplace=True
    )

    # 将出勤率从原始小数（0-1）转换为百分比（0-100），保留1位小数
    score_study["平均出勤率(%)"] = (score_study["平均出勤率(原始)"] * 100).round(1)
    # 删除原始出勤率列，仅保留百分比形式的出勤率，简化数据
    score_study = score_study.drop("平均出勤率(原始)", axis=1)

    # 合并性别指标和学习成绩指标为一个完整的DataFrame
    # pd.merge()：合并两个DataFrame
    # on="专业"：以“专业”列为连接键

    # how="outer"：外连接，保留所有专业的数据，避免数据丢失
    total_data = pd.merge(gender_pivot, score_study, on="专业", how="outer")
    # 填充缺失值：将合并后的数据中的NaN值填充为0，确保数据完整性
    total_data = total_data.fillna(0)


    # 在页面展示核心数据总览表格
    # st.dataframe()：在Streamlit中展示交互式表格
    # total_data：要展示的数据集
    # use_container_width=True：表格宽度自适应页面容器，提升显示效果
    # column_config：自定义表格列的配置，优化显示样式
    # st.column_config.TextColumn：文本列配置，指定显示名称和宽度
    # st.column_config.NumberColumn：数值列配置，指定显示名称、格式（保留1位小数）和宽度
    # hide_index=True：隐藏表格的行索引，使表格更简洁
    st.dataframe(
        total_data,
        use_container_width=True,
        column_config={
            "专业": st.column_config.TextColumn("专业名称", width="medium"),
            "男": st.column_config.NumberColumn("男生人数", width="small"),
            "女": st.column_config.NumberColumn("女生人数", width="small"),
            "总人数": st.column_config.NumberColumn("总人数", width="small"),
            "男生占比(%)": st.column_config.NumberColumn("男生占比(%)", format="%.1f", width="small"),
            "女生占比(%)": st.column_config.NumberColumn("女生占比(%)", format="%.1f", width="small"),
            "平均学习时长(小时)": st.column_config.NumberColumn("平均学习时长(小时)", format="%.1f", width="small"),
            "期中平均分": st.column_config.NumberColumn("期中平均分", format="%.1f", width="small"),
            "期末平均分": st.column_config.NumberColumn("期末平均分", format="%.1f", width="small"),
            "期末成绩标准差": st.column_config.NumberColumn("期末成绩标准差", format="%.1f", width="small"),
            "平均出勤率(%)": st.column_config.NumberColumn("平均出勤率(%)", format="%.1f", width="small"),
        },
        hide_index=True
    )


    # 分隔线
    st.markdown("***")

    # ======== 1. 各专业男女性别比例分析模块

    # 设置模块标题，使用序号区分不同分析模块
    st.header("1.各专业男女性别比例")
    # 分割页面为两列，列宽比例为2:1，用于分别展示图表和数据表格
    col1, col2 = st.columns([2, 1])


    # 提取数据中所有不重复的专业名称，用于后续数据处理
    zy_unique = data["专业"].dropna().unique().tolist()
    # 重新按专业和性别分组统计人数（与前文逻辑一致，确保数据一致性）
    gender_count = data.groupby(["专业", "性别"]).size().reset_index(name="人数")


    # 计算各专业的总人数，用于后续计算性别占比
    major_total = gender_count.groupby("专业")["人数"].sum().reset_index(name="总人数")
    # 合并人数数据和总人数数据，得到每个专业的性别人数及总人数
    gender_ratio = pd.merge(gender_count, major_total, on="专业")
    # 计算每个性别在对应专业中的占比（百分比），保留1位小数
    gender_ratio["比例(%)"] = (gender_ratio["人数"] / gender_ratio["总人数"] * 100).round(1)
    # 将占比中的0.0替换为0，简化数据显示
    gender_ratio["比例(%)"] = gender_ratio["比例(%)"].replace(0.0, 0)


    # 将性别占比数据转换为宽表，便于绘制分组柱状图
    ratio_wide = gender_ratio.pivot_table(
        index="专业",
        columns="性别",
        values="比例(%)",
        fill_value=0
    ).reset_index()

    # 重新设置列名，确保列顺序为专业、女、男
    ratio_wide.columns = ["专业", "女", "男"]


    # 在第一列中绘制性别比例分组柱状图
    with col1:
        
        # px.bar()：绘制柱状图
        # ratio_wide.melt()：将宽表转换为长表，适配plotly的输入格式
        # id_vars="专业"：保留专业列为标识列
        # var_name="性别"：将原列名（女、男）转为“性别”列的数值
        # value_name="比例(%)"：将原数值转为“比例(%)”列的数值
        # x="专业"：x轴为专业名称
        # y="比例(%)"：y轴为性别占比
        # color="性别"：按性别区分颜色
        # barmode="group"：分组柱状图（并列显示）
        # title：图表标题
        # labels：自定义轴标签，将“比例(%)”改为“性别占比(%)”
        # height=400：设置图表高度为400像素
        fig_bar = px.bar(
            ratio_wide.melt(id_vars="专业", var_name="性别", value_name="比例(%)"),
            x="专业",
            y="比例(%)",
            color="性别",
            barmode="group",
            title="各专业男女性别比例对比",
            labels={"比例(%)": "性别占比(%)"},
            height=400
        )
        
        # st.plotly_chart()：在Streamlit中展示plotly图表
        # use_container_width=True：图表宽度自适应列容器
        st.plotly_chart(fig_bar, use_container_width=True)


    # 在第二列中展示性别比例数据表格
    with col2:
        # st.markdown()：显示markdown格式的文本，设置为6级标题样式
        st.markdown("###### 性别比例数据")
        # 展示性别比例宽表数据，自定义列配置
        st.dataframe(
            ratio_wide,
            use_container_width=True,
            column_config={
                "专业": st.column_config.TextColumn("专业", width="medium"),
                "女": st.column_config.NumberColumn("女(%)", format="%.0f"),
                "男": st.column_config.NumberColumn("男(%)", format="%.0f")
            }
        )

    # 分隔线
    st.markdown("***")

    # ======== 2. 各专业学习指标对比分析模块
    st.header("2.各专业学习指标对比")

    # 分割页面为两列，列宽比例为3:1
    col3, col4 = st.columns([3, 1])

    # 按专业分组，计算平均学习时长、期中平均分、期末平均分，保留1位小数
    major_metrics = data.groupby("专业").agg(
        study_hours=("每周学习时长（小时）", "mean"),
        midterm_score=("期中考试分数", "mean"),
        final_score=("期末考试分数", "mean")
    ).round(1).reset_index()

    # 在第一列中绘制组合图表（柱状图+折线图）
    with col3:
        # go.Figure()：创建空的plotly图表对象，用于自定义多轨迹图表
        fig = go.Figure()
        # 添加平均学习时长柱状图轨迹
        # x：x轴数据为专业名称
        # y：y轴数据为平均学习时长
        # name：轨迹名称（显示在图例中）
        # marker_color：柱状图颜色（十六进制颜色码）
        # yaxis="y1"：使用左侧主y轴
        fig.add_trace(go.Bar(
            x=major_metrics["专业"],
            y=major_metrics["study_hours"],
            name="平均学习时间",
            marker_color="#8ecae6",
            yaxis="y1"
        ))
        
        # 添加平均期中成绩折线图轨迹
        # mode="lines+markers"：显示折线和数据点
        # line：设置折线颜色和宽度
        # marker：设置数据点大小
        # yaxis="y2"：使用右侧次y轴
        fig.add_trace(go.Scatter(
            x=major_metrics["专业"],
            y=major_metrics["midterm_score"],
            name="平均期中成绩",
            mode="lines+markers",
            line=dict(color="#fb8500", width=2),
            marker=dict(size=6),
            yaxis="y2"
        ))
        
        # 添加平均期末成绩折线图轨迹
        fig.add_trace(go.Scatter(
            x=major_metrics["专业"],
            y=major_metrics["final_score"],
            name="平均期末成绩",
            mode="lines+markers",
            line=dict(color="#219e45", width=2),
            marker=dict(size=6),
            yaxis="y2"
        ))
        
        # 配置图表布局
        # title_text：图表标题
        # title_font：设置标题字体大小
        # yaxis：配置左侧主y轴（平均学习时间）
        # yaxis2：配置右侧次y轴（成绩），overlaying="y"表示与主y轴重叠，side="right"显示在右侧
        # legend：配置图例位置，orientation="h"水平显示，yanchor="bottom"底部对齐
        # height：图表高度
        fig.update_layout(
            title_text="各专业平均学习时间与成绩对比",
            title_font=dict(size=14),
            yaxis=dict(
                title="平均学习时间(小时)",
                title_font=dict(color="#8ecae6"),
                tickfont=dict(color="#8ecae6"),
                range=[0, 30]
            ),
            yaxis2=dict(
                title="平均分数",
                overlaying="y",
                side="right",
                range=[70, 90]
            ),
            legend=dict(
                orientation="h",
                yanchor="bottom",
                y=1.02,
                xanchor="left",
                x=0
            ),
            height=400
        )
        
        # 展示图表
        st.plotly_chart(fig, use_container_width=True)


    # 在第二列中展示学习指标详细数据表格
    with col4:
        st.markdown("### 详细数据")
        # 重命名列，将英文列名改为中文，提升可读性
        table_data = major_metrics.rename(columns={
            "study_hours": "平均学习时间(小时)",
            "midterm_score": "期中成绩",
            "final_score": "期末成绩"
        })[["专业", "平均学习时间(小时)", "期中成绩", "期末成绩"]]
        # 展示数据表格
        st.dataframe(
            table_data,
            use_container_width=True,
            column_config={
                "专业": st.column_config.TextColumn("专业", width="small"),
                "平均学习时间(小时)": st.column_config.NumberColumn("平均学习时间(小时)", format="%.1f"),
                "期中成绩": st.column_config.NumberColumn("期中成绩", format="%.1f"),
                "期末成绩": st.column_config.NumberColumn("期末成绩", format="%.1f")
            },
            hide_index=True
        )
        

    # 分隔线
    st.markdown("***")

    # ======== 3. 各专业出勤率分析模块
    st.header("3.各专业出勤率分析")

    # 分割页面为两列，列宽比例为3:1
    col5, col6 = st.columns([3, 1])

    # 按专业分组，计算平均出勤率（原始小数），保留1位小数
    major_attendance = data.groupby("专业").agg(
        attendance=("上课出勤率", "mean")
    ).reset_index()

    # 将出勤率转换为百分比，保留1位小数
    major_attendance["attendance"] = (major_attendance["attendance"] * 100).round(1)


    # 在第一列中绘制出勤率柱状图
    with col5:
        # 创建plotly图表对象，添加柱状图轨迹
        fig_att = go.Figure(
            data=go.Bar(
                x=major_attendance["专业"],
                y=major_attendance["attendance"],
                # marker：配置柱状图样式，使用颜色渐变
                # colorscale：颜色渐变方案（YlGnBu_r为反向的黄-绿-蓝）
                # color：根据出勤率数值映射颜色
                # colorbar：配置颜色条，显示出勤率数值与颜色的对应关系
                marker=dict(
                    colorscale="YlGnBu_r",
                    color=major_attendance["attendance"],
                    colorbar=dict(
                        title="出勤率(%)",
                        orientation="v",
                        x=1.05,
                        y=0.5
                    )
                ),
                name="平均出勤率"
            )
        )
        
        # 配置图表布局
        fig_att.update_layout(
            title_text="各专业平均出勤率",
            title_font=dict(size=14),
            xaxis=dict(title="专业"),
            yaxis=dict(title="出勤率(%)", range=[0, 100]),
            height=400,
            # margin：设置图表右边距，避免颜色条被截断
            margin=dict(r=100)
        )
        
        # 展示图表
        st.plotly_chart(fig_att, use_container_width=True)


    # 在第二列中展示出勤率排名数据表格
    with col6:
        # 按出勤率降序排序，重置索引（删除原索引）
        rank_data = major_attendance.sort_values(by="attendance", ascending=False).reset_index(drop=True)
        # 添加排名列，从1开始计数
        rank_data["排名"] = rank_data.index + 1
        # 重命名列，将attendance改为平均出勤率(%)
        rank_table = rank_data[["排名", "专业", "attendance"]].rename(
            columns={"attendance": "平均出勤率(%)"}
        )
        st.markdown("### 出勤率排名")

        # 展示排名表格
        st.dataframe(
            rank_table,
            use_container_width=True,
            column_config={
                "排名": st.column_config.NumberColumn("排名", width="small"),
                "专业": st.column_config.TextColumn("专业", width="medium"),
                "平均出勤率(%)": st.column_config.NumberColumn("平均出勤率(%)", format="%.1f")
            },
            hide_index=True
        )

    # 分隔线
    st.markdown("***")

    # ======== 4. 各专业期中和期末考试平均分分析模块 
    st.header("4.各专业期中和期末考试平均分分析")

    # 分割页面为两列，列宽比例为3:1
    col7, col8 = st.columns([3, 1])


    # 按专业分组，计算期中、期末平均分，保留1位小数
    exam_scores = data.groupby("专业").agg(
        midterm=("期中考试分数", "mean"),
        final=("期末考试分数", "mean")
    ).round(1).reset_index()


    # 在第一列中绘制期中、期末成绩折线图
    with col7:
        # 创建plotly图表对象
        fig_exam = go.Figure()
        # 添加期中考试成绩折线图轨迹
        fig_exam.add_trace(go.Scatter(
            x=exam_scores["专业"],
            y=exam_scores["midterm"],
            name="期中考试平均分数",
            mode="lines+markers",
            line=dict(color="#fb8500", width=2),
            marker=dict(size=6)
        ))

        
        # 添加期末考试成绩折线图轨迹
        fig_exam.add_trace(go.Scatter(
            x=exam_scores["专业"],
            y=exam_scores["final"],
            name="期末考试平均分数",
            mode="lines+markers",
            line=dict(color="#219e45", width=2),
            marker=dict(size=6)
        ))

        
        # 配置图表布局
        fig_exam.update_layout(
            title_text="各专业期中和期末考试平均分数对比",
            title_font=dict(size=14),
            yaxis=dict(title="分数", range=[60, 100]),
            xaxis=dict(title="专业"),
            height=400,
            legend=dict(
                orientation="h",
                yanchor="bottom",
                y=1.02,
                xanchor="left",
                x=0
            )
        )

        
        # 展示图表
        st.plotly_chart(fig_exam, use_container_width=True)

    # 在第二列中展示考试分数详细数据表格
    with col8:
        st.markdown("### 考试分数详情")
        
        # 重命名列
        table_exam = exam_scores.rename(columns={
            "midterm": "期中考试平均分数",
            "final": "期末考试平均分数"
        })
        
        # 展示数据表格
        st.dataframe(
            table_exam,
            use_container_width=True,
            column_config={
                "专业": st.column_config.TextColumn("专业", width="medium"),
                "期中考试平均分数": st.column_config.NumberColumn("期中考试平均分数", format="%.1f"),
                "期末考试平均分数": st.column_config.NumberColumn("期末考试平均分数", format="%.1f")
            },
            hide_index=True
        )
        

    # 分隔线
    st.markdown("***")

    # ======== 5. 大数据管理专业专项分析模块
    st.header("5.大数据管理专业专项分析")

    # 筛选出数据中专业为“大数据管理”的行，复制数据避免原数据被修改
    bd_subset = data[data["专业"] == "大数据管理"].copy()


    # 判断是否存在大数据管理专业的数据
    if bd_subset.empty:
        
        # 若不存在，显示警告信息
        st.warning("未找到“大数据管理”专业的数据")
    else:
        # 若存在，计算该专业的关键指标
        avg_attendance = (bd_subset["上课出勤率"].mean() * 100).round(1)
        avg_final_score = bd_subset["期末考试分数"].mean().round(1)

        # 计算及格率：期末考试分数≥60的人数占比（百分比）
        pass_rate = ((bd_subset["期末考试分数"] >= 60).mean() * 100).round(1)
        avg_study_hours = bd_subset["每周学习时长（小时）"].mean().round(1)


        # 分割页面为四列，用于展示关键指标卡片
        card_col1, card_col2, card_col3, card_col4 = st.columns(4)

        with card_col1:
            # st.metric()：展示关键指标卡片，包含标签和数值
            st.metric(label="平均出勤率", value=f"{avg_attendance}%")
        with card_col2:
            st.metric(label="平均期末成绩", value=f"{avg_final_score}分")
        with card_col3:
            st.metric(label="及格率", value=f"{pass_rate}%")
        with card_col4:
            st.metric(label="平均学习时间", value=f"{avg_study_hours}小时")


        # 分割页面为两列，用于展示成绩分布直方图和箱线图
        chart_col1, chart_col2 = st.columns(2)

        with chart_col1:
            # 绘制期末成绩分布直方图
            fig_hist = go.Figure(
                go.Histogram(
                    x=bd_subset["期末考试分数"],
                    marker_color="#219e45",
                    name="期末成绩分布"
                )
            )
            
            fig_hist.update_layout(
                title="大数据管理专业期末成绩分布",
                title_font=dict(size=14),
                xaxis=dict(title="期末成绩"),
                yaxis=dict(title="人数"),
                height=300
            )
            
            st.plotly_chart(fig_hist, use_container_width=True)


        with chart_col2:
            # 绘制期末成绩箱线图
            fig_box = go.Figure(
                go.Box(
                    y=bd_subset["期末考试分数"],
                    marker_color="#219e45",
                    name="期末成绩箱线图"
                )
            )
            
            fig_box.update_layout(
                title="大数据管理专业期末成绩箱线图",
                title_font=dict(size=14),
                yaxis=dict(title="期末成绩"),
                height=300
            )
            
            st.plotly_chart(fig_box, use_container_width=True)

    # 分隔线
    st.markdown("***")

    # ======== 6. 各专业学习时间与成绩相关性分析模块 
    st.header("6.各专业学习时间与成绩相关性分析")

    # 分割页面为三列，列宽比例为3:3:2
    col9, col10, col11 = st.columns([3, 3, 2])

    # 筛选出所需列，删除包含缺失值的行，保证相关性计算的准确性
    corr_individual = data[["专业", "每周学习时长（小时）", "期末考试分数"]].dropna().copy()


    # 按专业分组，计算平均学习时长和平均期末成绩，保留1位小数（无特殊字符列名）
    corr_major = corr_individual.groupby("专业").agg(
        平均学习时长=("每周学习时长（小时）", "mean"),
        平均期末成绩=("期末考试分数", "mean")
    ).round(1).reset_index()


    # 重命名列，添加括号提升可读性
    corr_major.rename(
        columns={
            "平均学习时长": "平均学习时长(小时)",
        },
        inplace=True
    )


    # 定义函数：计算每个专业的学习时长与成绩的皮尔逊相关系数
    def calculate_corr(group):

        # corr()：计算相关系数矩阵
        # iloc[0, 1]：提取矩阵中学习时长与成绩的相关系数
        # round(2)：保留2位小数
        return group[["每周学习时长（小时）", "期末考试分数"]].corr().iloc[0, 1].round(2)


    # 按专业分组应用函数，得到每个专业的相关系数，命名为“相关系数”
    major_corr = corr_individual.groupby("专业").apply(calculate_corr).reset_index(name="相关系数")

    # 合并相关系数数据与平均学习时长、成绩数据
    major_corr = pd.merge(major_corr, corr_major, on="专业")

    # 在第一列中绘制学习时长与成绩的散点图
    with col9:
        fig_scatter = px.scatter(
            corr_individual,
            x="每周学习时长（小时）",
            y="期末考试分数",
            color="专业",
            title="各专业个体学习时间与期末成绩相关性",
            labels={
                "每周学习时长（小时）": "每周学习时长(小时)",
                "期末考试分数": "期末成绩"
            },
            opacity=0.7,
            # trendline="ols",  # 可选：添加普通最小二乘拟合线，需安装statsmodels库
            height=400
        )
        
        fig_scatter.update_layout(
            title_font=dict(size=14),
            xaxis=dict(title="每周学习时长(小时)"),
            yaxis=dict(title="期末成绩", range=[60, 100]),
            # 配置图例位置，避免遮挡数据
            legend=dict(orientation="v", yanchor="middle", y=0.5, xanchor="right", x=1.1)
        )
        
        st.plotly_chart(fig_scatter, use_container_width=True)


    # 在第二列中绘制学习时长与成绩的相关性热力图
    with col10:
        
        # 将数据转换为宽表，用于计算相关系数矩阵
        heatmap_data = corr_major.pivot_table(
            index="专业",
            values=["平均学习时长(小时)", "平均期末成绩"]
        )
        
        # 计算相关系数矩阵，保留2位小数
        corr_matrix = heatmap_data.corr().round(2)

        # 绘制热力图
        fig_heatmap = px.imshow(
            corr_matrix,
            title="专业层面学习时间与成绩相关性热力图",
            labels=dict(color="相关系数"),
            color_continuous_scale="RdYlBu_r",
            text_auto=True,  # 在热力图单元格中显示相关系数数值
            height=400
        )

        # 配置热力图布局，修复颜色条orientation参数（v表示垂直）
        fig_heatmap.update_layout(
            title_font=dict(size=14),
            coloraxis_colorbar=dict(title="相关系数", orientation="v", x=1.05)
        )
        st.plotly_chart(fig_heatmap, use_container_width=True)


    # 在第三列中展示相关性详细数据表格
    with col11:
        st.markdown("### 相关性详情")

        # 选择所需列并优化列名
        table_corr = major_corr[[
            "专业", "平均学习时长(小时)", "平均期末成绩", "相关系数"
        ]].rename(columns={
            "相关系数": "学习时间-成绩相关系数"
        })

        # 展示数据表格
        st.dataframe(
            table_corr,
            use_container_width=True,
            column_config={
                "专业": st.column_config.TextColumn("专业", width="small"),
                "平均学习时长(小时)": st.column_config.NumberColumn("平均学习时长(小时)", format="%.1f"),
                "平均期末成绩": st.column_config.NumberColumn("平均期末成绩", format="%.1f"),
                "学习时间-成绩相关系数": st.column_config.NumberColumn("相关系数", format="%.2f")
            },
            hide_index=True
        )
        
    # 分隔线
    st.markdown("***")

    # ======== 7. 各专业期中-期末成绩变化分析模块 
    st.header("7.各专业期中-期末成绩变化分析")

    # 分割页面为三列，列宽比例为3:3:2，更换列变量名避免与前序重复
    col12, col13, col14 = st.columns([3, 3, 2])

    # 按专业分组，计算期中、期末平均分，保留1位小数
    score_change = data.groupby("专业").agg(
        midterm_avg=("期中考试分数", "mean"),
        final_avg=("期末考试分数", "mean")
    ).round(1).reset_index()

    # 计算成绩变化差值：期末平均分 - 期中平均分，保留1位小数
    score_change["成绩变化差值"] = (score_change["final_avg"] - score_change["midterm_avg"]).round(1)

    # 将宽表转换为长表，适配雷达图绘制
    radar_data = score_change.melt(
        id_vars=["专业"],
        value_vars=["midterm_avg", "final_avg"],
        var_name="成绩类型",
        value_name="分数"
    )

    # 在第一列中绘制成绩变化差值柱状图
    with col12:
        # 根据成绩变化差值设置柱状图颜色：正数为绿色，负数为橙色，0为灰色
        colors = [
            "#219e45" if x > 0 else "#fb8500" if x < 0 else "#999999"
            for x in score_change["成绩变化差值"]
        ]
        
        # 绘制柱状图
        fig_diff_bar = go.Figure(
            go.Bar(
                x=score_change["专业"],
                y=score_change["成绩变化差值"],
                marker_color=colors,
                name="成绩变化差值（期末-期中）"
            )
        )
        
        # 配置布局，添加水平参考线（y=0）
        fig_diff_bar.update_layout(
            title_text="各专业成绩变化差值（期末-期中）",
            title_font=dict(size=14),
            xaxis=dict(title="专业"),
            yaxis=dict(title="成绩变化差值（分）", gridcolor="#e0e0e0"),
            height=400,
            # 添加水平虚线，标识差值为0的位置
            shapes=[
                dict(
                    type="line",
                    x0=-0.5, x1=len(score_change["专业"])-0.5,
                    y0=0, y1=0,
                    line=dict(color="#000000", width=1, dash="dash")
                )
            ]
        )
        
        st.plotly_chart(fig_diff_bar, use_container_width=True)


    # 在第二列中绘制期中-期末成绩雷达图
    with col13:
        # 提取所有专业名称
        majors = score_change["专业"].tolist()

        # 创建空的plotly图表对象
        fig_radar = go.Figure()

        # 遍历每个专业，添加雷达图轨迹
        for i, major in enumerate(majors):
            fig_radar.add_trace(go.Scatterpolar(
                r=[score_change.loc[i, "midterm_avg"], score_change.loc[i, "final_avg"]],
                theta=["期中考试", "期末考试"],
                fill="toself",  # 填充雷达图内部区域
                name=major
            ))

        # 配置雷达图布局
        fig_radar.update_layout(
            title_text="各专业期中-期末成绩雷达图",
            title_font=dict(size=14),
            polar=dict(
                radialaxis=dict(visible=True, range=[60, 100])  # 雷达图径向轴范围
            ),
            height=400,
            legend=dict(orientation="v", yanchor="middle", y=0.5)
        )
        
        st.plotly_chart(fig_radar, use_container_width=True)


    # 在第三列中展示成绩变化详细数据表格
    with col14:
        st.markdown("### 成绩变化详情")

        # 重命名列，提升可读性
        table_change = score_change.rename(columns={
            "midterm_avg": "期中考试平均分",
            "final_avg": "期末考试平均分",
            "成绩变化差值": "成绩变化差值（期末-期中）"
        })

        # 展示数据表格
        st.dataframe(
            table_change,
            use_container_width=True,
            column_config={
                "专业": st.column_config.TextColumn("专业", width="small"),
                "期中考试平均分": st.column_config.NumberColumn("期中平均分", format="%.1f"),
                "期末考试平均分": st.column_config.NumberColumn("期末平均分", format="%.1f"),
                "成绩变化差值（期末-期中）": st.column_config.NumberColumn("变化差值", format="%.1f")
            },
            hide_index=True
        )

    # 分隔线
    st.markdown("***")

    # ======== 8. 各专业成绩离散程度分析模块 
    st.header("8.各专业成绩离散程度分析")

    # 分割页面为三列，列宽比例为3:3:2，更换列变量名避免重复
    col15, col16, col17 = st.columns([3, 3, 2])

    # 筛选出所需列，删除包含缺失值的行
    score_dist = data[["专业", "期末考试分数"]].dropna().copy()

    # 按专业分组，计算期末成绩的离散程度指标（标准差、四分位数、平均分）
    score_stats = score_dist.groupby("专业")["期末考试分数"].agg(
        标准差="std",
        下四分位数=lambda x: x.quantile(0.25),
        中位数=lambda x: x.quantile(0.5),
        上四分位数=lambda x: x.quantile(0.75),
        平均分="mean"
    ).round(1).reset_index()

    # 在第一列中绘制期末成绩小提琴图
    with col15:
        # 绘制小提琴图，展示成绩分布的密度
        fig_violin = px.violin(
            score_dist,
            x="专业",
            y="期末考试分数",
            color="专业",
            box=True,  # 在小提琴图中显示箱线图
            points="outliers",  # 显示异常值
            title="各专业期末成绩分布（小提琴图）",
            height=400
        )

        # 配置小提琴图布局
        fig_violin.update_layout(
            title_font=dict(size=14),
            xaxis=dict(title="专业"),
            yaxis=dict(title="期末考试分数", range=[60, 100]),
            showlegend=False  # 隐藏图例（颜色已按专业区分，无需重复显示）
        )
        st.plotly_chart(fig_violin, use_container_width=True)

    # 在第二列中绘制期末成绩标准差柱状图
    with col16:
        # 绘制柱状图，展示各专业成绩的标准差
        fig_std_bar = go.Figure(
            go.Bar(
                x=score_stats["专业"],
                y=score_stats["标准差"],
                marker_color="#8ecae6",
                name="期末成绩标准差"
            )
        )

        # 配置布局，添加标题说明标准差的意义
        fig_std_bar.update_layout(
            title_text="各专业期末成绩标准差（数值越大，成绩越分散）",
            title_font=dict(size=14),
            xaxis=dict(title="专业"),
            yaxis=dict(title="标准差", gridcolor="#e0e0e0"),
            height=400
        )
        st.plotly_chart(fig_std_bar, use_container_width=True)


    # 在第三列中展示成绩离散程度详细数据表格
    with col17:
        st.markdown("### 离散程度详情")

        # 重命名列，优化显示名称
        table_stats = score_stats.rename(columns={
            "标准差": "期末成绩标准差",
            "下四分位数": "下四分位数（Q1）",
            "中位数": "中位数（Q2）",
            "上四分位数": "上四分位数（Q3）",
            "平均分": "期末平均分"
        })

        # 展示数据表格
        st.dataframe(
            table_stats,
            use_container_width=True,
            column_config={
                "专业": st.column_config.TextColumn("专业", width="small"),
                "期末成绩标准差": st.column_config.NumberColumn("标准差", format="%.1f"),
                "下四分位数（Q1）": st.column_config.NumberColumn("Q1", format="%.1f"),
                "中位数（Q2）": st.column_config.NumberColumn("Q2", format="%.1f"),
                "上四分位数（Q3）": st.column_config.NumberColumn("Q3", format="%.1f"),
                "期末平均分": st.column_config.NumberColumn("平均分", format="%.1f")
            },
            hide_index=True
        )
# ---------------------- 页面3：成绩预测 ----------------------
elif st.session_state["current_page"] == "成绩预测":
    # 导入并执行成绩预测页面代码
    import predictsc
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
    with st.form("predictsc_form"):
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
                        
