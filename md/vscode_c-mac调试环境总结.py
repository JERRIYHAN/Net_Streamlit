import streamlit as st

a='''# vscode 调试——累死我了
==爆肝一天vscode你欠我的用什么还==

主要问题其实聚焦于内置终端和调试的问题，包括但不限于：
* 内置终端无法输入输出
  * 首先发现：“点击右上角小三角-调试文件” != “fn+ f5”进入的调试（两者不同），其区别在于前者在终端里右侧的显示是"clang/g++"之类的，而后者是“debug”有一个小虫图标。一般而言，使用debug小虫图标模式。
* 可执行文件错误
  * 有时发生于代码和可执行文件存储在子文件夹里的情况，此时在launch.json的program项里面修改路径即可。
  * 有时发生于仅有源代码，缺乏编译后的可执行文件的情况，此时可以在右上角小三角里选择（"Run Code"（不是“运行代码”！）），会编译生成一个二进制文件，这个文件就是可执行文件。
* 
## 一般流程参考（在新目录下配置环境）
---
如无其他要求，可简单将配置文件复制到新的作用目录下

---
如需自己配置，
1. 首先创建源文件，c/c++
2. 写完后，先跑run code 生成可执行文件
3. 按fn+f5，生成调试文件 tasks.json
4. 如有需要，可在调试界面生成 launch.json，并注意修改相关配置使其与tasks.json适应；
   1. "program": "${workspaceFolder}/code/${fileBasenameNoExtension}",与tasks中args里最后一行（-o后的）文件名一致，如有子文件夹，将子文件路径加入“program”，比如这里的/code
   2. "terminal": "integrated" 在vs集成内置里面跑，不用开mac默认终端
   3. 注意修改configuration配置的时候，在不同行之间要加==逗号==
5. shift+command+p 打开顶部运行，可搜索debug，configuration，clang(c/c++),g++(c/c++)之类的，其实还没太搞清楚hh

实在不行就在csdn浏览记录里面找一找，或者直接搜。
现将20240905实测能跑的launch.json tastks.json附下
* launch.json
```
{
    // 使用 IntelliSense 了解相关属性。 
    // 悬停以查看现有属性的描述。
    // 欲了解更多信息，请访问: https://go.microsoft.com/fwlink/?linkid=830387
    "version": "0.2.0",
    "configurations": [
        {
            "type": "lldb",
            "request": "launch",
            "name": "Debug",
            "terminal": "integrated",
            "program": "${workspaceFolder}/code/${fileBasenameNoExtension}",
            "args": [],
            "cwd": "${workspaceFolder}",
            "stopOnEntry": true
        }
    ]
}
```

* tasks.json
```
{
    "tasks": [
        {
            "type": "cppbuild",
            "label": "C/C++: clang 生成活动文件",
            "command": "/usr/bin/clang",
            "args": [
                "-fcolor-diagnostics",
                "-fansi-escape-codes",
                "-g",
                "${file}",
                "-o",
                "${fileDirname}/${fileBasenameNoExtension}"
            ],
            "options": {
                "cwd": "${fileDirname}"
            },
            "problemMatcher": [
                "$gcc"
            ],
            "group": {
                "kind": "build",
                "isDefault": true
            },
            "detail": "调试器生成的任务。"
        }
    ],
    "version": "2.0.0"
}
```
'''
st.markdown(a)