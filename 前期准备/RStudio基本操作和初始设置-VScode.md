# RStudio基本操作和初始设置

**Table of Contents**

- [1 连接 Rstudio 与 Github 进行版本控制](#1-连接-rstudio-与-github-进行版本控制)
- [2 工作界面介绍](#2-工作界面介绍)
- [3 初始设置](#3-初始设置)
  - [3.1 R markdown 安装](#31-r-markdown-安装)
  - [3.2 Options 设定](#32-options-设定)
- [4 Workflow](#4-workflow)
- [5 最常用快捷键（必会）](#5-最常用快捷键必会)
- [References](#references)



## 1 连接 Rstudio 与 Github 进行版本控制

- 如有需要，参考[连接Rstudio与Github](http://afarx.com/2018/02/26/Rstudio-Github/)。

## 2 工作界面介绍

![RStudio打开界面](https://bookdown.org/xiao/RAnalysisBook/RstudioDesk_mark.png)

- 脚本窗口（左上角：Source）：用于编辑脚本，如 R 脚本等（如果未出现该窗口，用快捷键 Ctrl+Shift+N 新建一个脚本）。
- 命令窗口（左下角：Console）：用于输入命令。
- 变量历史等窗口（右上角：Environment）：有4个标签页，Environment 为环境窗口，可以暂时简单理解为查看变量的窗口；History 为历史窗口，用于查看历史；其他标签页暂不介绍。
- 文件等窗口（右下角）：有5个标签页，Files 用于查看与管理文件；Plot 用于查看输出的绘图；Packages 用于管理和查看已安装“包”；Help用于查看帮助文档；Viewer 用于浏览某些输出，如网页。

## 3 初始设置

### 3.1 R markdown 安装

- 在命令窗口输入：
  - `install.packages("rmarkdown")` # 写rmarkdown必需的包。
  - `install.packages("knitr")` # 导出文件必需的包。
  - `install.packages("tinytex")` # TeX的轻量级发行版，用于PDF文件的导出。
  - `install.packages("rticles")` # 配合中文导出PDF，有很多不同的文档模板可供使用。

### 3.2 Options 设定

- Code -> Saving：Default text encoding：UTF-8。
- Appearance：可以修改 RStudio 的主题、字体、编辑器的主题等。
- Pane Layout：可以设置 RStudio 的窗口布局，以及选择各个窗口内所显示的内容。
- Packages -> Management：“Primary CRAN repository” 选择国内的安装源。
- Python：根据 Python 的环境路径选择 Python 解释器的路径。
- Sweave：“PDF Generation”，在Weave Rnw files using 选择 knitr，在 Typeset LaTeX into PDF using 选择 XeLaTex；“LaTeX Editing and Compilation”，全部勾选。

## 4 Workflow

在 RStudio 中写代码有3中选择：写在命令窗口中，写在R脚本中，写在Rmarkdown文档中。对初学者而言，使用Rmarkdown文档是比较合适的。

1. 新建一个 Project 来管理所有文档。
2. 新建一个 R Markdown 文档。选择“From Template”，
3. 将代码嵌入块中。一次按行、按块或全部运行代码。
4. 编写文本并添加表格、图形、图像和引文。使用 Markdown 语法或 RStudio Visual Markdown 编辑器格式化。
5. 在 YAML 头中设置输出格式和选项。自定义主题或添加参数以执行或添加与 Shiny 的交互。
6. 在 Knit 可选择不同的文件类型进行浏览，在写作时预览作品，同时将对应格式保存至工作目录下。
7. 使用 PDF 格式并输出中文时，请点击 Knit 旁的小齿轮，并修改字体引擎为 xelatex。

## 5 最常用快捷键（必会）

1. 注释/取消注释当前行（代码块）： Ctrl+Shift+C；
2. 插入代码块：Ctrl+Alt+I；
3. 运行光标所在行的代码：Ctrl+Enter；
4. 运行当前光标所在行的代码块：Ctrl+Shift+Enter。

## References

1. [连接Rstudio与Github](http://afarx.com/2018/02/26/Rstudio-Github/)
2. [R 数据分析指南与速查手册](https://bookdown.org/xiao/RAnalysisBook/)
3. [R与tidyverse——数据分析入门](https://tshi.page/r-and-tidyverse-book/index.html)
4. [R markdown 入门安装教程](https://www.jianshu.com/p/4fa7c107fe9c)
5. [Rmarkdown与Rnotebook使用心得](https://blog.csdn.net/qq_41437512/article/details/107094265)