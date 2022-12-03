# MacOS 安装 Python3、R 和 RStudio Desktop

**Table of Contents**

- [1 安装 Python3](#1-安装-python3)
- [2 安装 R](#2-安装-r)
- [3 安装 RStudio Desktop](#3-安装-rstudio-desktop)
- [4 安装 Homebrew](#4-安装-homebrew)
- [5 安装 git 用于与 Github 的版本控制](#5-安装-git-用于与-github-的版本控制)
- [References](#references)

## 1 安装 Python3

- 在官网下载并安装最新的 pkg 安装包：[Python Releases for macOS | Python.org](https://www.python.org/downloads/macos/)。
- 在 Terminal 中输入命令：`python --version`，查看 python 版本号。
- 如果想要使用 python 命令，而非 python3 命令执行 python，那么可以设置环境变量来解决，在终端中执行如下代码：`echo 'alias python=python3'>> .bash_profile`。
- 推出并且重新打开 Terminal，输入 `python`，可看到 Python3。

## 2 安装 R

- 在官网下载并安装最新的 pkg 安装包：[The Comprehensive R Archive Network](https://mirrors.tuna.tsinghua.edu.cn/CRAN/)。

## 3 安装 RStudio Desktop

- 在官网下载并安装最新的安装包：[Download RStudio Desktop](https://posit.co/download/rstudio-desktop/)。

## 4 安装 Homebrew

- 在 Terminal 中输入命令：`export https_proxy=http://127.0.0.1:7890 http_proxy=http://127.0.0.1:7890 all_proxy=socks5://127.0.0.1:789`。

- 在 Terminal 中输入命令：`/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"`。

## 5 安装 git 用于与 Github 的版本控制

- 在 Terminal 中输入命令：`brew install git`。

## References

1. [【B站】2022新版黑马程序员python教程:P5](https://www.bilibili.com/video/BV1qW4y1a7fU?p=5&vd_source=fa22bae99c47db3f7bc43573bd9b3ed3)
2. [Failed to connect to raw.githubusercontent.com:443解决办法](https://zhuanlan.zhihu.com/p/115450863)
3. [安装 Homebrew](https://brew.sh/index_zh-cn)
4. [git(Download for macOS)](https://git-scm.com/download/mac)
