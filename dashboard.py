import streamlit as st

#构建主页

#构建导航栏
pages = {
    "首页":[
        st.Page("pages/main_page.py", title="@JERRIYHAN")
    ],
    "个人简介": [
        st.Page("pages/Pprofile.py", title="我是谁？"),
    ],
    "C语言学习": [
        st.Page("md/hellomd.py", title="hellomd"),
        st.Page("md/# 原码、反码、补码.py", title="原码、反码、补码"),
        st.Page("md/# 运算符.py", title="运算符"),
        st.Page("md/常变量说明.py", title="常变量说明"),
        st.Page("md/判断.py", title="判断"),
        st.Page("md/循环.py", title="循环"),
        st.Page("md/一些小tips.py", title="一些小tips"),
        st.Page("md/指针.py", title="指针"),
        st.Page("md/vscode_c-mac调试环境总结.py", title="vscode_c-mac调试环境总结"),
    ],
    "Python学习":[
        st.Page("CS_Python/P3.py", title="P3 结构化程序设计"),
        st.Page("CS_Python/P4.py", title="P4 函数与递归"),
        st.Page("CS_Python/P5.py", title="P5 数据结构-列表元组字典"),
        st.Page("CS_Python/P6.py", title="P6 数据文件"),
        st.Page("CS_Python/P7.py", title="P7 面向对象程序设计"),
        st.Page("CS_Python/P8.py", title="P8 数据可视化"),

    ],
    "AI学习":[
        st.Page("AI_files/NN_demo.py", title="NN 框架"),
        st.Page("AI_files/CNN_MNIST.py", title="CNN 框架"),
    ]
}

pg = st.navigation(pages)
pg.run()
