import streamlit as st
import pandas as pd
import numpy as np
import datetime

#修改标签页文字和图标
st.set_page_config(page_title="我的网站",page_icon="💻",layout="wide")

st.title("My网站")
tab1, tab2, tab3,tab4,tab5,tab6 = st.tabs(["数字档案", "南宁美食数据仪表", "相册","音乐播放器","视频网站","个人简历"])

with tab1:
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

with tab2:

    # 餐厅数据
    restaurants_data = {
        "餐厅": ["兰州拉面", "螺蛳粉", "肯德基", "小汤总", "华莱士","朴大叔"],
        "类型": ["西北风味面食", "中式快餐", "西式快餐", "中餐", "西式快餐","韩式快餐"],
        "评分": [4.6, 4.2, 4.7, 4.3, 4.1,4.4],
        "人均消费(元)": [15, 12,50, 22, 16,18],
       
    }
    # 创建餐厅数据框
    df = pd.DataFrame(restaurants_data)

    # 创建地图坐标数据
    map_data={
             "latitude": [22.854301, 22.864321, 22.814321, 22.834321, 22.873774],
             "longitude": [108.222763, 108.322742, 108.262742, 108.212742, 108.302431]
    }
    # 创建地图坐标数据框
    map_df=pd.DataFrame(map_data)
    #显示地图
    st.map(map_df)

    #分割线
    st.markdown('***')
    st.header("餐厅数据")
    # 使用write()方法展示数据框
    st.write(df)

    #分割线
    st.markdown('***')
    #标题
    st.title("🌟餐厅评分")
    # 修改df，用餐厅列作为df的索引，替换原有的索引
    df.set_index('餐厅', inplace=True)
    # 通过y指定评分所在这一列为条形图的y轴
    st.bar_chart(df, y='评分')

    st.markdown('***')
    st.title("💰餐厅人均消费")
    # 修改df，用类型列作为df的索引，替换原有的索引
    df.set_index('类型', inplace=True)
    # 通过y指定人均消费(元)所在这一列为折线图的y轴，并通过width、height和use_container_width指定折线图的宽度和高度
    st.line_chart(df, y='人均消费(元)',width=800, height=500, use_container_width=False)

    #分割线
    st.markdown('***')
    #标题
    st.title("📈餐厅一年价格趋势")
    # 价格走势数据
    price_data={
            '月份':["01月", "02月", "03月", "04月", "05月","06月","07月", "08月", "09月", "10月", "11月","12月"],
            '兰州拉面':[10,15,12,13,20,11,14,16,18,10,11,16],
            '螺蛳粉':[11,10,15,19,13,14,10,10,16,17,11,12],
            '肯德基':[23,25,19,50,78,29,25,40,30,20,26,32],
            '小汤总':[19,16,18,15,20,26,28,46,75,23,34,30],
            '华莱士':[10,21,11,15,15,13,46,75,16,42,65,13],
            '朴大叔':[8,14,10,16,23,19,18,10,22,23,10,19],
    }
    # 创建价格走势数据框
    df1 = pd.DataFrame(price_data)
    # 通过x指定月份所在这一列为折线图的x轴，并通过width、height和use_container_width指定折线图的宽度和高度
    st.line_chart(df1, x='月份',width=800, height=500, use_container_width=False)

    #分割线
    st.markdown('***')
    # 时间人流量数据
    time_data={
            '时间':["10:00", "11:00", "12:00", "13:00", "16:00","17:00","18:00", "19:00", "20:00"],
            '兰州拉面':[3,5,10,20,6,15,22,12,7],
            '螺蛳粉':[4,3,8,17,8,15,45,16,8],
            '肯德基':[15,13,78,98,16,13,13,26,16],
            '小汤总':[13,32,21,13,19,19,13,21,24],
            '华莱士':[16,64,32,21,16,5,7,9,9],
            '朴大叔':[44,21,35,18,9,18,16,11,17],
    }
    st.title("🕐用餐高峰期")
    # 创建人流量数据框
    df2= pd.DataFrame(time_data)
    # 通过x指定时间所在这一列为面积图的x轴，并通过width、height和use_container_width指定面积图的宽度和高度
    st.area_chart(df2, x='时间',width=800, height=500, use_container_width=False)

with tab3:

    #标题
    st.title("动物相册")

    # 将当前的图片索引存储在内存的img_ind变量中，避免和其他页面的ind冲突
    if 'img_ind' not in st.session_state:
        st.session_state['img_ind']=0

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
    st.image(images[st.session_state['img_ind']]['url'],caption=images[st.session_state['img_ind']]['text'])
    #实现上一张按钮的函数
    def lastImg():
        st.session_state['img_ind']=(st.session_state['img_ind']-1)%len(images)
    #实现下一张按钮的函数
    def nextImg():
        st.session_state['img_ind']=(st.session_state['img_ind']+1)%len(images)
    #分列容器
    c1,c2=st.columns(2)
    #使用分裂容器排列按钮布局
    with c1:
        st.button("上一张",on_click=lastImg,use_container_width=True)
    with c2:
        st.button("下一张",on_click=nextImg,use_container_width=True)

with tab4:


    st.title("🎶简易音乐播放器")
    st.markdown("##### 使用Streamlit制作的音乐播放器，支持切歌和播放控制")

    # 将当前的音乐索引存储在内存的music_ind变量中，避免和其他页面的ind冲突
    if 'music_ind' not in st.session_state:
        st.session_state['music_ind']=0

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
        st.session_state['music_ind']=(st.session_state['music_ind']-1)%len(audio_file)
    #实现下一首按钮的函数
    def nextmusic():
        st.session_state['music_ind']=(st.session_state['music_ind']+1)%len(audio_file)
        
    #分列容器，分为左右两边
    c1,c2 = st.columns([1, 2])

    #对左右两边进行排列，左边显示图片和文字，右边显示歌曲信息和按钮
    with c1:
        st.image(audio_file[st.session_state['music_ind']]['image'],caption=audio_file[st.session_state['music_ind']]['text'])
    with c2:
        st.subheader(audio_file[st.session_state['music_ind']]['title'])
        st.markdown(f"**歌手**：{audio_file[st.session_state['music_ind']]['artist']}")
        st.markdown(f"**时长**：{audio_file[st.session_state['music_ind']]['duration']}")
        #再次进行左右排列，按钮并排显示
        b1,b2=st.columns(2)
        with b1:
            st.button("上一首⏮",on_click=lastmusic,use_container_width=True)
        with b2:
            st.button("下一首⏭",on_click=nextmusic,use_container_width=True)
             
    #在页面中显示音频播放控制条
    st.audio(audio_file[st.session_state['music_ind']]['url'])

with tab5:

    # 标题
    st.title('📺视频播放器📺')

    # 分割线
    st.markdown('***')
    # 用数组存储视频相关信息
    video_arr=[{
        'url':'https://upos-sz-mirrorcos.bilivideo.com/upgcxcode/53/96/1619299653/1619299653-1-16.mp4?e=ig8euxZM2rNcNbRVhwdVhwdlhWdVhwdVhoNvNC8BqJIzNbfq9rVEuxTEnE8L5F6VnEsSTx0vkX8fqJeYTj_lta53NCM=&trid=585cbb29ba4047e096ff5ece8a7c146p&mid=0&deadline=1765769920&nbs=1&platform=html5&os=estgcos&uipk=5&oi=1939826609&gen=playurlv3&og=cos&upsig=64dcece8d779fd3b7d533ba7243dfab3&uparams=e,trid,mid,deadline,nbs,platform,os,uipk,oi,gen,og&bvc=vod&nettype=0&bw=321145&f=p_0_0&qn_dyeid=&agrr=1&buvid=&build=0&dl=0&orderid=0,1',
        'title':'喜羊羊与灰太狼之跨时空救兵第一集',
        'episode':1,
        'text':'该电视动画讲述了小羊们随慢羊羊村长冰极探险时遭小狼人淘淘设计骗其破坏时空宝石致时空混乱，不同时代的人来到青青草原，世界面临被重置到史前年代的危机，众羊狼为阻止危机联合驾驶嘻哈火车与天狼号穿梭时空送回闯入人物的故事。',
        'yy':'小🐏🐑,🐺,时空迷失者',
        'image':'http://i.gtimg.cn/qqlive/img/jpgcache/files/qqvideo/hori/o/o5e8ihhilym9plx_big.jpg'
        },{
        'url':'https://upos-sz-mirrorcos.bilivideo.com/upgcxcode/74/71/31520327174/31520327174-1-192.mp4?e=ig8euxZM2rNcNbR1nWdVhwdlhWRHhwdVhoNvNC8BqJIzNbfq9rVEuxTEnE8L5F6VnEsSTx0vkX8fqJeYTj_lta53NCM=&nbs=1&os=estgcos&platform=html5&trid=d56c7fe4d09640e58d98128bc820f2bO&deadline=1765770649&uipk=5&gen=playurlv3&og=cos&mid=0&oi=1385955528&upsig=2b9743e09a83bc361884e5ddcc2ad1fa&uparams=e,nbs,os,platform,trid,deadline,uipk,gen,og,mid,oi&bvc=vod&nettype=1&bw=954176&buvid=&build=7330300&dl=0&f=O_0_0&agrr=1&orderid=0,3',
        'title':'喜羊羊与灰太狼之奇妙大营救',
        'episode':2,
        'text':'该动画片讲述了奇猫国突遭妙狗国入侵后，喜羊羊与伙伴们化身猫形态展开营救行动，却在过程中被击落并分散至妙狗国五层区域‌。随着剧情推进，他们各自突破地域考验、升级奇力，却发现妙狗国国王暗中操控黑暗能量，意图挑拨羊狼关系并控制两国‌。最终，小羊们通过友情唤醒黑化的灰太狼，联手封印黑暗能量，化解两国矛盾并重建和平‌。',
        'yy':'小🐏🐑,🐺,奇猫国居民' ,
        'image':'https://so1.360tres.com/t0132fcd7aaf1bfcb6e.jpg'
        },{
        'url':'https://upos-sz-mirrorcos.bilivideo.com/upgcxcode/80/68/153486880/153486880_da8-1-16.mp4?e=ig8euxZM2rNcNbRVhwdVhwdlhWdVhwdVhoNvNC8BqJIzNbfq9rVEuxTEnE8L5F6VnEsSTx0vkX8fqJeYTj_lta53NCM=&trid=fedf711c4d7140e19376781a9ac0f48p&gen=playurlv3&os=estgcos&og=cos&mid=0&oi=143446004&platform=html5&deadline=1765770372&nbs=1&uipk=5&upsig=63c3ab0cff08e2115bb322e4766e30be&uparams=e,trid,gen,os,og,mid,oi,platform,deadline,nbs,uipk&bvc=vod&nettype=0&bw=422448&f=p_0_0&qn_dyeid=&agrr=1&buvid=&build=0&dl=0&orderid=0,1',
        'title':'喜羊羊与灰太狼之羊村守护者第一集',
        'episode':3,
        'text':'该剧讲述了狼将军利用各法宝强化七大恶狼攻打羊村。为保羊村，众羊寻找各种方法，意外获得羊族前辈的神奇武器。一路上小羊们用神奇装备打退群狼多次攻击。被小羊们的善良团结感动的灰太狼，帮助众羊终于打败狼将军，草原实现了真正和平的故事。',
        'yy':'小🐏🐑,🐺,羊村守护者后勤部',
        'image':'https://3img.hitv.com/preview/sp_images/2021/01/26/20210126163938694.jpg?x-oss-process=image/resize,w_280,h_392/format,jpg'
        },{
        'url':'https://upos-sz-mirrorcos.bilivideo.com/upgcxcode/25/34/34086323425/34086323425-1-192.mp4?e=ig8euxZM2rNcNbRVhwdVhwdlhWdVhwdVhoNvNC8BqJIzNbfq9rVEuxTEnE8L5F6VnEsSTx0vkX8fqJeYTj_lta53NCM=&deadline=1765770496&nbs=1&uipk=5&gen=playurlv3&os=estgoss&mid=0&oi=144233936&og=ali&trid=08a24986551d4098a4dc66737a815aeO&platform=html5&upsig=1b34cd7d1fa8033e0f5b47c5e688f7e2&uparams=e,deadline,nbs,uipk,gen,os,mid,oi,og,trid,platform&bvc=vod&nettype=1&bw=683906&dl=0&f=O_0_0&agrr=1&buvid=&build=7330300&orderid=0,3',
        'title':'喜羊羊与灰太狼之决战次时代',
        'episode':4,
        'text':'该动画片讲述了喜羊羊和灰太狼意外地被带到了十五年后，为了回到自己的时空，二人与未来的小羊们收集分散的象星石碎片，并组合象星石。但在过程中，神秘人也派遣厉害的手下来抢夺碎片，于是双方就展开了精彩纷呈的碎片争夺战的故事。',
        'yy':'小🐏🐑,🐺,机器人部队' ,
        'image':'https://pic1.zhimg.com/v2-a068b27298284a74c7c4ae349afd7169_r.jpg?source=1940ef5c'
        },{
        'url':'https://upos-sz-mirrorcos.bilivideo.com/upgcxcode/90/45/32730844590/32730844590-1-192.mp4?e=ig8euxZM2rNcNbRVhwdVhwdlhWdVhwdVhoNvNC8BqJIzNbfq9rVEuxTEnE8L5F6VnEsSTx0vkX8fqJeYTj_lta53NCM=&platform=html5&os=zosbv&nbs=1&uipk=5&mid=0&gen=playurlv3&og=hw&trid=13a5d5a1ecad4ee7bd04ef02c1e3033O&deadline=1765770553&oi=2067284620&upsig=bb2c1513ef3766bcf9d979bc43366f67&uparams=e,platform,os,nbs,uipk,mid,gen,og,trid,deadline,oi&bvc=vod&nettype=1&bw=717839&f=O_0_0&agrr=1&buvid=&build=7330300&dl=0&orderid=0,3',
        'title':'喜羊羊与灰太狼之勇闯四季城',
        'episode':5,
        'text':'传说中,森林里住着邪恶的大魔王，他自称“破影大王”。突然有一天，他来到了四季城，并召集许多怪物，成立怪物城，给四季城带来危机。为了帮助四季城的小精灵脱险，羊村守护者们再度出击，勇闯四季城。不料在途中，喜羊羊竟然意外变成无法自控的“破影大王”，时而清醒，时而捣乱，让整个旅途笑料百出。羊狼们一路闯关，修炼并进阶“勇者”的能力，同时他们也在寻找“净化”喜羊羊的方法。而另一面，破影大王对这群“不速之客”自然不会束手就擒。谁又将成为下一个战胜影王的勇者传奇呢？',
        'yy':'小🐏🐑,🐺,四季城居民' ,
        'image':'https://tu.zhongwen.wiki/images/qiuwenbaike/zh/thumb/b/b7/The_Season_Towns_KV.jpg/640px-The_Season_Towns_KV.jpg'
        }]

    # 检查内存中是否有video_ind（即当前播放集数索引），避免和其他页面的ind冲突
    if 'video_ind' not in st.session_state:
        st.session_state['video_ind']=0
        
    # 获取当前播放剧集的标题
    current=video_arr[st.session_state['video_ind']]['title']
    # 渲染标题样式，展示标题
    st.markdown(f"<h3 style='color:#FF8C00; text-align: center;'>当前播放：{current}</h3>", unsafe_allow_html=True)

    # 在页面上播放当前剧集的视频
    st.video(video_arr[st.session_state['video_ind']]['url'],autoplay=True)

    # 获取当前剧集的介绍、主演信息和对应的海报图片
    current_text=video_arr[st.session_state['video_ind']]['text']
    current_yy=video_arr[st.session_state['video_ind']]['yy']
    current_image=video_arr[st.session_state['video_ind']]['image']

    # 美化展示剧集信息
    with st.container(border=True):
        st.markdown("<h5 style='color:#4169E1;'>📝剧集介绍</h5>", unsafe_allow_html=True)
        st.markdown(f"<p style='line-height: 1.6;'>{current_text}</p>", unsafe_allow_html=True)

    # 定义函数，接收集数索引i，更新会话状态的video_ind
    def play(i):
        st.session_state['video_ind']=int(i)

    # 创建分列布局，共5列，每列放一个切换按钮    
    c=st.columns(5)
    # 遍历每一列，生成对应集数的按钮
    for i,col in enumerate(c):
        with col:
            st.button('第'+str(i+1)+'集',use_container_width=True,on_click=play,args=([i]))

    # 分割线
    st.markdown('***')

    # 创建带边框的容器，展示角色和海报
    with st.container(border=True):
        st.markdown("<h5 style='color:#4169E1; margin-top: 15px;'>🦄主要角色</h5>", unsafe_allow_html=True)
        st.markdown(f"<p style='font-size: 16px;'>{current_yy}</p>", unsafe_allow_html=True)
        # 展示当前剧集对应图片
        st.image(current_image)

with tab6:
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
