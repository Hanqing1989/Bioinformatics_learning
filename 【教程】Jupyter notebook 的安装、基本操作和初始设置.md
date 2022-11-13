# 【教程】Jupyter notebook 的安装、基本操作和初始设置

#jupyter #R #python #biopython 

# Table of Contents

1. [安装 Jupyter notebook](#安装-jupyter-notebook)
2. [运行 Jupyter notebook](#运行-jupyter-notebook)
3. [蓝绿两模式：命令模式、编辑模式](#蓝绿两模式命令模式编辑模式)
4. [两种单元格：代码单元格和 Markdown 单元格](#两种单元格代码单元格和-markdown-单元格)
5. [最常用快捷键（必会）](#最常用快捷键必会)
6. [所有快捷键](#所有快捷键)
7. [设置 Jupyter Notebook 文件存放位置](#设置-jupyter-notebook-文件存放位置)
	1. [创建文件夹/目录](#创建文件夹目录)
	2. [配置文件路径](#配置文件路径)
	3. [修改配置文件](#修改配置文件)
8. [拓展功能](#拓展功能)
	1. [关联 Jupyter Notebook 和 conda 的环境和包——“nb_conda”](#关联-jupyter-notebook-和-conda-的环境和包nb_conda)
	2. [Markdown 生成目录](#markdown-生成目录)
9. [关闭和退出](#关闭和退出)
	1. [关闭笔记本和终端](#关闭笔记本和终端)
	2. [退出 Jupyter Notebook 程序](#退出-jupyter-notebook-程序)
10. [References](#references)

- Jupyter notebook 集编程和写作于一身，这就叫做“文学编程”。
 
- Jupyter notebook 不止可以运行 python，还可以运行 julia、R、Javascript 等语言，这也是 `jupyter` 这个名字的由来。[Jupyter notebook支持的编程语言](https://github.com/jupyter/jupyter/wiki/Jupyter-kernels)  

## 安装 Jupyter notebook

- 如果你安装了 python 数据科学全家桶 Anaconda，那么其中自带了 Jupyter notebook。

- 如果你没安装 Anaconda，可以直接在命令行里运行这行命令

```shell
pip install jupyter -i https://pypi.tuna.tsinghua.edu.cn/simple
```

## 运行 Jupyter notebook

- 在 Terminal 中输入命令：`jupter notebook`，回车。稍等片刻即可跳出浏览器网页。

![jupyter notebook打开界面](https://upload-images.jianshu.io/upload_images/13714448-803f32720cf0278e.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

- 点击右边的 New-Python3 即可创建 python 文档。
- 点击 New-Folder 可以创建新文件夹。
- 点击 New-Text File 可以创建空的 `.txt` 文件。
- 点击 New-Terminal 可以打开操作系统命令行，你可以使用操作系统对应的命令行进行目录切换、解压文件等操作。
- 勾选文件夹，点击 rename 即可重命名。

## 蓝绿两模式：命令模式、编辑模式

Jupyter notebook 中，代码和文档都存在于一个个单元格中，每个单元格都有蓝色和绿色两种状态。

- 命令模式（蓝色）：用于执行键盘输入的快捷命令（新增单元格、剪切、复制等等）。通过 `Esc` 键从绿色的编辑模式切换到蓝色的命令模式，此时单元左侧显示蓝色竖线。

- 编辑模式（绿色）：编辑文本和代码。选中单元并按 `Enter` 键进入编辑模式，此时单元左侧显示绿色竖线。

## 两种单元格：代码单元格和 Markdown 单元格

- Jupyter notebook 中，有两种单元格：代码单元格和 Markdown 单元格。

- 代码单元格：这里是你编写代码的地方，通过按 `Shift + Enter` 运行代码，其结果显示在本单元下方。代码单元左边有 `In [1]:` 这样的序列标记，方便人们查看代码的执行次序。在蓝色命令模式下，按 `y` 键可以将 Markdown 单元格转换为代码单元格。
- Markdown 单元格：在这里对文本进行编辑，采用 markdown 的语法规范，可以设置文本格式、插入链接、图片甚至数学公式。同样使用 `Shift + Enter` 运行 markdown 单元来显示渲染后的文本。在蓝色命令模式下按 `m` 键可以将代码单元格转换为 Markdown 单元格。

## 最常用快捷键（必会）

h 查看所有快捷键

Enter 从命令模式进入编辑模式

Esc 从编辑模式退回到命令模式

m 将代码单元格转换为 Markdown 单元格

y 将 Markdown 单元格转换为代码单元格

shift+Enter 运行本单元格，选择下面的代码块

ctrl+Enter 运行本单元格

alt+Enter 运行本单元格，在下方新建一个单元格

a 在上方新建一个单元格（above）

b 在下方新建一个单元格（below）

d 删除选中的单元格（delete）

x 剪切本单元格

c 复制本单元格

shift v 粘贴到上面

v 粘贴到下面

l 显示代码行号

## 所有快捷键

h 查看所有快捷键

![命令模式快捷键](https://upload-images.jianshu.io/upload_images/13714448-b9df2500cb80d59c.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

![编辑模式快捷键](https://upload-images.jianshu.io/upload_images/13714448-62d750fe7af8823e.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

## 设置 Jupyter Notebook 文件存放位置

- 如果你不想把今后在 Jupyter Notebook 中编写的所有文档都直接保存在家目录下，那你需要修改 Jupyter Notebook 的文件存放路径。

### 创建文件夹/目录

- Windows 用户在想要存放 Jupyter Notebook 文件的**磁盘**中**新建文件夹**并为该文件夹命名；双击进入该文件夹，然后复制地址栏中的路径。
- Linux/macOS 用户在想要存放 Jupyter Notebook 文件的位置**创建目录**并为目录命名，假如目录名为 Documents 文件夹下的 jupyter 文件夹（路径为/Users/user_name/Documents/jupyter），则在 Terminal 输入命令为：`mkdir Documents/jupyter`；进入目录，命令为：`cd Documents/jupyter`；查看目录的路径，命令为：`pwd`；复制该路径（/Users/user_name/Documents/jupyter）。
- “user_name”为你的用户名。

### 配置文件路径

- 在 Terminal 输入一个便捷获取配置文件所在路径的命令：`jupyter notebook --generate-config`。
	- 注意： 这条命令虽然可以用于查看配置文件所在的路径，但主要用途是是否将这个路径下的配置文件**替换**为**默认配置文件**。如果你是第一次查询，那么**或许**不会出现下图的提示；若文件已经存在或被修改，使用这个命令之后会出现询问“Overwrite /Users/raxxie/. jupyter/jupyter_notebook_config. py with default config? [y/N]”，即“用默认配置文件覆盖此路径下的文件吗？”，如果按“y”，则完成覆盖，那么之前所做的修改都将失效；如果只是为了查询路径，那么一定要输入“N”。

- 常规的情况下，Windows 和 Linux/macOS 的配置文件所在路径和配置文件名如下所述：
	- Windows 系统的配置文件路径：`C:\Users\user_name\.jupyter\`。
	- Linux/macOS 系统的配置文件路径：`/Users/user_name/.jupyter/` 或 `~/.jupyter/`。
	- 配置文件名：`jupyter_notebook_config.py`。
	-  “user_name”为你的用户名。

### 修改配置文件

- Windows 系统的用户可以使用文档编辑工具或 IDE 打开“jupyter_notebook_config. py”文件并进行编辑。常用的文档编辑工具和 IDE 有记事本、Notepad++、vim、Sublime  Text、PyCharm 等。其中，vim 是没有图形界面的，是一款学习曲线较为陡峭的编辑器，其他工具在此不做使用说明，因为上手相对简单。通过 vim 修改配置文件的方法请继续往下阅读。
- Linux/macOS 系统的用户建议直接通过终端调用 vim 来对配置文件进行修改。具体操作步骤如下：
	- 在 Terminal 输入命令：`vim ~/.jupyter/jupyter_notebook_config.py`。
	- 进入配置文件后不要按其他键，用**英文半角**直接输入 `/c.NotebookApp.notebook_dir`，按回车，光标从底部切换到文档正文中被查找关键词的首字母。
	- 按**小写 i**进入编辑模式，底部出现“--INSERT--”说明成功进入编辑模式。使用方向键把光标定位在第二个单引号上（光标定位在哪个字符，就在这个字符前开始输入），把“创建文件夹/目录”步骤中复制的路径粘贴在此处。
	- **把该行行首的井号（#）删除**。因为配置文件是 Python 的可执行文件，在 Python 中，井号（#）表示注释，即在编译过程中不会执行该行命令，所以为了使修改生效，需要删除井号（#）。
	- 先按 `esc` 键，从编辑模式退出，回到命令模式。再用**英文半角**直接输入 `:wq`，回车即成功保存且退出了配置文件。
	- 在终端中输入命令 `jupyter notebook` 打开 Jupyter Notebook，此时你会看到一个清爽的界面。

## 拓展功能

### 关联 Jupyter Notebook 和 conda 的环境和包——“nb_conda”

- 在 Terminal 输入命令：`conda install nb_conda`，执行上述命令能够将你 conda 创建的环境与 Jupyter Notebook 相关联，便于你在 Jupyter Notebook 的使用中，在不同的环境下创建笔记本进行工作。
- 可以在 Conda 扩展项下对 conda 环境和包进行一系列操作。
- 可以在笔记本内的“Kernel”类目里的“Change  kernel”切换内核。
- 在 Terminal 输入命令：`canda remove nb_conda`，卸载nb_conda包。

### Markdown 生成目录

- 通过安装扩展来实现目录的添加，在 Terminal 输入命令：`conda install -c conda-forge jupyter_contrib_nbextensions`。
- 启动 Jupyter Notebook，出现“Nbextensions”扩展项，点击“Nbextensions”，勾选“Table  of Contents ⑵”。
- 在 Jupyter Notebook 中使用 Markdown，点击目录的图标即可使用。

## 关闭和退出

### 关闭笔记本和终端

- 进入“Running”页面。
- 第一栏是“Terminals”，即所有正在运行的终端均会在此显示；第二栏是“Notebooks”，即所有正在运行的“ipynb”笔记本均会在此显示。
- 点击想要关闭的终端或笔记本后黄色“Shutdown”按钮。
- 成功关闭终端或笔记本。
- 注意：此方法可以关闭任何正在运行的终端和笔记本。

### 退出 Jupyter Notebook 程序

- 想要彻底退出 Jupyter Notebook，需要关闭它的服务器。只需要在它启动的终端上输入：
	- Mac 用户：control c
	- Windows 用户：ctrl c
- 然后在终端上会提示：“Shutdown this notebook server (y/[n])?”输入 y 即可关闭服务器，这才是彻底退出了 Jupyter Notebook 程序。

## References

1. [zihaopython/Jupyter notebook快速上手.md at master · TommyZihao/zihaopython · GitHub](https://github.com/TommyZihao/zihaopython/blob/master/%E6%95%B0%E6%8D%AE%E5%88%86%E6%9E%90%E4%B8%8E%E5%8F%AF%E8%A7%86%E5%8C%96%E5%AE%9E%E6%88%98%E6%A1%88%E4%BE%8B%EF%BC%9A%E5%AD%A6%E4%B9%A0%E6%97%B6%E9%97%B4%E4%B8%8E%E6%88%90%E7%BB%A9%E7%9A%84%E5%85%B3%E7%B3%BB%EF%BC%88%E7%BA%BF%E6%80%A7%E5%9B%9E%E5%BD%92%EF%BC%89/Jupyter%20notebook%E5%BF%AB%E9%80%9F%E4%B8%8A%E6%89%8B.md)
2. [Jupyter Notebook介绍、安装及使用教程 - 知乎](https://zhuanlan.zhihu.com/p/33105153)