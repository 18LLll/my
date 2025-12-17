import streamlit as st
import pandas as pd
import plotly.express as px

def get_dataframe_from_excel():
    # 用pd中的read_excel()读取Excel文件
    df = pd.read_excel(
        'supermarket_sales.xlsx',  # 文件路径及名称
        sheet_name='销售数据',  # 读取名为"销售数据"工作表的数据
        skiprows=1,   #  跳过excel中的第一行，因为第一行是标题
        index_col='订单号'  #将“订单号”这一列作为返回的数据框的索引
    )
    # 提取时间中的小时数，取出原有的'时间'这一列，to_datetime将数据转换成datetime类型
    #format指定原有时间字符串的格式
    #.dt.hour表示转换后的数据框取出小时数作为新列
    #最后赋值给df['小时数']
    df['小时数'] = pd.to_datetime(df["时间"], format="%H:%M:%S").dt.hour
    return df

def add_siderbar_func(df):
    #创建侧边栏
    with st.sidebar:
        #添加侧边栏标题
        st.header("请筛选数据：")
        # 求"城市"列去重复后的值，再赋值
        city_unique = df["城市"].unique().tolist()  # 转列表，避免Pandas数组格式问题
        city = st.multiselect(
            "请选择城市：",
            options=city_unique, #将所有选项设置为city_unique
            default=city_unique,  # 第一次默认选项
        )

        #求"顾客类型"列去重复后的值，再赋值
        customer_type_unique = df["顾客类型"].unique().tolist()
        customer_type = st.multiselect(
            "请选择顾客类型：",
            options=customer_type_unique,#将所有选项设置为customer_type_unique
            default=customer_type_unique,# 第一次默认选项
        )

         # 求"性别"列去重复后的值，再赋值
        gender_unique = df["性别"].unique().tolist()
        gender = st.multiselect(
            "请选择性别：",
            options=gender_unique,#将所有选项设置gender_为unique
            default=gender_unique,# 第一次默认选项
        )
        # query()查询方法，传入过滤条件字符串
        # @xxx：可以通过@使用Streamlit多选下拉按钮'xxx'的值
        df_selection=df.query(
            "城市==@city  & 顾客类型 ==@customer_type & 性别 == @gender"
            )
        return df_selection

def product_line_chart(df):
    # 将df按产品类型列分组，并计算总价列的和，最后按总价排序
    sales_by_product_line = df.groupby(by=["产品类型"])[["总价"]].sum().sort_values(by="总价")


    # px.bar生成条形图
    # x="总价":条形图的长度表示总价
    # y=xxxxxx::条形图的标签是产品类型
    # orientation="h":生成横向的条形图
    # title:设置图表标题，使用HTML标签加粗
    fig_product_sales = px.bar(
        sales_by_product_line,
        x="总价",
        y=sales_by_product_line.index,
        orientation="h",
        title="<b>按产品类型划分的销售额</b>",
        color_discrete_sequence=["#0083B8"]  # 统一图表颜色，更美观
    )

    #将生成的条形图返回
    return fig_product_sales

def hour_chart(df):
    # 将df按'小时数'列分组，并计算'总价'列的和
    sales_by_hour = df.groupby(by=["小时数"])[["总价"]].sum()
    
    # x=sales_by_hour.index:条形图的长度表示小时数
    fig_hour_sales = px.bar(
        sales_by_hour,
        x=sales_by_hour.index,
        y="总价", #条形图的标签是总价
        title="<b>按小时数划分的销售额</b>",
        color_discrete_sequence=["#FF6B6B"]
    )
    
    #将生成的条形图返回
    return fig_hour_sales

def main_page_demo(df):

    """主界面函数"""
    #设置标题
    st.title('📊超市销售仪表板')
    st.divider()  # 增加分隔线，优化布局
    
    #创建关键指标信息区，生成3个列容器
    left_key_col,middle_key_col,right_key_col = st.columns(3)

    #选中数据框中的"总价"列，使用sum()计算"总价"列的和，使用int()求整
    total_sales = int(df["总价"].sum())
    #选中数据框中的"评分"列，使用mean()计算"评分"列的平均值，使用round()四舍五入
    #保留1位小数
    average_rating = round(df["评分"].mean(),1)
    #对刚刚的结果再次四舍五入，只保留整数，并使用int()函数，表示就要整数，增加代码的可读性
    star_rating_string = ":star:" * int(round(average_rating,0))
    #选中数据框中的"总价"列，使用mean()计算"评分"列的平均值，使用round()四舍五入
    #保留2位小数
    average_sale_by_transaction = round(df["总价"].mean(),2)



    with left_key_col:
        st.subheader("总销售额：")
        st.subheader(f"RMB ￥ {total_sales:,}")

    with middle_key_col:
        st.subheader("顾客评分的平均值：")
        st.subheader(f"{average_rating} {star_rating_string}")

    with right_key_col:
        st.subheader("每单的平均销售额：")
        st.subheader(f"RMB ￥ {average_sale_by_transaction}")

    st.divider()#生成一个水平分割线


    #创建图标信息区，生成两个列容器
    left_chart_col,right_chart_col = st.columns(2)

    with left_chart_col:
        #生成纵向条形图
        hour_fig = hour_chart(df)
        #展示生成的Plotly图形，并设置使用父容器的宽度
        st.plotly_chart(hour_fig,use_container_width=True)

    with right_chart_col:
        #生成横向条形图
        product_fig = product_line_chart(df)
        #展示生成的Plotly图形，并设置使用父容器的宽度
        st.plotly_chart(product_fig,use_container_width=True)

def run_app():
    """启动应用"""
    #设置页面
    st.set_page_config(
        page_title="销售仪表板",#标题
        page_icon=":bar_chart:",#图标
        layout="wide"#宽布局
        )
    #将Excel中的销售数据读取到数据框中
    sale_df=get_dataframe_from_excel()
    #添加不同的多选项下拉按钮，并形成筛选后的数据框，构建筛选区
    df_selection = add_siderbar_func(sale_df)
    #构建主界面
    main_page_demo(df_selection)

if __name__ == "__main__":
    run_app()
