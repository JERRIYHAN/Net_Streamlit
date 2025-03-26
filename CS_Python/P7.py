import streamlit as st
st.write("# P7 面向对象程序设计")

st.write("## 7-1")
st.code('''
class Building:
    def __init__(self,l,w,h,a):
        self.l=l
        self.w=w
        self.h=h
        self.a=a
    def square(self):
        return self.l*self.w*self.h
    def m(self):
        return self.square()*self.a
p=Building(2,2,3,5)
print(p.square())
print(p.m())

''')

st.write("## 7-2")
st.code('''
class identifier:
    def __init__(self,i):
        self.i=i
    def getyear(self):
        return str(self.i)[6:14]
    def Disp(self):
        print(self.i)
p=identifier(500103456789034502)
print(p.getyear())
p.Disp()

''')

st.write("## 7-3")
st.code('''
class Rect:
    def __init__(self,l,w):
        self.l=l
        self.w=w
    def zhou(self):
        return 2*(self.l+self.w)
    def s(self):
        return self.l*self.w
    def Sum(self,r):
        return self.s()+r.s()
r1=Rect(2,3)
r2=Rect(4,5)
print(r1.zhou())
print(r2.s())
print(r1.Sum(r2))

''')

st.write("## 7-4")
st.code('''
class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def Disp(self):
        print(self.name)
        print(self.age)
class Teacher(Person):
    def __init__(self,name,age,no,ta):
        Person.__init__(self,name,age)
        self.no=no
        self.ta=ta
    def NewDisp(self):
        Person.Disp(self)
        print(self.no)
        print(self.ta)
p=Teacher("w",3,4,5)
p.NewDisp()

''')
