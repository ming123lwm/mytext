import streamlit as st
from streamlit.components.v1 import html

# 页面配置：设置标题、布局
st.set_page_config(
    page_title="个人简历生成器",
    layout="wide",  # 宽布局适配左右分栏
    initial_sidebar_state="collapsed"  # 隐藏侧边栏
)

# 自定义CSS：美化表单和预览区域
st.markdown("""
    <style>
    /* 全局样式重置 */
    .stApp {
        background-color: white;
    }
    /* 表单区域样式 */
    .form-container {
        background-color: #2c2c2c;
        padding: 20px;
        border-radius: 8px;
        color: #fff;
        height: 100%;
    }
    /* 预览区域样式 */
    .preview-container {
        background-color: #1e1e1e;
        padding: 20px;
        border-radius: 8px;
        color: #fff;
        height: 100%;
    }
    /* 预览标题样式 */
    .preview-title {
        border-bottom: 2px solid #007bff;
        padding-bottom: 8px;
        margin-bottom: 15px;
        font-size: 24px;
        font-weight: 600;
    }
    /* 技能进度条 */
    .skill-bar {
        background-color: #333;
        height: 8px;
        border-radius: 4px;
        margin: 5px 0 15px 0;
    }
    .skill-fill {
        background-color: #dc3545;
        height: 100%;
        border-radius: 4px;
    }
    /* 修复Streamlit默认组件样式冲突 */
    .form-container .stTextInput>div>div>input {
        background-color: #444;
        color: #fff;
        border: 1px solid #666;
    }
    .form-container .stTextArea>div>div>textarea {
        background-color: #444;
        color: #fff;
        border: 1px solid #666;
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
    gender = st.radio("性别",["男", "女", "其他"],horizontal=True,label_visibility='hidden')
    age = st.number_input("年龄", min_value=18, max_value=60, value=24)
    job = st.text_input("工作岗位", "")
    phone = st.text_input("联系电话", "")
    email = st.text_input("电子邮箱", "")
    address = st.text_input("地址", "")
    birth_date = st.date_input("出生日期", value=None)  # 留空则不显示
    academic = st.selectbox("学历", ["大专", "本科", "硕士", "博士"], index=0)
    language = st.multiselect("语言能力（可多选）", ["中文", "英语", "日语","阿拉伯语","韩语","德语","法语"], default=["中文", "英语"])
    skills = st.multiselect("技能（可多选）", ["java", "HTML/C++", "Python","机器学习","jsp"], default=["java"])
    
    # 工作经验
    st.subheader("工作经验/年")
    experience = st.slider("工作经验", 0, 30, 0)
    
    #理想薪资
    my_range = range(0, 30000)
    highest_salary, minimun_salary = st.select_slider(
    '选择理想的薪资范围',
    options=my_range,
    value=(3000,5000))

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
    
    # 用st.markdown实现带样式的预览标题（替代不支持参数的st.subheader）
    st.markdown('<div class="preview-title">简历实时预览</div>', unsafe_allow_html=True)

    # 顶部：姓名+头像+基础信息
    preview_col1, preview_col2 = st.columns([1, 2])
    with preview_col1:
        st.subheader(name)
        # 显示头像（默认用占位图）
        if avatar:
            st.image(avatar, width=120, caption="头像")
        else:
            # 用公共占位图
            st.image("https://via.placeholder.com/120x150?text=头像", width=120)
    
    with preview_col2:
        st.write(f"性别：{gender}")
        st.write(f"年龄：{age} 岁")
        st.write(f"学历：{academic}")
        st.write(f"工作经验：{experience}")
        st.write(f"理想薪资：{highest_salary} - {minimun_salary} 元")
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

    #技能
    st.subheader("专业技能")
    st.write(skills)

