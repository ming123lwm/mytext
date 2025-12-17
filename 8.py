import streamlit as st
import pandas as pd
import numpy as np
from streamlit.components.v1 import html

# ====================== 全局配置（仅调用一次，必须在所有st命令前） ======================
st.set_page_config(
    page_title="广西职业师范学院",
    page_icon="🏫",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ====================== 全局黑色主题样式（统一控制） ======================
st.markdown("""
    <style>
    /* 全局基础样式 - 黑色主题核心 */
    .stApp {
        background-color: #000000;  /* 纯黑背景 */
        color: #ffffff;  /* 白色文字 */
        font-family: 'Microsoft YaHei', 'SimHei', sans-serif;
    }
    /* 所有标题统一白色 */
    h1, h2, h3, h4, h5, h6 {
        color: #ffffff !important;
        text-shadow: 0 0 8px #444444;
    }
    /* 普通文本白色 */
    .stText, p, span, div {
        color: #ffffff !important;
    }
    /* 按钮样式 - 黑色主题 */
    .stButton>button {
        background-color: #222222;
        color: #ffffff;
        border: 1px solid #444444;
        border-radius: 8px;
        font-size: 16px;
        font-weight: bold;
    }
    .stButton>button:hover {
        background-color: #333333;
        border-color: #555555;
    }
    /* 输入框/选择框样式 */
    .stTextInput>div>div>input,
    .stTextArea>div>div>textarea,
    .stSelectbox>div>div>select,
    .stMultiselect>div>div>select,
    .stNumberInput>div>div>input {
        background-color: #222222;
        color: #ffffff;
        border: 1px solid #444444;
        border-radius: 4px;
    }
    /* 滑块样式 */
    .stSlider>div>div>div>div {
        background-color: #333333;
    }
    .stSlider>div>div>div>div>div {
        background-color: #666666;
    }
    /* 进度条样式 */
    div[data-testid="stProgress"] > div > div {
        background: linear-gradient(90deg, #444444, #666666, #888888);
        border-radius: 10px;
        box-shadow: 0 0 8px #333333;
    }
    /* 分割线样式 */
    hr {
        border: none;
        height: 3px;
        background: linear-gradient(90deg, transparent, #444444, transparent);
        margin: 20px 0;
    }
    /* 表格样式 */
    .stDataFrame {
        background-color: #111111;
        border: 3px solid #333333;
        border-radius: 15px;
        overflow: hidden;
        box-shadow: 0 4px 10px rgba(0, 0, 0, 0.5);
    }
    table th {
        background-color: #222222 !important;
        color: #ffffff !important;
        font-weight: bold;
        font-size: 1.1rem;
    }
    table td {
        border: 1px solid #333333 !important;
        color: #ffffff !important;
        background: #111111 !important;
    }
    /* Metric指标卡片 */
    .stMetric {
        background-color: #111111;
        border: 3px solid #333333;
        border-radius: 20px;
        padding: 20px;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.5);
    }
    .stMetric label {
        color: #ffffff !important;
        font-size: 1.3rem;
        font-weight: bold;
    }
    .stMetric value {
        color: #dddddd !important;
        font-size: 2.2rem !important;
        font-weight: bold;
    }
    /* 代码块样式 */
    .stCode {
        background-color: #111111 !important;
        border: 3px solid #333333 !important;
        border-radius: 15px;
        box-shadow: 0 4px 10px rgba(0, 0, 0, 0.3);
        color: #ffffff !important;
    }
    /* 选项卡样式 */
    [data-testid="stTab"] {
        background-color: #111111;
        color: #ffffff !important;
        border: 1px solid #333333;
    }
    [data-testid="stTab"][aria-selected="true"] {
        background-color: #222222 !important;
        color: #ffffff !important;
        border-color: #444444;
    }
    [data-testid="stTabContent"] {
        background-color: #000000;
    }
    /* 图片圆角 + 黑色主题适配 */
    .stImage {
        border-radius: 8px;
        box-shadow: 0 4px 15px rgba(255,255,255,0.1);
    }
    /* 相册图片标题白色 */
    .stImage > div > caption {
        color: #ffffff !important;
        font-size: 18px;
        font-weight: 500;
    }
    </style>
""", unsafe_allow_html=True)

# ====================== 主标题（替换为图片并靠左） ======================
# 移除原文字标题，用HTML渲染指定图片并靠左
st.markdown("""
    <img src="https://www.gxvnu.edu.cn/images/QQtupian20240701090920_fuben.png" 
         style="float: left; max-width: 400px; margin-bottom: 20px; border-radius: 8px;" 
         alt="广西职业师范学院">
""", unsafe_allow_html=True)
# 清除浮动，避免影响下方布局
st.markdown("<div style='clear: both;'></div>", unsafe_allow_html=True)

# ====================== 创建6个选项卡 ======================
tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs([
    "数字档案", 
    "南宁美食数据", 
    "个人简历生成器", 
    "音乐播放器", 
    "视频播放器",
    "相册"
])

# ====================== 选项卡1：数字档案（无修改） ======================
with tab1:
    # 1. 主标题（Title）
    st.title("🎀 甜甜的学生档案 🍬")
    st.markdown("---")

    # 2. 基础信息（Header + Text + Markdown）
    st.header("📝 可爱小档案")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.text("✨ 学生昵称: 小甜豆")
        st.markdown("<span style='color:#dddddd;'>▸ 入学时间: 2022.09</span>", unsafe_allow_html=True)
    with col2:
        st.text("🎨 喜欢的颜色: 粉色")
        st.markdown("<span style='color:#dddddd;'>▸ 专属徽章: 软萌小码农</span>", unsafe_allow_html=True)
    with col3:
        st.text("🍡 小目标: 学会做可爱的可视化")
        st.markdown("<span style='color:#dddddd;'>▸ 心情状态: 超开心😜</span>", unsafe_allow_html=True)
    st.markdown("---")

    # 3. 技能矩阵（Metric + 进度条）
    st.header("💻 编程小技能")
    skill_col1, skill_col2, skill_col3 = st.columns(3)
    with skill_col1:
        st.metric("Python", "90%", "+4%")
    with skill_col2:
        st.metric("SQL", "85%", "+2%")
    with skill_col3:
        st.metric("Streamlit", "60%", "+8%")

    st.text("🎈 学习进度条")
    st.progress(82)  # 模拟进度条
    st.markdown("---")

    # 4. 任务日志（Table）
    st.header("📅 甜甜的任务日志")
    task_data = {
        "📆 日期": ["2025.12.11", "2025.12.11", "2025.12.11"],
        "🎯 任务": ["制作可爱档案页", "写甜甜的代码", "做粉色可视化"],
        "🌸 状态": ["✅ 完成啦", "⚪ 努力中", "❣️ 待解锁"],
        "💖 难度": ["★★☆☆☆", "★★★☆☆", "★★☆☆☆"]
    }
    task_df = pd.DataFrame(task_data)
    st.dataframe(task_df, use_container_width=True)  # 表格
    st.markdown("---")

    # 5. 最新代码成果（Code）
    st.header("💌 可爱代码小片段")
    code_content = """
    # 制作粉色爱心进度条
    def cute_progress(rate):
        heart = "❤️" * int(rate * 10)
        empty = "♡" * (10 - int(rate * 10))
        print(f"进度: {heart}{empty} {rate*100}%")

    # 调用示例
    cute_progress(0.8)  # 进度: ❤️❤️❤️❤️❤️❤️❤️❤️♡♡ 80%
    """
    st.code(code_content, language="python")  # 代码块

    # 6. 小日记（Markdown + Text）
    st.markdown("### 📜 甜甜的小日记")
    st.text("▸ 今天学会了做粉色的界面，超开心～")
    st.text("▸ 代码写累了就吃一颗草莓糖🍓")
    st.text("▸ 下次要做更可爱的可视化！")
    st.markdown("<span style='color:#dddddd;'>✨ 今日小幸运: 代码一次运行成功～</span>", unsafe_allow_html=True)

# ====================== 选项卡2：南宁美食数据（无修改） ======================
with tab2:
    # ---------------------- 标题与介绍 ----------------------
    st.title("🍔 南宁美食探索")
    st.markdown("探索广西南宁最受欢迎的美食地点！选择你感兴趣的餐厅类型，查看评分和位置。")

    # ---------------------- 1. 南宁美食地图（map组件） ----------------------
    st.subheader("📍 南宁美食地图")
    # 构造5家餐厅的经纬度数据（南宁区域）
    map_data = pd.DataFrame({
        "latitude": [22.823555, 22.812116, 22.813655, 22.814418, 22.805077],  # 南宁纬度范围
        "longitude": [108.342463, 108.392014, 108.423043, 108.390838, 108.368414],  # 南宁经度范围
        "餐厅名称": ["桂林肥仔·中华餐饮名店（星光大道店）", "桂小厨广西菜（万象城店）", "横州鱼生馆（爱琴海店）", "甘家界柠檬鸭（春晖店）", "啫啫村 生料啫啫煲（琅西店）"]
    })
    st.map(map_data, use_container_width=True)

    # ---------------------- 2. 餐厅评分（bar_chart组件） ----------------------
    st.subheader("⭐ 餐厅评分")
    # 5家餐厅的评分数据
    score_data = pd.DataFrame({
        "餐厅名称": ["桂林肥仔·中华餐饮名店（星光大道店）", "桂小厨广西菜（万象城店）", "横州鱼生馆（爱琴海店）", "甘家界柠檬鸭（春晖店）", "啫啫村 生料啫啫煲（琅西店）"],
        "评分": [4.0, 4.5, 4.2, 4.7, 4.3]
    }).set_index("餐厅名称")
    st.bar_chart(score_data, use_container_width=True)

    # ---------------------- 3. 不同类型餐厅价格（area_chart组件） ----------------------
    st.subheader("💰 不同餐厅人均消费价格")
    # 5类餐厅的人均消费数据
    price_data = pd.DataFrame({
        "餐厅类型": ["桂林肥仔·中华餐饮名店（星光大道店）", "桂小厨广西菜（万象城店）", "横州鱼生馆（爱琴海店）", "甘家界柠檬鸭（春晖店）", "啫啫村 生料啫啫煲（琅西店）"],
        "人均消费(元)": [65, 98, 75, 60, 42]
    }).set_index("餐厅类型")
    st.area_chart(price_data, use_container_width=True)

    # ---------------------- 4. 5家餐厅12个月价格走势（line_chart组件） ----------------------
    st.subheader("📈 5家餐厅12个月价格走势")
    # 构造12个月（1-12月）+5家餐厅的价格数据
    months = [f"{i}月" for i in range(1, 13)]
    price_trend_data = pd.DataFrame({
        "月份": months,
        "桂林肥仔·中华餐饮名店（星光大道店）": np.random.randint(48, 70, size=12),  # 价格小幅波动
        "桂小厨广西菜（万象城店）": np.random.randint(75, 103, size=12),
        "横州鱼生馆（爱琴海店）": np.random.randint(64, 95, size=12),
        "甘家界柠檬鸭（春晖店）": np.random.randint(49, 83, size=12),
        "啫啫村 生料啫啫煲（琅西店）": np.random.randint(38, 65, size=12)
    }).set_index("月份")
    st.line_chart(price_trend_data, use_container_width=True)

    # ---------------------- 5. 5家餐厅12个月月均人流量 ----------------------
    flow_data = pd.DataFrame({
        "月份": months,
        "桂林肥仔·中华餐饮名店（星光大道店）": np.random.randint(1800, 3500, size=12),
        "桂小厨广西菜（万象城店）": np.random.randint(1500, 3000, size=12),
        "横州鱼生馆（爱琴海店）": np.random.randint(800, 2000, size=12),
        "甘家界柠檬鸭（春晖店）": np.random.randint(2000, 4000, size=12),
        "啫啫村 生料啫啫煲（琅西店）": np.random.randint(2800, 4800, size=12)
    }).set_index("月份")
    st.subheader("👥 5家餐厅12个月月均人流量（人次）")
    st.area_chart(flow_data, use_container_width=True, color=["#666666", "#888888", "#999999", "#AAAAAA", "#BBBBBB"])

    # ---------------------- 6. 餐厅详情（下拉选择） ----------------------
    st.subheader("🏠 餐厅详情")
    selected_restaurant = st.selectbox("选择餐厅查看详情", map_data["餐厅名称"].tolist())

    # 模拟餐厅详情数据
    restaurant_detail = {
        "桂林肥仔·中华餐饮名店（星光大道店）": {
            "评分": "4.0/5.0",
            "人均消费": "65元",
            "推荐菜品": ["糖醋排骨", "啤酒鱼", "白切鸡"],
            "拥挤程度": "80% 拥挤"
        },
        "桂小厨广西菜（万象城店）": {
            "评分": "4.5/5.0",
            "人均消费": "98元",
            "推荐菜品": ["老友鱼", "脆皮小刀鸭", "巴马黑豆豆腐"],
            "拥挤程度": "60% 拥挤"
        },
        "横州鱼生馆（爱琴海店）": {
            "评分": "4.2/5.0",
            "人均消费": "75元",
            "推荐菜品": ["新鲜鱼生"],
            "拥挤程度": "70% 拥挤"
        },
        "甘家界柠檬鸭（春晖店）": {
            "评分": "4.7/5.0",
            "人均消费": "60元",
            "推荐菜品": ["柠檬鸭", "酸笋炒牛肉", "猪血炒饭"],
            "拥挤程度": "90% 拥挤"
        },
        "啫啫村 生料啫啫煲（琅西店）": {
            "评分": "4.3/5.0",
            "人均消费": "42元",
            "推荐菜品": ["猪杂啫啫煲", "黑椒牛肉啫啫煲", "鲜鱿啫啫煲"],
            "拥挤程度": "99% 拥挤"
        }
    }

    # 展示选中餐厅的详情
    detail = restaurant_detail[selected_restaurant]
    col1, col2 = st.columns(2)
    with col1:
        st.write(f"**{selected_restaurant}**")
        st.write(f"评分：{detail['评分']}")
        st.write(f"人均消费：{detail['人均消费']}")
        st.write(f"当前拥挤程度：{detail['拥挤程度']}")
    with col2:
        st.write("**推荐菜品**")
        for dish in detail["推荐菜品"]:
            st.write(f"- {dish}")

# ====================== 选项卡3：个人简历生成器（无修改） ======================
with tab3:
    # 自定义CSS：简历模块黑色主题（覆盖全局但保持统一）
    st.markdown("""
        <style>
        /* 表单区域样式 - 黑色主题 */
        .form-container {
            background-color: #111111;
            padding: 20px;
            border-radius: 8px;
            color: #ffffff;
            height: 100%;
            border: 1px solid #333333;
        }
        /* 预览区域样式 - 黑色主题 */
        .preview-container {
            background-color: #111111;
            padding: 20px;
            border-radius: 8px;
            color: #ffffff;
            height: 100%;
            border: 1px solid #333333;
        }
        /* 预览标题样式 */
        .preview-title {
            border-bottom: 2px solid #666666;
            padding-bottom: 8px;
            margin-bottom: 15px;
            font-size: 24px;
            font-weight: 600;
            color: #ffffff;
        }
        /* 技能进度条 */
        .skill-bar {
            background-color: #222222;
            height: 8px;
            border-radius: 4px;
            margin: 5px 0 15px 0;
        }
        .skill-fill {
            background-color: #666666;
            height: 100%;
            border-radius: 4px;
        }
        </style>
    """, unsafe_allow_html=True)

    # -------------- 左侧：信息表单区域 --------------
    col1, col2 = st.columns([1, 2])  # 左右分栏（表单:预览 = 1:2）

    with col1:
        st.markdown('<div class="form-container">', unsafe_allow_html=True)
        st.subheader("个人信息表单")

        # 基础信息
        name = st.text_input("姓名", "某某")
        gender = st.radio("性别", ["男", "女", "其他"], horizontal=True, label_visibility='hidden')
        age = st.number_input("年龄", min_value=18, max_value=60, value=24)
        job = st.text_input("工作岗位", "")
        phone = st.text_input("联系电话", "")
        email = st.text_input("电子邮箱", "")
        address = st.text_input("地址", "")
        birth_date = st.date_input("出生日期", value=None)  # 留空则不显示
        academic = st.selectbox("学历", ["大专", "本科", "硕士", "博士"], index=0)
        language = st.multiselect(
            "语言能力（可多选）", 
            ["中文", "英语", "日语", "阿拉伯语", "韩语", "德语", "法语"], 
            default=["中文", "英语"]
        )
        skills = st.multiselect(
            "技能（可多选）", 
            ["java", "HTML/C++", "Python", "机器学习", "jsp"], 
            default=["java"]
        )

        # 工作经验
        st.subheader("工作经验/年")
        experience = st.slider("工作经验", 0, 30, 0)

        # 理想薪资
        my_range = range(0, 30000)
        minimum_salary, highest_salary = st.select_slider(
            '选择理想的薪资范围',
            options=my_range,
            value=(3000, 5000)
        )

        # 个人简介
        st.subheader("个人简介")
        intro = st.text_area(
            "简介内容",
            value="本人是计算机专业的应届毕业生，主要研究方向为前端开发与全栈开发。现于XX互联网科技公司担任前端开发岗，在项目中负责前端页面的交互与性能优化。具备良好的团队协作能力与工程思维，对新技术保持学习热情，曾参与多个大型校园项目的开发与落地（如校园小程序、企业官网、个人博客等），熟练掌握前端工程化工具与跨端开发技术。",
            height=150
        )

        # 上传头像
        st.subheader("头像上传")
        avatar = st.file_uploader("上传头像（支持JPG/PNG）", type=["jpg", "png"])
        st.markdown('</div>', unsafe_allow_html=True)

    # -------------- 右侧：简历实时预览区域 --------------
    with col2:
        st.markdown('<div class="preview-container">', unsafe_allow_html=True)
        
        # 预览标题
        st.markdown('<div class="preview-title">简历实时预览</div>', unsafe_allow_html=True)

        # 顶部：姓名+头像+基础信息
        preview_col1, preview_col2 = st.columns([1, 2])
        with preview_col1:
            st.subheader(name)
            # 显示头像（默认用占位图）
            if avatar:
                st.image(avatar, width=120, caption="头像")
            else:
                # 黑色主题占位图
                st.image("https://via.placeholder.com/120x150/000000/ffffff?text=头像", width=120)
        
        with preview_col2:
            st.write(f"性别：{gender}")
            st.write(f"年龄：{age} 岁")
            st.write(f"学历：{academic}")
            st.write(f"工作经验：{experience} 年")
            st.write(f"理想薪资：{minimum_salary} - {highest_salary} 元")
            st.write(f"工作岗位：{job}")
            st.write(f"联系电话：{phone}")
            st.write(f"电子邮箱：{email}")
            if birth_date:
                st.write(f"出生日期：{birth_date.strftime('%Y-%m-%d')}")
            st.write(f"语言能力：{', '.join(language)}")
            st.write(f"地址：{address}")

        # 分隔线
        st.markdown("---")

        # 个人简介
        st.subheader("个人简介")
        st.write(intro)

        # 分隔线
        st.markdown("---")

        # 技能
        st.subheader("专业技能")
        st.write(skills)
        
        st.markdown('</div>', unsafe_allow_html=True)

# ====================== 选项卡4：音乐播放器（无修改） ======================
with tab4:
    st.title("🎵简易音乐播放器")

    # 初始化会话状态
    if 'song_ind' not in st.session_state:
        st.session_state['song_ind'] = 0

    # 歌曲列表（包含封面、标题、歌手、时长、音频链接）
    songs = [
        {
            "cover": "http://p2.music.126.net/lHrmzaGOd-PmrlmVxJfWyg==/109951172350451653.jpg?param=130y130",
            "title": "海屿你",
            "singer": "小奥奥",
            "duration": "4:56",
            "audio_url": "https://music.163.com/song/media/outer/url?id=3322383475.mp3"
        },
        {
            "cover": "http://p2.music.126.net/YiYv2SfEno67XeuEVwDhXQ==/109951169849771260.jpg?param=130y130",
            "title": "Sneaky Tactics",
            "singer": "Ilona Harpaz",
            "duration": "2:31",
            "audio_url": "https://music.163.com/song/media/outer/url?id=2614865529.mp3"
        },
        {
            "cover": "http://p2.music.126.net/EDhgL1S2DLGVE_5cjU-hfQ==/109951172410328709.jpg?param=130y130",
            "title": "大东北是我的家乡",
            "singer": "袁娅维TIA RAY",
            "duration": "3:46",
            "audio_url": "https://music.163.com/song/media/outer/url?id=3327141886.mp3"
        }
    ]

    # 获取当前歌曲信息
    current_song = songs[st.session_state['song_ind']]

    # 布局：封面+歌曲信息
    col_cover, col_info = st.columns([1, 2])
    with col_cover:
        st.image(current_song["cover"], caption="专辑封面", width=150)
    with col_info:
        st.subheader(current_song["title"])
        st.write(f"歌手: {current_song['singer']}")
        st.write(f"时长: {current_song['duration']}")

    # 核心：播放当前歌曲的音频
    st.subheader("🎧 播放音频")
    st.audio(current_song["audio_url"], format="audio/mp3", start_time=0)

    # 切换歌曲函数
    def next_song():
        st.session_state['song_ind'] = (st.session_state['song_ind'] + 1) % len(songs)

    def prev_song():
        st.session_state['song_ind'] = (st.session_state['song_ind'] - 1) % len(songs)

    # 切换按钮
    c1, c2 = st.columns([2, 2])
    with c1:
        st.button("|◀|上一首", on_click=prev_song, use_container_width=True)
    with c2:
        st.button("|▶|下一首", on_click=next_song, use_container_width=True)

# ====================== 选项卡5：视频播放器（无修改） ======================
with tab5:
    # 视频及配套信息数据
    video_arr = [
        {
            'url': 'https://www.w3schools.com/html/movie.mp4',
            'title': '还珠格格第一部-第1集',
            'intro': '本集讲述了紫薇带着丫鬟金锁从济南来到北京，欲认父乾隆，却阴差阳错与小燕子相识，小燕子仗义答应帮紫薇进宫送信的故事。',
            'cast': [
                {'name': '林心如', 'role': '夏紫薇', 'avatar': 'https://b0.bdstatic.com/ugc/-uh4PU8AW7L8HT9AYEt2iAffdfae3676bc83fd2419d680f1b66e83.jpg'},
                {'name': '苏有朋', 'role': '五阿哥永琪', 'avatar': 'https://q3.itc.cn/images01/20250527/49aaeaa71540434b982b45ad2b5ec4b1.jpeg'}
            ]
        },
        {
            'url': 'https://www.w3school.com.cn/example/html5/mov_bbb.mp4',
            'title': '还珠格格第一部-第2集',
            'intro': '小燕子误打误撞闯入围场，被乾隆误认为是自己失散多年的女儿，当场被封为“还珠格格”，紫薇得知后又惊又急，陷入两难境地。',
            'cast': [
                {'name': '林心如', 'role': '夏紫薇', 'avatar': 'https://b0.bdstatic.com/ugc/-uh4PU8AW7L8HT9AYEt2iAffdfae3676bc83fd2419d680f1b66e83.jpg'},
                {'name': '周杰', 'role': '福尔康', 'avatar': 'https://b0.bdstatic.com/ugc/-uh4PU8AW7L8HT9AYEt2iAffdfae3676bc83fd2419d680f1b66e83.jpg'}
            ]
        },
        {
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
                on_click=lambda x=i: st.session_state.update({'ind': x})
            )

    # ========== 剧集介绍 + 演职人员图文 ==========
    st.divider()  # 分割线，优化排版
    current_video = video_arr[st.session_state['ind']]

    # 1. 剧集介绍
    st.subheader('📝 剧集介绍')
    st.write(current_video['intro'])

    # 2. 演职人员图文展示
    st.subheader('🎭 演职人员')
    cols_cast = st.columns(len(current_video['cast']))
    for idx, cast in enumerate(current_video['cast']):
        with cols_cast[idx]:
            st.image(cast['avatar'], width=120, caption=f"{cast['name']} · {cast['role']}")

# ====================== 选项卡6：相册（修复所有错误） ======================
with tab6:
    st.title("我的相册")

    # 初始化会话状态（避免与视频播放器的ind冲突，改用photo_ind）
    if 'photo_ind' not in st.session_state:
        st.session_state['photo_ind'] = 0

    # 图片列表
    images = [
        {
            'url': "https://www.baltana.com/files/wallpapers-2/Cute-Cat-Images-07756.jpg",
            'text': '猫'
        },
        {
            'url': "https://cdn.britannica.com/82/232782-050-8062ACFA/Black-labrador-retriever-dog.jpg",
            'text': 'dog'
        },
        {
            'url': "https://live.staticflickr.com/2686/4497672316_d283310530_3k.jpg",
            'text': 'lion'
        }
    ]

    # 显示当前图片（适配黑色主题）
    st.image(
        images[st.session_state['photo_ind']]['url'],
        caption=images[st.session_state['photo_ind']]['text'],
        use_container_width=False,
        width=600  # 限制图片宽度
    )

    # 切换图片函数
    def lastImg():
        st.session_state['photo_ind'] = (st.session_state['photo_ind'] - 1) % len(images)

    def nextImg():
        st.session_state['photo_ind'] = (st.session_state['photo_ind'] + 1) % len(images)

    # 分列容器（修正变量名cl→col1）
    col1, col2 = st.columns(2)

    with col1:
        st.button("上一张", on_click=lastImg, use_container_width=True)

    with col2:
        st.button("下一张", on_click=nextImg, use_container_width=True)
