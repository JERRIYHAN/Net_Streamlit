import streamlit as st

#构建主页

#构建导航栏
pages = {
    "首页":[
        st.Page("pages/main_page.py", title="@JERRIYHAN")
    ],
    "个人简介": [
        st.Page("pages/Pprofile.py", title="我是谁？")
    ]
}

pg = st.navigation(pages)
pg.run()
