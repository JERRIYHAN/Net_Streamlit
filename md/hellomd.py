import streamlit as st


st.balloons()
a='''# 这是一个markdown文件标题
## 这是一个二级标题（记得加空格！！）

> 这是一个引用

有序列表————把大象放进冰箱：
1. 打开冰箱（记得加空格！！）
2. 把大象放进去
3. 关上冰箱

无序列表————短横线
- 乌鸦坐飞机（记得加空格！！）
- 老鹰展翅
* 龙卷风摧毁停车场
* * 龙卷风摧毁停车场
* * * 龙卷风摧毁停车场
- 老鹰展翅

明天要做的事：
- [ ] 吃饭（记得处处加空格！！）
- [ ] 睡觉
- [x] 睡觉

代码块(使用反引号，在键盘上“1”的左边，有始有终)：
``` c
int main{
    return 0;
}
```

行内`printf();`

数学公式(使用latex)：
$$
\frac{/\partial f}{\partial ×} = 2\sqrt{a}x
$$

行内$\theta=x^2$

xiabiao H~2~O
x^2^

表格（注意第二行的对齐方式,冒号）：
|A|B|C|
|:--|:---:|--:|
|xiaoming|xiaowang|xiaoda|

题注：
莫愁前路无知己，天下谁人不识君^[李白]

---
横线
---

---
横线

---

[google](https://www.google.com "悬浮时显示")

[baidu][id]
[百度][id]
引用链接适用于多处使用同一个元素的时候，通过id赋值传参

[id]:https://baidu.com"引用链接"

链接也可以索引到文档内的某个位置
[回到标题](#这是一个markdown文件标题)

URL:
https://google.com

*斜体*
**加粗**


<u>xiahuaxian</u> :smile: :grin: 😅
==高亮==
----

<iframe src="//player.bilibili.com/player.html?isOutside=true&aid=327623069&bvid=BV1JA411h7Gw&cid=171385214&p=1" scrolling="no" border="0" frameborder="no" framespacing="0" allowfullscreen="true"></iframe>'''

st.markdown(a)
