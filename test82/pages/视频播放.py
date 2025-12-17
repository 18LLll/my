import streamlit as st


st.set_page_config(page_title="视频播放",page_icon="⏯",layout="wide")
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

# 检查内存中是否有'ind'（即当前播放集数索引），无则初始化为0（默认播放第1集）
if 'ind' not in st.session_state:
    st.session_state['ind']=0
    
# 获取当前播放剧集的标题
current=video_arr[st.session_state['ind']]['title']
# 渲染标题样式，展示标题
st.markdown(f"<h3 style='color:#FF8C00; text-align: center;'>当前播放：{current}</h3>", unsafe_allow_html=True)

# 在页面上播放当前剧集的视频
st.video(video_arr[st.session_state['ind']]['url'],autoplay=True)

# 获取当前剧集的介绍、主演信息和对应的海报图片
current_text=video_arr[st.session_state['ind']]['text']
current_yy=video_arr[st.session_state['ind']]['yy']
current_image=video_arr[st.session_state['ind']]['image']

# 美化展示剧集信息
with st.container(border=True):
    st.markdown("<h5 style='color:#4169E1;'>📝剧集介绍</h5>", unsafe_allow_html=True)
    st.markdown(f"<p style='line-height: 1.6;'>{current_text}</p>", unsafe_allow_html=True)

# 定义函数，接收集数索引i，更新会话状态的'ind'
def play(i):
    st.session_state['ind']=int(i)

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
