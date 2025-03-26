import streamlit as st
a='''# 循环
```c
//while：可能一次不执行
while(condition)
{
   statement(s);
}
```

```c
//for：可用(init;;increment)省略的方式构建无限循环
for ( init; condition; increment )
{
   statement(s);
}
```
```c
//do_while:与while的区别就在于会至少执行一次，再检查条件
do
{
   statement(s);

}while( condition );
```
|控制语句|描述|
|:-:|:-:|
|break 语句|终止循环或 switch 语句，程序流将继续执行紧接着循环或 switch 的下一条语句。|
|continue 语句|告诉一个循环体立刻停止本次循环迭代，重新开始下次循环迭代。|
|goto 语句|将控制转移到被标记的语句。但是不建议在程序中使用 goto 语句。|

## 遍历字符串
循环便利字符串时，可引入i并简写如下（省去strlen过程）'''

st.markdown(a)