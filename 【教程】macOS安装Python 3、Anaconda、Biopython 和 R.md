# 【教程】macOS安装Python 3、Anaconda、Biopython 和 R

#Anaconda #python #biopython #教程

# Table of Contents

1. [macOS](#macos)
   1. [安装 Anaconda3](#安装-anaconda3)
   2. [安装 Python 3](#安装-python-3)
   3. [配置 Python3 环境 ：](#配置-python3-环境-)
   4. [安装 Biopython](#安装-biopython)
   5. [管理 Anaconda 环境](#管理-anaconda-环境)
      1. [创建新环境](#创建新环境)
      2. [切换环境](#切换环境)
      3. [退出环境至root](#退出环境至root)
      4. [显示已创建环境](#显示已创建环境)
      5. [复制环境](#复制环境)
      6. [删除环境](#删除环境)
   6. [管理包](#管理包)
      1. [模糊查找](#模糊查找)
      2. [获取当前环境中已安装的包信息](#获取当前环境中已安装的包信息)
      3. [安装包](#安装包)
         1. [在指定环境中安装包](#在指定环境中安装包)
         2. [在当前环境中安装包](#在当前环境中安装包)
         3. [从 Anaconda. org 安装包](#从-anaconda-org-安装包)
      4. [卸载包](#卸载包)
         1. [卸载指定环境中的包](#卸载指定环境中的包)
         2. [卸载当前环境中的包](#卸载当前环境中的包)
      5. [更新包](#更新包)
         1. [更新所有包](#更新所有包)
         2. [更新指定包](#更新指定包)
   7. [安装 R](#安装-r)
2. [References](#references)

## macOS

### 安装 Anaconda3

- 下载并安装最新的 pkg 安装包：[Anaconda下载页](https://repo.anaconda.com/archive/)。
- 等待“Installation”部分结束，在“Summary”部分若看到“The installation was completed successfully.”则安装成功，直接点击“Close”关闭对话框。
- 在 mac 的 Launchpad 中可以找到名为“Anaconda-Navigator”的图标，点击打开。若“Anaconda-Navigator”成功启动，则说明真正成功地安装了 Anaconda；如果未成功，请务必仔细检查以上安装步骤。
- 在 Terminal 中输入命令：`conda list`，如果 Anaconda 被成功安装，则会显示已经安装的包名和版本号。
- 提示：默认情况下，新创建的环境将会被保存在 ***/Users/<user_name>/anaconda3/env*** 目录下，其中， ***<user_name>*** 为当前用户的用户名。

### 安装 Python 3

- **如果要装Anaconda3，其中会自带python3，无需再额外手动安装python**。
- 在官网下载并安装最新的 pkg 安装包：[Python Releases for macOS | Python.org](https://www.python.org/downloads/macos/)。
- 在 Terminal 中输入命令：`python --version`，查看 python 版本号。
- 如果想要使用 python 命令，而非 python3 命令执行 python，那么可以设置环境变量来解决，在终端中执行如下代码：`echo 'alias python=python3'>> .bash_profile`。
- 推出并且重新打开 Terminal，输入 `python`，可看到 Python3。

###  配置 Python3 环境 ：

- 在 Terminal 中输入命令：`which python3`，查看该路径是否与 Anaconda 默认环境（base） 的路径相同，如不一致，继续下一步。
- 在 Terminal 中输入命令：`open ~/.bash_profile`，会弹出一个记事本，在最下方插入一行命令： `export PATH="/Users/user_name/opt/anaconda3/bin:${PATH}"`（user_name 为当前用户的用户名），关闭记事本。
- 在 Terminal 中输入命令：`source ~/.bash_profile`，保存修改，再输入 `which python3`，输出的结果就是对应的路径了。

### 安装 Biopython 

- 在 Terminal 中输入命令：`conda install -c conda-forge biopython`，直到安装完成。
- 在 Terminal 中输入命令：`conda update -c conda-forge biopython`，可更新版本。
- 其他安装方法参考：[Packages · Biopython](https://biopython.org/wiki/Packages)。

### 管理 Anaconda 环境

#### 创建新环境

- 在 Terminal 中输入命令：`python --version`，查看 python 版本号。
- 在 Terminal 中输入命令：`conda create --name <env_name> <package_names>`。
  - 注意：
  - ***<env_name>*** 即创建的环境名。建议以英文命名，且不加空格，名称两边不加尖括号“<>”。
  - ***<package_names>*** 即安装在环境中的包名。名称两边不加尖括号“<>”。
- 例如，在 Terminal 中输入命令： `  conda create --name env_R R=4.2 `，即创建一个名为“R”的环境，环境中安装版本为 4.2 的 R。
- 如果要在新创建的环境中创建多个包，则直接在 <package_names>后以**空格**隔开，添加多个包名即可。如： `conda create -n env_python_and_R python=3.9 biopython`，即创建一个名为“python_and_R”的环境，环境中安装版本为 3.9 的 python，同时也安装了 biopython。
- ***--name*** 同样可以替换为 ***-n*** 。

#### 切换环境

- 在 Terminal 中输入命令：`source activate <env_name>`，***<env_name>*** 即创建的环境名。建议以英文命名，且不加空格，名称两边不加尖括号“<>”。
  - 1. 如果创建环境后安装 Python 时没有指定 Python 的版本，那么将会安装与 Anaconda 版本相同的 Python 版本，即如果安装 Anaconda 第 2 版，则会自动安装 Python 2. x；如果安装 Anaconda 第 3 版，则会自动安装 Python 3. x。
  - 2. 当成功切换环境之后，在该行行首将以“(env_name)”开头。其中，“env_name”为切换到的环境名。如：在 macOS 系统中执行 ***source active python2*** ，即切换至名为“python2”的环境，则行首将会以 (python2) 开头。

#### 退出环境至root

- 在 Terminal 中输入命令：`source deactivate`。当执行退出当前环境，回到 root 环境命令后，原本行首以“(env_name)”开头的字符将不再显示。

#### 显示已创建环境

- 在 Terminal 中输入命令：`conda info --envs` 或 `conda info -e` 或 `conda env list`。结果中星号 `*` 所在行即为当前所在环境。macOS 系统中默认创建的环境名为“base”。

#### 复制环境

- 在 Terminal 中输入命令：`conda create --name <new_env_name> --clone <copied_env_name>`。
  - ① ***<copied_env_name>*** 即为被复制/克隆环境名。环境名两边不加尖括号“<>”。
  - ② ***<new_env_name>*** 即为复制之后新环境的名称。环境名两边不加尖括号“<>”。
  - ③ ***conda create --name py2 --clone python2*** ，即为克隆名为“python2”的环境，克隆后的新环境名为“py2”。此时，环境中将同时存在“python2”和“py2”环境，且两个环境的配置相同。

#### 删除环境

- 在 Terminal 中输入命令：`conda remove --name <env_name> --all`。注意： ***<env_name>*** 为被删除环境的名称。环境名两边不加尖括号“<>”。

### 管理包

#### 模糊查找

- 在 Terminal 中输入命令：`conda search <text>`。
  - 注意： `<text>` 是查找含有**此字段**的包名。此字段两边不加尖括号“<>”。例如： ***conda search py*** 即查找含有“py”字段的包，有哪些版本可供安装。

#### 获取当前环境中已安装的包信息

- 在 Terminal 中输入命令：`conda list`。执行上述命令后将在终端显示当前环境已安装包的包名及其版本号。

#### 安装包

##### 在指定环境中安装包

- 在 Terminal 中输入命令：`conda install --name <env_name> <package_name>`。
  - 注意：
  - ① **<env_name>** 即将包安装的指定环境名。环境名两边不加尖括号“<>”。
  - ② **<package_name>** 即要安装的包名。包名两边不加尖括号“<>”。
  - 例如： ***conda install --name python2 pandas*** 即在名为“python2”的环境中安装pandas包。

##### 在当前环境中安装包

- 在 Terminal 中输入命令：`conda install <package_name>`。
  - 注意：
  - ① ***<package_name>*** 即要安装的包名。包名两边不加尖括号“<>”。
  - ② 执行命令后在当前环境中安装包。
  - 例如： ***conda install pandas*** 即在当前环境中安装pandas包。

##### 从 Anaconda. org 安装包

- 当使用 ***conda install*** 无法进行安装时，可以考虑从 [http://Anaconda.org](https://link.zhihu.com/?target=http%3A//Anaconda.org) 中获取安装包的命令，并进行安装。
- 搜索安装包时，无需注册。
- 选择满足需求的包或下载量最多的包，点击包名。
- 复制“To install this package with conda run:”下方的命令，并粘贴在 Terminal 中执行，完成安装。

#### 卸载包

##### 卸载指定环境中的包

- 在 Terminal 中输入命令：`conda remove --name <env_name> <package_name>`。
  - 注意：
  - ① ***<env_name>*** 即卸载包所在指定环境的名称。环境名两边不加尖括号“<>”。
  - ② ***<package_name>*** 即要卸载包的名称。包名两边不加尖括号“<>”。
  - 例如： ***conda remove --name python2 pandas*** 即卸载名为“python2”中的 pandas 包。

##### 卸载当前环境中的包

- 在 Terminal 中输入命令：`conda remove <package_name>`。
  - 注意：
  - ① ***<package_name>*** 即要卸载包的名称。包名两边不加尖括号“<>”。
  - ② 执行命令后即在当前环境中卸载指定包。
  - 例如： ***conda remove pandas*** 即在当前环境中卸载 pandas 包。

#### 更新包

##### 更新所有包

- 在 Terminal 中输入命令：`conda update --all` 或 `conda upgrade --all`。建议：在安装 Anaconda 之后执行上述命令更新 Anaconda 中的所有包至最新版本，便于使用。

##### 更新指定包

- 在 Terminal 中输入命令：`conda update <package_name>` 或 `conda upgrade <package_name>`。
  - 注意：
  - ① ***<package_name>*** 为指定更新的包名。包名两边不加尖括号“<>”。
  - ② 更新多个指定包，则包名以**空格**隔开，向后排列。如： ***conda update pandas numpy matplotlib*** 即更新pandas、numpy、matplotlib包。

### 安装 R

- 在官网下载并安装最新的 pkg 安装包：[The Comprehensive R Archive Network](https://mirrors.tuna.tsinghua.edu.cn/CRAN/)。
- macOS 10.9 or later 下载安装 XQuartz：[XQuartz](https://www.xquartz.org/)。
- 在 Terminal 中输入命令：`R`，查看 R 版本号。
- 在 jupyter notebook 上安装解释器内核 iRkernel：在 Terminal 中输入命令：`install.packages(c('repr', 'IRdisplay', 'evaluate', 'crayon', 'pbdZMQ', 'devtools', 'uuid', 'digest'))`，在弹出的界面选择合适的仓库，然后一路安装，出现如下结果：Download the package at '/private/var/folders/3/ts5911dn7bq20h89cw8p2crc0000gn/T/RtmpCiXpAc/downloaded_packages'。在 Terminal 中输入命令：`devtools::install_github('IRkernel/IRkernel')`，运行完后，在 Terminal 中输入命令：`IRkernel::installspec ()`，运行完成后，退出 Terminal，新建一个 Terminal 输入 jupyter notebook，看看右上角有没有新建 R 语言 notebook 的选项。

## References

1. [Anaconda介绍、安装及使用教程 - 知乎](https://zhuanlan.zhihu.com/p/32925500)
2. [MacOs系统配置python总结：系统python、Conda、Homebrew切换及PATH配置_Bernard.Dong的博客-CSDN博客](https://blog.csdn.net/BernardDong/article/details/121586842)
3. [在MacOS上安装以及使用Jupyter Notebook运行R语言 | Dave是只学习基](https://davekim3872.github.io/2020/08/12/jupyter-notebook-R/)
