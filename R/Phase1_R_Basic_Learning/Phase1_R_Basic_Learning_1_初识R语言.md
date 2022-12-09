R语言基础学习（第一阶段）——初识R语言
================

- <a href="#1-r语言介绍" id="toc-1-r语言介绍">1 R语言介绍</a>
  - <a href="#11-r的使用" id="toc-11-r的使用">1.1 R的使用</a>
    - <a href="#111-工作空间" id="toc-111-工作空间">1.1.1 工作空间</a>
  - <a href="#12-包" id="toc-12-包">1.2 包</a>
    - <a href="#121-什么是包" id="toc-121-什么是包">1.2.1 什么是包</a>
    - <a href="#122-包的安装" id="toc-122-包的安装">1.2.2 包的安装</a>
    - <a href="#123-包的载入" id="toc-123-包的载入">1.2.3 包的载入</a>
    - <a href="#124-获取帮助" id="toc-124-获取帮助">1.2.4 获取帮助</a>
- <a href="#2-创建数据集" id="toc-2-创建数据集">2 创建数据集</a>
  - <a href="#21-数据集的概念" id="toc-21-数据集的概念">2.1 数据集的概念</a>
  - <a href="#22-数据结构" id="toc-22-数据结构">2.2 数据结构</a>
    - <a href="#221-向量" id="toc-221-向量">2.2.1 向量</a>
    - <a href="#222-矩阵" id="toc-222-矩阵">2.2.2 矩阵</a>
    - <a href="#223-数组" id="toc-223-数组">2.2.3 数组</a>
    - <a href="#224-数据框" id="toc-224-数据框">2.2.4 数据框</a>
    - <a href="#225-因子" id="toc-225-因子">2.2.5 因子</a>
    - <a href="#226-列表" id="toc-226-列表">2.2.6 列表</a>
  - <a href="#23-数据的输入" id="toc-23-数据的输入">2.3 数据的输入</a>
    - <a href="#231-导入带分隔符的文本文件"
      id="toc-231-导入带分隔符的文本文件">2.3.1 导入带分隔符的文本文件</a>
    - <a href="#232-导入excel电子表格" id="toc-232-导入excel电子表格">2.3.2
      导入Excel电子表格</a>
    - <a href="#233-导入spss文件" id="toc-233-导入spss文件">2.3.3
      导入SPSS文件</a>
  - <a href="#24-数据的导出" id="toc-24-数据的导出">2.4 数据的导出</a>
    - <a href="#241-导出符号分隔文本文件"
      id="toc-241-导出符号分隔文本文件">2.4.1 导出符号分隔文本文件</a>
    - <a href="#242-导出excel电子表格" id="toc-242-导出excel电子表格">2.4.2
      导出Excel电子表格</a>
    - <a href="#243-导出给统计学程序" id="toc-243-导出给统计学程序">2.4.3
      导出给统计学程序</a>
  - <a href="#25-处理数据对象的实用函数"
    id="toc-25-处理数据对象的实用函数">2.5 处理数据对象的实用函数</a>

Source：

1.  《R语言实战（中文第二版）》

2.  [【B站】从零开始学 R
    语言，带你玩转医学统计学](https://www.bilibili.com/video/BV1JU4y1f7zg/?spm_id_from=333.1007.top_right_bar_window_custom_collection.content.click&vd_source=fa22bae99c47db3f7bc43573bd9b3ed3)

3.  [Yufei
    Zhong：R语言学习笔记](https://bookdown.org/zyf19940501/Rbook/)

# 1 R语言介绍

## 1.1 R的使用

- R语句由函数和赋值构成。R使用\<-（快捷键：alt +
  -），而不是传统的=作为赋值符号。例如，以下语句：

<!-- -->

    # 创建一个名为X的向量对象，它包含5个来自标准正态分布的随机偏差。
    x <- rnorm(5)

### 1.1.1 工作空间

- 当前的工作目录(working
  directory)是R用来读取文件和保存结果的默认目录。我们可以使用函数`getwd()`来查看当前的工作目录，或使用函数`setwd()`设定当前的工作目录。如果需要读入一个不在当前工作目录下的文件，则需在调用语句中写明完整的路径。记得使用引号闭合这些目录名和文件名。

- 用于管理工作空间的部分标准命令如下：

``` r
> # 显示当前的工作目录
> getwd()
[1] "/Users/liang.hanqing/Documents/Git-local/Github_Bioinformatics_Learning/R/Phase1_R_Basic_Learning"
> # 列出当前工作空间中的对象
> ls()
character(0)
```

    # 移除(删除)一个或多个对象
    rm(objectlist)
    # 显示可用选项的说明
    help(options)
    # 显示或设置当前选项
    options()

``` r
> # 创建了一个包含20个均匀分布随机变量的向量，生成了此数据的摘要统计量和直方图。
> options(digits=3) # 数字将被格式化,显示为具有小数点后三位有效数字的格式
> x <- runif(20) # 创建了一个包含20个均匀分布随机变量的向量
> summary(x) # 生成了此数据的摘要统计量
   Min. 1st Qu.  Median    Mean 3rd Qu.    Max. 
  0.054   0.312   0.703   0.616   0.808   0.974 
> hist(x) # 生成了此数据的直方图
```

![](Phase1_R_Basic_Learning_1_初识R语言_files/figure-gfm/unnamed-chunk-2-1.png)<!-- -->

## 1.2 包

### 1.2.1 什么是包

- 包是R函数、数据、预编译代码以一种定义完善的格式组成的集合。计算机上存储包的目录称为库(library)。函数`.libPaths( )`能够显示库所在的位置，函数`library()`则可以显示库中有哪些包。

### 1.2.2 包的安装

- 第一次安装一个包，使用命令`install.packages('packages_name')`即可。
- 使用命令`update.packages()`可以更新已经安装的包。
- 要查看已安装包的描述，可以使用`installed.packages()`命令，这将列出安装的包，以及它们的版本号、依赖关系等信息。
- 如把包下载到本地，可在工作区右侧的“Package”打开本地包进行安装。

### 1.2.3 包的载入

- 要在R会话中使用它，还需要使用`library()`命令载入这个包。例如，要使用gclus包，执行命令`library(gclus)`即可。当然，在载入一个包之前必须已经安装了这个包。**在一个会话中，包只需载入一次**。

### 1.2.4 获取帮助

    ?foo 或 help('foo') # 查看函数 foo 的帮助
    ??foo 或 help.search('foo') # 以 foo 为关键词搜索本地帮助文档
    example('foo') # 函数 foo 的使用示例
    RSiteSearch('foo') # 以 foo 为关键词搜索在线文档和邮件列表存档
    apropos('foo',mode = 'function') # 列出名称中含有 foo 的所有可用函数
    data() # 列出当前已加载包中所含的所有可用示例数据集
    vignette() # 列出当前已安装包中所有可用的 vignette 文档
    vignette('foo') # 为主题 foo 显示指定的 vignette 文档

# 2 创建数据集

## 2.1 数据集的概念

- 数据集通常是由数据构成的一个矩形数组，**行表示观测(observation)，列表示变量(variable)**。

## 2.2 数据结构

- R拥有许多用于存储数据的对象类型，包括标量、向量、矩阵、数组、数据框和列表。
- 在R中，对象(object)是指可以赋值给变量的任何事物，包括常量、数据结构、函数，甚至图形。
- 因子(factor)是名义型变量或有序型变量。它们在R中被特殊地存储和处理。

### 2.2.1 向量

- 向量是用于存储数值型、字符型或逻辑型数据的一维数组。执行组合功能的函数`c()`可用来创建向量。

``` r
> a <- c(1, 2, 5, 3, 6, -2, 4)  # a是数值型向量
> b <- c("one", "two", "three")  # b是字符型向量
> c <- c(TRUE, TRUE, TRUE, FALSE, TRUE, FALSE) # c是逻辑型向量
```

- **注意：单个向量中的数据必须拥有相同的类型或模式(数值型、字符型或逻辑型)。同一向量中无法混杂不同模式的数据。**
- **注意：标量是只含一个元素的向量，例如f \<- 3、g \<- “US”和h \<-
  TRUE。它们用于保存常量。**
- 索引：通过在方括号中给定元素所处位置的数值，可以访问向量中的元素。

``` r
> a <- c("k", "j", "h", "a", "c", "m") 
> a[3]
[1] "h"
```

``` r
> a[c(1, 3, 5)]
[1] "k" "h" "c"
```

``` r
> a[2:6]
[1] "j" "h" "a" "c" "m"
```

### 2.2.2 矩阵

- 矩阵是一个二维数组，只是每个元素都拥有相同的模式(数值型、字符型或逻辑型)。可通过函数`matrix()`创建矩阵。一般使用格式为：

<!-- -->

    my_matrix <- matrix(vector, nrow=number_of_rows, ncol=number_of_columns,
                         byrow=logical_value, dimnames=list(
                             char_vector_rownames, char_vector_colnames))

- 其中vector包含了矩阵的元素，nrow和ncol用以指定行和列的维数，dimnames包含了可选的、以字符型向量表示的行名和列名。选项byrow则表明矩阵应当按行填充`(byrow=TRUE)`还是按列填充`(byrow=FALSE)`，**默认情况下按列填充**。注意：这些元素的名字不可更改。

``` r
> # 创建一个5*4的矩阵
> y <- matrix(1:20, nrow=5, ncol=4)
> y
     [,1] [,2] [,3] [,4]
[1,]    1    6   11   16
[2,]    2    7   12   17
[3,]    3    8   13   18
[4,]    4    9   14   19
[5,]    5   10   15   20
```

``` r
> # 创建了一个2×2的含列名标签的矩阵并按 行 进行填充
> cells <- c(1,26,24,68)
> row_names <- c("R1", "R2")
> col_names <- c("C1", "C2")
> my_matrix_1 <- matrix(cells, nrow=2, ncol=2, byrow=TRUE, 
+                       dimnames=list(row_names, col_names))
> my_matrix_1
   C1 C2
R1  1 26
R2 24 68
```

``` r
> # 创建了一个2×2的矩阵并按 列 进行了填充
> my_matrix_2 <- matrix(cells, nrow=2, ncol=2, byrow=FALSE, 
+                       dimnames=list(row_names, col_names))
> my_matrix_2
   C1 C2
R1  1 24
R2 26 68
```

- 可以使用下标和`[方括号]`来选择矩阵中的行、列或元素。`X[i,]`指矩阵X中的第i行，`X[,j]`指第j列，`X[i, j]`指第i行第j个元素。选择多行或多列时，下标i和j可为数值型向量。

``` r
> x <- matrix(1:10, nrow=2)
> x
     [,1] [,2] [,3] [,4] [,5]
[1,]    1    3    5    7    9
[2,]    2    4    6    8   10
```

``` r
> x[2,]
[1]  2  4  6  8 10
```

``` r
> x[,2]
[1] 3 4
```

``` r
> x[1,4]
[1] 7
```

``` r
> x[1,c(4,5)]
[1] 7 9
```

- 案例：构建热图

``` r
> data=as.matrix(mtcars) #heatmap()接受的数值对象为矩阵，因此需要事先将mtcars数据框转成矩阵
> heatmap(data) #不需要传入任何参数，就可以进行热图的绘制。
```

![](Phase1_R_Basic_Learning_1_初识R语言_files/figure-gfm/unnamed-chunk-15-1.png)<!-- -->

``` r
> 
> heatmap(data, scale="column")#传入scale参数。
```

![](Phase1_R_Basic_Learning_1_初识R语言_files/figure-gfm/unnamed-chunk-15-2.png)<!-- -->

``` r
> heatmap(data, scale="column", col = terrain.colors(256),Colv = NA, Rowv = NA)
```

![](Phase1_R_Basic_Learning_1_初识R语言_files/figure-gfm/unnamed-chunk-15-3.png)<!-- -->

### 2.2.3 数组

- 数组(array)与矩阵类似，但是维度可以大于2。数组可通过array函数创建，形式如下:

<!-- -->

    my_array <- array(vector, dimensions, dimnames)

- 其中vector包含了数组中的数据，dimensions是一个数值型向量，给出了各个维度下标的最大值，而dimnames是可选的、各维度名称标签的列表。

``` r
> # 创建一个数组
> dim1 <- c("A1", "A2")
> dim2 <- c("B1", "B2", "B3")
> dim3 <- c("C1", "C2", "C3", "C4")
> z <- array(1:24, c(2, 3, 4), dimnames=list(dim1, dim2, dim3))
> z
, , C1

   B1 B2 B3
A1  1  3  5
A2  2  4  6

, , C2

   B1 B2 B3
A1  7  9 11
A2  8 10 12

, , C3

   B1 B2 B3
A1 13 15 17
A2 14 16 18

, , C4

   B1 B2 B3
A1 19 21 23
A2 20 22 24
```

``` r
> z[1,2,3] # 表示在C3的第一行第二列
[1] 15
```

### 2.2.4 数据框

- 由于不同的列可以包含不同模式(数值型、字符型等)的数据，数据框的概念较矩阵来说更为一般，与通常在SAS、SPSS和Stata中的数据集类似。**数据框是R中最常处理的数据结构**。

- 数据框可通过函数`data.frame()`创建：

<!-- -->

    my_data <- data.frame(col1, col2, col3,...)

- 其中的列向量col1、col2、col3等可为任何类型(如字符型、数值型或逻辑型)。每一列的名称可由函数names指定。

``` r
> patientID <- c(1, 2, 3, 4)
> age <- c(25, 34, 28, 52)
> diabetes <- c("Type1", "Type2", "Type1", "Type1")
> status <- c("Poor", "Improved", "Excellent", "Poor")
> patientdata <- data.frame(patientID, age, diabetes, status)
> patientdata
  patientID age diabetes    status
1         1  25    Type1      Poor
2         2  34    Type2  Improved
3         3  28    Type1 Excellent
4         4  52    Type1      Poor
```

- 选取数据框中元素的方式有若干种。可以使用前述(如矩阵中的)下标记号，亦可直接指定列名。

``` r
> patientdata[1:2]
  patientID age
1         1  25
2         2  34
3         3  28
4         4  52
```

``` r
> patientdata[c("diabetes", "status")]
  diabetes    status
1    Type1      Poor
2    Type2  Improved
3    Type1 Excellent
4    Type1      Poor
```

``` r
> patientdata$age # 表示patientdata数据框中的变量age
[1] 25 34 28 52
```

- 如果想生成糖尿病类型变量diabetes和病情变量status的列联表，使用以下代码即可：

``` r
> table(patientdata$diabetes, patientdata$status)
       
        Excellent Improved Poor
  Type1         1        0    2
  Type2         0        1    0
```

- 可以联合使用函数`attach()`和`detach()`或**单独使用函数`with()`来简化代码**。

- 实例标识符

  - 在病例数据中，病人编号(patientID)用于区分数据集中不同的个体。在R中，实例标识符(case
    identifier)可通过数据框操作函数中的rowname选项指定。例如，语句：

<!-- -->

    patientdata <- data.frame(patientID, age, diabetes,                           
                              status, row.names=patientID)

- 将patientID指定为R中标记各类打印输出和图形中实例名称所用的变量。

### 2.2.5 因子

- 变量可归结为名义型、有序型或连续型变量。

  - **名义型变量是没有顺序之分的类别变量**。糖尿病类型Diabetes(Type1、Type2)是名义型变量的一例。即使在数据中Type1编码为1而Type2编码为2，这也并不意味着二者是有序的。
  - **有序型变量表示一种顺序关系，而非数量关系**。病情Status(poor、improved、excellent)是顺序型变量的一个上佳示例。我们明白，病情为poor(较差)病人的状态不如improved(病情好转)的病人，但并不知道相差多少。
  - **连续型变量可以呈现为某个范围内的任意值，并同时表示了顺序和数量**。年龄Age就是一个连续型变量，它能够表示像14.5或22.8这样的值以及其间的其他任意值。很清楚，15岁的人比14岁的人年长一岁。

- 类别(名义型)变量和有序类别(有序型)变量在R中称为因子(factor)。因子在R中非常重要，因为它决定了数据的分析方式以及如何进行视觉呈现。

- 函数`factor()`以一个整数向量的形式存储类别值，整数的取值范围是`[1...k]`(其中k是名义型变量中唯一值的个数)，同时一个由字符串(原始值)组成的内部向量将映射到这些整数上。举例来说，假设有向量：

<!-- -->

    diabetes <- c("Type1", "Type2", "Type1", "Type1")

- 语句`diabetes <- factor(diabetes)`将此向量存储为(1,2,1,1)，并在内部将其关联为1=Type1和2=Type2(具体赋值根据字母顺序而定)。针对向量diabetes进行的任何分析都会将其作为名义型变量对待，并自动选择适合这一测量尺度1的统计方法。要表示有序型变量，需要为函数`factor()`指定参数ordered=TRUE。给定向量：

<!-- -->

    status <- c("Poor", "Improved", "Excellent", "Poor")

- 语句`status <- factor(status, ordered=TRUE)`会将向量编码为(3,2,1,3)，并在内部将这些值关联为1=Excellent、2=Improved以及3=Poor。另外，针对此向量进行的任何分析都会将其作为有序型变量对待，并自动选择合适的统计方法。

- 对于字符型向量，因子的水平默认依字母顺序创建。这对于因子status是有意义的，因为”Excellent”、“Improved”、“Poor”的排序方式恰好与逻辑顺序相一致。如果”Poor”被编码为”Ailing”，会有问题，因为顺序将为”Ailing”、“Excellent”、“Improved”。如果理想中的顺序是”Poor”、“Improved”、“Excellent”，则会出现类似的问题。按默认的字母顺序排序的因子很少能够让人满意。可以通过指定levels选项来覆盖默认排序。例如:

<!-- -->

    status <- factor(status, order=TRUE,                  
                     levels=c("Poor", "Improved", "Excellent"))

- 各水平的赋值将为1=Poor、2=Improved、3=Excellent。请保证指定的水平与数据中的真实值相匹配，因为任何在数据中出现而未在参数中列举的数据都将被设为缺失值。

- 数值型变量可以用levels和labels参数来编码成因子。如果男性被编码成1，女性被编码成2，则以下语句：

<!-- -->

    sex <- factor(sex, levels=c(1, 2), labels=c("Male", "Female"))

- 把变量转换成一个无序因子。注意到标签的顺序必须和水平相一致。在这个例子中，性别将被当成类别型变量，标签”Male”和”Female”将替代1和2在结果中输出，而且所有不是1或2的性别变量将被设为缺失值。

- 案例：因子的使用

``` r
> patientID <- c(1, 2, 3, 4)
> age <- c(25, 34, 28, 52)
> diabetes <- c("Type1", "Type2", "Type1", "Type1") # 普通因子
> status <- c("Poor", "Improved", "Excellent", "Poor") # 有序因子
> # 以上为以向量形式输入数据
> diabetes <- factor(diabetes)
> status <- factor(status, order=TRUE)
> patientdata <- data.frame(patientID, age, diabetes, status)
> str(patientdata) # 显示对象的结构
'data.frame':   4 obs. of  4 variables:
 $ patientID: num  1 2 3 4
 $ age      : num  25 34 28 52
 $ diabetes : Factor w/ 2 levels "Type1","Type2": 1 2 1 1
 $ status   : Ord.factor w/ 3 levels "Excellent"<"Improved"<..: 3 2 1 3
```

``` r
> summary(patientdata) # 显示对象的统计概要
   patientID         age        diabetes       status 
 Min.   :1.00   Min.   :25.0   Type1:3   Excellent:1  
 1st Qu.:1.75   1st Qu.:27.2   Type2:1   Improved :1  
 Median :2.50   Median :31.0             Poor     :2  
 Mean   :2.50   Mean   :34.8                          
 3rd Qu.:3.25   3rd Qu.:38.5                          
 Max.   :4.00   Max.   :52.0                          
```

### 2.2.6 列表

- **列表(list)是R的数据类型中最为复杂的一种**。一般来说，列表就是一些对象(或成分，component)的有序集合。列表允许你整合若干(可能无关的)对象到单个对象名下。例如，某个列表中可能是若干向量、矩阵、数据框，甚至其他列表的组合。可以使用函数`list()`创建列表：

<!-- -->

    my_list <- list(object1, object2, ...)

- 其中的对象可以是目前为止讲到的任何结构。你还可以为列表中的对象命名：

<!-- -->

    my_list <- list(name1=object1, name2=object2, ...)

- 案例：创建一个列表

``` r
> g <- "My First List"
> h <- c(25, 26, 18, 39)
> j <- matrix(1:10, nrow=5)
> k <- c("one", "two", "three")
> my_list <- list(title=g, ages=h, j, k)  # 创建列表
> my_list   # 输出整个列表
$title
[1] "My First List"

$ages
[1] 25 26 18 39

[[3]]
     [,1] [,2]
[1,]    1    6
[2,]    2    7
[3,]    3    8
[4,]    4    9
[5,]    5   10

[[4]]
[1] "one"   "two"   "three"
```

``` r
> # 输出第二个成分
> my_list[[2]]
[1] 25 26 18 39
```

## 2.3 数据的输入

- **Excel数据文件、SPSS、SAS等文件，都可以使用rstudio的文件导入选项，直接将数据导入。**

### 2.3.1 导入带分隔符的文本文件

- 可以使用`read.table()`从带分隔符的文本文件中导入数据。此函数可读入一个表格格式的文件并将其保存为一个数据框。表格的每一行分别出现在文件中每一行。其语法如下：

<!-- -->

    my_dataframe <- read.table(file, options)

- 其中，file是一个带分隔符的ASCII文本文件，options是控制如何处理数据的选项，具体选项包括：

<!-- -->

    header # 一个表示文件是否在第一行包含了变量名的逻辑型变量
    sep # 分开数据值的分隔符。默认是 sep="",这表示了一个或多个空格、制表符、换行或回车。使用 sep=","来读取用逗号来分隔行内数据的文件,使用 sep="\t"来读取使用制表符来分割行内数据的文件
    row.names # 一个用于指定一个或多个行标记符的可选参数
    col.names # 如果数据文件的第一行不包括变量名 (header=FASLE) , 你可以用 col.names 去指定一个包含变量名的字符向量。 如果 header=FALSE 以及 col.names 选项被省略了, 变量会被分别命名为 V1、V2,以此类推
    na.strings # 可选的用于表示缺失值的字符向量。比如说,na.strings=c("-9", "?")把-9 和?值在读取数据的时候转换成 NA
    colClasses # 可选的分配到每一列的类向量。 比如说, colClasses=c("numeric", "numeric", "character", "NULL", "numeric")把前两列读取为数值型变量,把第三列读取为字符型向量,跳过第四列,把第五列读取为数值型向量。如果数据有多余五列,colClasses 的值会被循环。当你在读取大型文本文件的时候,加上 colClasses 选项可以可观地提升处理的速度
    quote # 用于对有特殊字符的字符串划定界限的自负床。默认值是双引号(")或单引号(')
    skip # 读取数据前跳过的行的数目。这个选项在跳过头注释的时候比较有用
    stringsAsFactors # 一个逻辑变量, 标记处字符向量是否需要转化成因子。 默认值是 TRUE, 除非它被 colClases 所覆盖。当你在处理大型文本文件的时候,设置成 stringsAsFactors=FALSE 可以提升处理速度
    text # 一个指定文字进行处理的字符串。如果 text 被设置了,file 应该被留空。

- 案例：读取studentgrades.csv的文本文件，它包含了学生在数学、科学、和社会学习的分数。

``` r
> grades <- read.table("studentgrades.csv", header=TRUE,     
+                      row.names="StudentID", sep=",")
> grades # print data frame
   First          Last Math Science Social.Studies
11   Bob         Smith   90      80             67
12  Jane         Weary   75      NA             80
10   Dan Thornton, III   65      75             70
40  Mary     "O'Leary"   90      95             92
```

``` r
> str(grades) # view data frame structure
'data.frame':   4 obs. of  5 variables:
 $ First         : chr  "Bob" "Jane" "Dan" "Mary"
 $ Last          : chr  "Smith" "Weary" "Thornton, III" "\"O'Leary\""
 $ Math          : int  90 75 65 90
 $ Science       : int  80 NA 75 95
 $ Social.Studies: int  67 80 70 92
```

- 案例：

- 先安装forestplot、grid、abind、checkmate四个包。

``` r
> library(forestplot)
> os_forest <- read.csv('os_forest.csv',header = FALSE)
> # 读入数据的时候一定要把header设置成FALSE，保证第一行不被当作列名称。
> tiff('Figure_os_forest.tiff',height = 800,width = 1200,res= 150)
> forestplot(labeltext = as.matrix(os_forest[,1:3]),
+            #设置用于文本展示的列，此处用数据的前三列作为文本，在图中展示
+            mean = os_forest$V4, #设置均值
+            lower = os_forest$V5, #设置均值的上限
+            upper = os_forest$V6, #设置均值的下限
+            is.summary = c(T,T,T,F,F,T,F,F,T,F,F),
+            #该参数接受一个逻辑向量，用于定义数据中的每一行是否是汇总值，若是，则在对应位置设置为TRUE，若否，则设置为FALSE；设置为TRUE的行则以粗体出现
+            zero = 1, #设置参照值，此处我们展示的是HR值，故参照值是1，而不是0
+            boxsize = 0.4, #设置点估计的方形大小
+            lineheight = unit(10,'mm'),#设置图形中的行距
+            colgap = unit(3,'mm'),#设置图形中的列间距
+            lwd.zero = 2,#设置参考线的粗细
+            lwd.ci = 1.5,#设置区间估计线的粗细
+            col=fpColors(box='#458B00',  summary= "#8B008B",lines = 'black',zero = '#7AC5CD'),
+            #使用fpColors()函数定义图形元素的颜色，从左至右分别对应点估计方形，汇总值，区间估计线，参考线
+            xlab="The estimates",#设置x轴标签
+            graph.pos = 3)#设置森林图的位置，此处设置为3，则出现在第三列
```

### 2.3.2 导入Excel电子表格

- 使用`install.packages("readxl")`下载安装readxl包，紧接着通过`library("readxl")`加载该包，函数`read_excel()`导入一个工作表到一个数据框中。最简单的格式是`read_excel(file,n)`，其中file是Excel工作簿的所在路径，n则为要导入的工作表序号。

``` r
> library(readxl) 
> workbook <- "/Users/liang.hanqing/Documents/Git-local/Github_Bioinformatics_Learning/R/Phase1_R_Basic_Learning/studentgrades.xlsx" 
> mydataframe <- read_excel(workbook, 1)
```

- 在工作区右侧的Environment，可看到“mydataframe”，单击即可打开数据集。

### 2.3.3 导入SPSS文件

``` r
> library(foreign)
> my_data <- read.spss('pancerdata.sav')
> head(my_data)
$caseno
 [1]  1  2  3  4  5  6  7  9 10 11 12 14 15 16 17 18 19 20 21 22 23 24 25 26 28
[26] 30 33 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 53 54 55 56 58 62
[51] 63 64 65 66 67 68 69 70 71 72 73 74 75 76 77 78 79 80 81 83 84 85 86 87 88
[76] 89 90 91 92 93 94 95 96

$time
 [1]  2.4  1.7  0.1  1.0  4.8  6.4 10.8  5.1  1.1  0.5  0.8  4.0  4.0  4.0  8.5
[16]  3.6  6.9  6.2  1.0  6.2  4.3  3.1  8.3 12.7  4.9  2.7 10.6 18.2  1.4  5.8
[31]  3.0  1.5  2.4  2.0  1.1  2.5  5.4  4.4  4.8  3.1  5.6  3.1  1.3 11.5  3.8
[46]  2.9  2.2  1.7  3.5 11.3  9.0 12.5  6.8 10.8  3.0  1.8  5.0  8.0  6.8 11.1
[61]  9.4  3.9  2.1  4.3  9.3  8.8  2.4 21.6  5.6 11.4 18.3  9.2  4.5  8.2 15.0
[76]  6.9  3.5  2.1  3.1  3.2  1.9  2.1  7.0

$censor
 [1] 死亡 死亡 死亡 死亡 死亡 死亡 死亡 死亡 死亡 死亡 死亡 死亡 死亡 死亡 死亡
[16] 死亡 死亡 死亡 死亡 死亡 死亡 死亡 死亡 死亡 死亡 死亡 死亡 死亡 死亡 死亡
[31] 死亡 死亡 死亡 死亡 死亡 死亡 死亡 死亡 死亡 死亡 死亡 死亡 死亡 死亡 死亡
[46] 死亡 死亡 死亡 死亡 死亡 死亡 死亡 死亡 死亡 死亡 死亡 死亡 死亡 死亡 删失
[61] 死亡 死亡 死亡 死亡 死亡 死亡 死亡 死亡 死亡 死亡 死亡 死亡 死亡 死亡 死亡
[76] 死亡 死亡 死亡 死亡 死亡 死亡 死亡 死亡
Levels: 死亡 删失

$age
 [1] 66 69 48 73 65 38 62 59 53 70 71 61 69 41 49 56 59 53 72 57 49 74 43 60 55
[26] 70 63 69 66 58 67 74 77 70 75 65 71 50 56 68 65 65 43 83 65 63 47 75 63 54
[51] 56 50 62 53 63 59 66 62 72 54 68 63 68 48 68 75 49 62 56 56 59 59 48 64 60
[76] 75 46 53 62 47 62 55 80

$sex
 [1] 男 男 男 男 男 男 女 女 男 男 男 女 男 女 男 男 女 男 女 女 男 男 女 女 女
[26] 男 男 女 女 女 女 男 女 女 男 女 女 男 男 女 女 男 女 男 男 男 女 女 女 男
[51] 女 男 男 女 男 男 女 男 男 男 女 女 女 女 男 女 男 男 女 男 女 男 男 男 男
[76] 男 男 女 男 男 男 男 男
Levels: 男 女

$trt
 [1] 无术中放疗 无术中放疗 无术中放疗 无术中放疗 无术中放疗 无术中放疗
 [7] 无术中放疗 无术中放疗 无术中放疗 无术中放疗 无术中放疗 无术中放疗
[13] 无术中放疗 无术中放疗 无术中放疗 无术中放疗 无术中放疗 无术中放疗
[19] 无术中放疗 无术中放疗 无术中放疗 无术中放疗 有术中放疗 有术中放疗
[25] 有术中放疗 有术中放疗 有术中放疗 有术中放疗 有术中放疗 有术中放疗
[31] 有术中放疗 有术中放疗 有术中放疗 有术中放疗 有术中放疗 有术中放疗
[37] 有术中放疗 有术中放疗 有术中放疗 有术中放疗 有术中放疗 有术中放疗
[43] 有术中放疗 有术中放疗 有术中放疗 有术中放疗 有术中放疗 有术中放疗
[49] 有术中放疗 有术中放疗 有术中放疗 有术中放疗 有术中放疗 有术中放疗
[55] 有术中放疗 有术中放疗 有术中放疗 有术中放疗 有术中放疗 有术中放疗
[61] 有术中放疗 有术中放疗 有术中放疗 有术中放疗 有术中放疗 有术中放疗
[67] 有术中放疗 有术中放疗 有术中放疗 有术中放疗 有术中放疗 有术中放疗
[73] 有术中放疗 有术中放疗 有术中放疗 有术中放疗 有术中放疗 有术中放疗
[79] 有术中放疗 有术中放疗 有术中放疗 有术中放疗 有术中放疗
Levels: 无术中放疗 有术中放疗
```

## 2.4 数据的导出

### 2.4.1 导出符号分隔文本文件

- 可以用`write.table()`函数将R对象输出到符号分隔文件中。函数使用方法是：

<!-- -->

    write.table(x, outfile, sep=delimiter, quote=TRUE, na="NA")

- 其中x是要输出的对象，outfile是目标文件。例如，这条语句：

<!-- -->

    write.table(mydata, "mydata.txt", sep=",")

- 会将mydata数据集输出到当前目录下逗号分隔的mydata.txt文件中。用路径(例如c:/myprojects/mydata.txt)可以将输出文件保存到任何地方。用sep=“替换sep=”,“，数据就会保存到制表符分隔的文件中。默认情况下，字符串是放在引号(”“)中的，缺失值用NA表示。

### 2.4.2 导出Excel电子表格

- 安装writexl包：`install.packages("writexl")`，包中的`writexl::write_xlsx()`函数可以将R数据框写入到Excel文件中。使用方法是：

``` r
> library(writexl) 
> writexl::write_xlsx(patientdata,path = 'patientdata.xlsx')
```

- 在工作区目录下可找到patientdata.xlsx文件。

- 例如，这条语句：

<!-- -->

    library(xlsx) 
    write.xlsx(mydata, "mydata.xlsx")

- 会将mydata数据框保存到当前目录下的Excel文件mydata.xlsx的工作表(默认是Sheet1)中。默认情况下，数据集中的变量名称会被作为电子表格头部，行名称会放在电子表格的第一列。函数会覆盖已存在的mydata.xlsx文件。

### 2.4.3 导出给统计学程序

- foreign包中的`write.foreign()`可以将数据框导出到外部统计软件。这会创建两个文件，一个是保存数据的文本文件，另一个是指导外部统计软件导入数据的编码文件。使用方法如下：

<!-- -->

    write.foreign(dataframe, datafile, codefile, package=package)

- 例如，下面这段代码：

<!-- -->

    library(foreign) 
    write.foreign(mydata, "mydata.txt", "mycode.sps", package="SPSS")

- 会将mydata数据框导出到当前目录的纯文本文件mydata.txt中，同时还会生成一个用于读取该文本文件的SPSS程序mycode.sps。

## 2.5 处理数据对象的实用函数

    length(object) # 显示对象中元素/成分的数量 
    dim(object) # 显示某个对象的维度 
    str(object) # 显示某个对象的结构 
    class(object) # 显示某个对象的类或类型 
    mode(object) # 显示某个对象的模式 
    names(object) # 显示某对象中各成分的名称 
    c(object, object,...) # 将对象合并入一个向量 
    cbind(object, object, ...) # 按列合并对象 
    rbind(object, object, ...) # 按行合并对象 
    object # 输出某个对象 
    head(object) # 列出某个对象的开始部分 
    tail(object) # 列出某个对象的最后部分 
    ls() # 显示当前的对象列表
    rm(object, object, ...) # 删除一个或更多个对象。语句 rm(list = ls())将删除当前工作环境中的几乎所有对象
    newobject <- edit(object) # 编辑对象并另存为newobject 
    fix(object) # 直接编辑对象
