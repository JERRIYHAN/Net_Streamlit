import streamlit as st

a='''# 判断
## ? : 运算符(三元运算符)
条件运算符 ? :，可以用来替代 if...else 语句。它的一般形式如下：
```c
Exp1 ? Exp2 : Exp3;
```
![](https://www.runoob.com/wp-content/uploads/2014/09/Conditional-Statement-in-C-Programming-Lanuage-Ternary-Operator.png )

## switch 语句
switch与if的用法类似，但区别在于switch可以一一执行满足多条件时的多种case，多用于调试；而if一旦满足某一个条件，就跳出if了。

switch的一般用法：
```c
switch(A)
{
    case 常量表达式1:语句1;
    case 常量表达式2:语句2;
    ...
    default:语句n+1;
}
```
⚠️ 需要注意的是，A是整数类型（char、short、int或枚举），或者是能够隐式转换为整数类型的表达式。A将与常量表达式一一比较，相等时执行。
💡 defalut是可选的，适用于没有case符合条件时的执行'''

st.markdown(a)