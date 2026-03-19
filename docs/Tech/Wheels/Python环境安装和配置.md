---
tags:
  - Python
  - Wheel
---
# Python环境安装和配置

+ Python本体安装
+ pip配置
+ 安装Pycharm
+ VSC的Python环境配置
+ Anaconda安装与配置

##  本体安装

直接去[官方网站](https://www.python.org/downloads/)下载，如果速度偏慢可以使用国内镜像

测试安装成功方法：`win`+`R` type `cmd` 进入shell type `python` 若是返回版本则说明安装成功

## pip配置

换为国内镜像源(可以永久，在需要使用官方时再临时换源)

```Bash
pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple
```

检测换源成功与否

```Bash
pip config list
```

应该会返回

```
global.index-url='https://pypi.tuna.tsinghua.edu.cn/simple'
```

## Vscode

我比较倾向于在Vscode中使用Python，只需要在扩展栏中输入Python然后选择安装数量最大的那个(起码现在是)扩展，即可使用

## 安装Pycharm

>我高中比较喜欢的IDE，但是后面因为VSCODE的强大而弃用，但是时常有人问我怎么装干脆也写一下

直接去官网下载[免费的](https://www.jetbrains.com/pycharm/download/?section=windows)，后续的步骤只是阅读英文

>即使你完全不懂电脑也尽量不要使用金币找人帮忙下载这种免费软件，请你上网(贴吧、小红书、知乎、CSDN、博客园)寻找解决方案或者求助，安装从来不是很复杂的事情！

## 安装Anaconda

>可以参考博客园的这一[教程](https://www.cnblogs.com/ajianbeyourself/p/17654155.html)

### 基本的安装和注意事项

先安装Anaconda或者Miniconda：[官网链接](https://www.anaconda.com/download) 速度较慢可以使用[清华源](https://mirrors.tuna.tsinghua.edu.cn/anaconda/archive/)

下载前可以先按时间排序选择最新的版本，不要下载一些很古老的版本

下载安装过程中可以勾选一下Recommend的选项(能看懂意思当然自己定义最好)

检验方式是在`Anaconda Powershell`中 type `conda --version`

因为新版Anaconda不建议你直接将Anaconda添加入PATH变量(出于自我保护的目的)，因此如果你想要添加到PATH可能需要自己设置

在PATH中加入以下三条即可：

```
#文件路径取决于你的Anaconda安装在哪
D:\Anaconda
D:\Anaconda\Scripts
D:\Anaconda\Library\bin
```

!!! info "验证效果"
    如果添加到PATH你可以直接在cmd或是终端中使用conda --version以及conda相关的命令，如果不添加你可以在Anaconda Powershell中使用，官方应该是不建议直接添加到PATH的，为了隔离环境和安全性的考虑笔者也不建议这么做，但是如果是新手可以考虑直接添加，日后删除即可。

### 相关的基本命令

```
#换源
#添加源
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/free/
conda config --set show_channel_urls yes
#检验
conda config --show

#添加虚拟环境路径
conda config --add envs_dirs *newdir*
#注意除了查看.condarc文件中的envs_dirs参数外还需要对新的envs文件夹的权限进行设置
#需要修改对象为All Users以及完全控制和写入权限

#创建虚拟环境
conda create -n *name* python=3.10
#删除虚拟环境
conda remove -n *name* --all
#切换环境
conda activate *name*
#列出当前环境所有的包
conda list
#列出所有环境
conda env list
#安装Jupyter Notebook
#可以直接使用Anaconda Navigator
#或者使用命令行
conda install ipykernel
#注意：安装之后还需要进行注册内核
python -m ipykernel install --user --name my_data_env --display-name "My Data Analysis Environment"
#这么操作之后你才可以进行Select Kernel
```

