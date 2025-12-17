import streamlit as st

#修改标签页文字和图标
st.set_page_config(page_title='音乐播放器', page_icon='🔉')

st.title("🎶简易音乐播放器")
st.markdown("##### 使用Streamlit制作的音乐播放器，支持切歌和播放控制")

#将当前的音乐索引存储在内存的ind变量中，如果内存中无ind则设置为0
if 'ind' not in st.session_state:
    st.session_state['ind']=0

# 用数组存储音频信息
audio_file =[{
        'title': "没有理由",
        'artist': "永彬Ryan.B/周延英（英子-effie）",
        'duration': "3:35",
        'url':"https://music.163.com/song/media/outer/url?id=550138197.mp3",
        'image':"http://p2.music.126.net/VAux0wpbTJz6timFFHVgLQ==/109951163237307291.jpg?param=130y130",
        'text':'没有理由的歌曲封面'
    },{
        'title': "КаминJONY x EMIN ~ Mix壁炉(快版)",
        'artist': "jony.me/JONY/EMIN",
        'duration': "2:37",
        'url':"https://music.163.com/song/media/outer/url?id=2095997688.mp3",
        'image':"https://musicboxtv.ru/wp-content/uploads/2020/04/EMIN-feat.-JONY-Kamin.jpg",
        'text':'壁炉的歌曲封面'
    },{
        'title': "ICARUS(伊卡洛斯) ",
        'artist': "Tony Ann",
        'duration': "3:19",
        'url':"https://music.163.com/song/media/outer/url?id=2108766934.mp3",
        'image':"http://n.sinaimg.cn/sinacn15/720/w1920h1200/20180319/c7da-fyskeuc2242646.jpg",
        'text':'伊卡洛斯的歌曲封面'
    },{
        'title': "Dusk Till Dawn",
        'artist': "Kurt Hugo Schneider/Kirsten Collins/Blake Rose",
        'duration': "3:09",
        'url':"https://music.163.com/song/media/outer/url?id=1836100414.mp3",
        'image':"http://p1.music.126.net/O2dB0EmvWJslGt1YzHFH2g==/109951165982469757.jpg",
        'text':'Dusk Till Dawn的歌曲封面'
    }]

#实现上一首按钮的函数
def lastmusic():
    st.session_state['ind']=(st.session_state['ind']-1)%len(audio_file)
#实现下一首按钮的函数
def nextmusic():
    st.session_state['ind']=(st.session_state['ind']+1)%len(audio_file)
    
#分列容器，分为左右两边
c1,c2 = st.columns([1, 2])

#对左右两边进行排列，左边显示图片和文字，右边显示歌曲信息和按钮
with c1:
    st.image(audio_file[st.session_state['ind']]['image'],caption=audio_file[st.session_state['ind']]['text'])
with c2:
    st.subheader(audio_file[st.session_state['ind']]['title'])
    st.markdown(f"**歌手**：{audio_file[st.session_state['ind']]['artist']}")
    st.markdown(f"**时长**：{audio_file[st.session_state['ind']]['duration']}")
    #再次进行左右排列，按钮并排显示
    b1,b2=st.columns(2)
    with b1:
        st.button("上一首⏮",on_click=lastmusic,use_container_width=True)
    with b2:
        st.button("下一首⏭",on_click=nextmusic,use_container_width=True)
         
#在页面中显示音频播放控制条
st.audio(audio_file[st.session_state['ind']]['url'])
