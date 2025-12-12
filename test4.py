import streamlit as st

#修改标签页文字和图标
st.set_page_config(page_title="动物相册",page_icon="🦌")
#标题
st.title("动物相册")

#将当前的图片索引存储在内存的ind变量中，如果内存中五ind则设置为0
if 'ind' not in st.session_state:
    st.session_state['ind']=0


#用数组存储图片信息
images=[{
    'url':"http://n.sinaimg.cn/sinakd20117/88/w1080h608/20230707/42ff-adc44db7a87659a260208c21f122364e.jpg",
    'text':'麋鹿'
    },{
    'url':"https://huacheng.gz-cmc.com/upload/news/image/2023/04/28/5bbd0f6a03dc4f96b3f3d942d89eec4d.jpeg",
    'text':'考拉'
        },{
    'url':"https://www.quazero.com/uploads/allimg/140228/1-14022QA428.jpg",
    'text':'小猫'
        }]
#展示图片及其信息在页面中
st.image(images[st.session_state['ind']]['url'],caption=images[st.session_state['ind']]['text'])
#实现上一张按钮的函数
def lastImg():
    st.session_state['ind']=(st.session_state['ind']-1)%len(images)
#实现下一张按钮的函数
def nextImg():
    st.session_state['ind']=(st.session_state['ind']+1)%len(images)
#分列容器
c1,c2=st.columns(2)
#使用分裂容器排列按钮布局
with c1:
    st.button("上一张",on_click=lastImg,use_container_width=True)
with c2:
    st.button("下一张",on_click=nextImg,use_container_width=True)
         

         

