import streamlit as st

st.set_page_config(page_title='视频', page_icon='📽', layout='wide')

# 视频及配套信息数据（补充介绍、演职人员、头像）
video_arr = [
    {
        'url': 'https://www.w3schools.com/html/movie.mp4',
        'title': '还珠格格第一部-第1集',
        'intro': '本集讲述了紫薇带着丫鬟金锁从济南来到北京，欲认父乾隆，却阴差阳错与小燕子相识，小燕子仗义答应帮紫薇进宫送信的故事。',
        'cast': [
            {'name': '林心如', 'role': '夏紫薇', 'avatar': 'https://b0.bdstatic.com/ugc/-uh4PU8AW7L8HT9AYEt2iAffdfae3676bc83fd2419d680f1b66e83.jpg'},# 示例头像链接
            {'name': '苏有朋', 'role': '五阿哥永琪', 'avatar': 'https://q3.itc.cn/images01/20250527/49aaeaa71540434b982b45ad2b5ec4b1.jpeg'}
        ]
    },{
        'url': 'https://www.w3school.com.cn/example/html5/mov_bbb.mp4',
        'title': '还珠格格第一部-第2集',
        'intro': '小燕子误打误撞闯入围场，被乾隆误认为是自己失散多年的女儿，当场被封为“还珠格格”，紫薇得知后又惊又急，陷入两难境地。',
        'cast': [
            {'name': '林心如', 'role': '夏紫薇', 'avatar': 'https://b0.bdstatic.com/ugc/-uh4PU8AW7L8HT9AYEt2iAffdfae3676bc83fd2419d680f1b66e83.jpg'},
            {'name': '周杰', 'role': '福尔康', 'avatar': 'https://b0.bdstatic.com/ugc/-uh4PU8AW7L8HT9AYEt2iAffdfae3676bc83fd2419d680f1b66e83.jpg'}
        ]
    },{
        'url': 'https://media.w3.org/2010/05/sintel/trailer.mp4',
        'title': '还珠格格第一部-第3集',
        'intro': '小燕子入宫后闹出诸多笑话，乾隆虽觉她跳脱，却也十分喜爱。紫薇和金锁在尔康、尔泰的帮助下，终于有机会接近皇宫，寻找认父的契机。',
        'cast': [
            {'name': '林心如', 'role': '夏紫薇', 'avatar': 'https://b0.bdstatic.com/ugc/-uh4PU8AW7L8HT9AYEt2iAffdfae3676bc83fd2419d680f1b66e83.jpg'},
            {'name': '张铁林', 'role': '乾隆', 'avatar': 'https://b0.bdstatic.com/ugc/-uh4PU8AW7L8HT9AYEt2iAffdfae3676bc83fd2419d680f1b66e83.jpg'}
        ]
    }
]

# 初始化session_state（记录当前播放集数）
if 'ind' not in st.session_state:
    st.session_state['ind'] = 0

# ========== 动态标题（随视频切换） ==========
st.title(video_arr[st.session_state['ind']]['title'])

# ========== 播放视频 ==========
st.video(video_arr[st.session_state['ind']]['url'], autoplay=True)

# ========== 横向集数按钮 ==========
cols_btn = st.columns(len(video_arr))  # 根据集数创建等宽列
for i in range(len(video_arr)):
    with cols_btn[i]:
        st.button(
            f'第{i+1}集',
            use_container_width=True,
            on_click=lambda x=i: st.session_state.update({'ind': x})  # 简化切换逻辑
        )

# ========== 剧集介绍 + 演职人员图文（动态更新） ==========
st.divider()  # 分割线，优化排版
current_video = video_arr[st.session_state['ind']]

# 1. 剧集介绍
st.subheader('📝 剧集介绍')
st.write(current_video['intro'])

# 2. 演职人员图文展示（横向排列头像+信息）
st.subheader('🎭 演职人员')
cols_cast = st.columns(len(current_video['cast']))  # 按演员数量创建列
for idx, cast in enumerate(current_video['cast']):
    with cols_cast[idx]:
        # 显示演员头像（自适应宽度）
        st.image(cast['avatar'], width=120, caption=f"{cast['name']} · {cast['role']}")
        # 可补充更多信息（如简介）
        # st.write(f"饰演：{cast['role']}")

# 可选：调整整体样式，让页面更美观
st.markdown(
    """
    <style>
    .stButton>button {
        font-size: 16px;
        font-weight: bold;
    }
    .stImage {
        border-radius: 8px;  # 头像圆角
    }
    </style>
    """,
    unsafe_allow_html=True
)

