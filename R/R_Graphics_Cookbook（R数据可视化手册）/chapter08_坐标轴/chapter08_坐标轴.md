chapter08_坐标轴
================

- <a href="#8-坐标轴" id="toc-8-坐标轴">8 坐标轴</a>
  - <a href="#81-交换x轴和y轴" id="toc-81-交换x轴和y轴">8.1 交换x轴和y轴</a>
  - <a href="#82-设置连续型坐标轴的值域"
    id="toc-82-设置连续型坐标轴的值域">8.2 设置连续型坐标轴的值域</a>
  - <a href="#83-反转一条连续型坐标轴" id="toc-83-反转一条连续型坐标轴">8.3
    反转一条连续型坐标轴</a>
  - <a href="#84-修改类别型坐标轴上项目的顺序"
    id="toc-84-修改类别型坐标轴上项目的顺序">8.4
    修改类别型坐标轴上项目的顺序</a>
  - <a href="#85-设置x轴和y轴的缩放比例"
    id="toc-85-设置x轴和y轴的缩放比例">8.5 设置x轴和y轴的缩放比例</a>
  - <a href="#86-设置刻度线的位置" id="toc-86-设置刻度线的位置">8.6
    设置刻度线的位置</a>
  - <a href="#87-移除刻度线和标签" id="toc-87-移除刻度线和标签">8.7
    移除刻度线和标签</a>
  - <a href="#88-修改刻度标签的文本" id="toc-88-修改刻度标签的文本">8.8
    修改刻度标签的文本</a>
  - <a href="#89-修改刻度标签的外观问题"
    id="toc-89-修改刻度标签的外观问题">8.9 修改刻度标签的外观问题</a>
  - <a href="#810-修改坐标轴标签的文本"
    id="toc-810-修改坐标轴标签的文本">8.10 修改坐标轴标签的文本</a>
  - <a href="#811-移除坐标轴标签" id="toc-811-移除坐标轴标签">8.11
    移除坐标轴标签</a>
  - <a href="#812-修改坐标轴标签的外观"
    id="toc-812-修改坐标轴标签的外观">8.12 修改坐标轴标签的外观</a>
  - <a href="#813-沿坐标轴显示直线" id="toc-813-沿坐标轴显示直线">8.13
    沿坐标轴显示直线</a>
  - <a href="#814-使用对数坐标轴" id="toc-814-使用对数坐标轴">8.14
    使用对数坐标轴</a>
  - <a href="#815-为对数坐标轴添加刻度"
    id="toc-815-为对数坐标轴添加刻度">8.15 为对数坐标轴添加刻度</a>
  - <a href="#816-绘制环状图形" id="toc-816-绘制环状图形">8.16
    绘制环状图形</a>
  - <a href="#817-在坐标轴上使用日期" id="toc-817-在坐标轴上使用日期">8.17
    在坐标轴上使用日期</a>
  - <a href="#818-在坐标轴上使用相对时间"
    id="toc-818-在坐标轴上使用相对时间">8.18 在坐标轴上使用相对时间</a>

Source：

1.  《R数据可视化手册》，北京：人民邮电出版社，2014.5

# 8 坐标轴

## 8.1 交换x轴和y轴

- 使用`coord_flip()`来翻转坐标轴：

``` r
> library(ggplot2)
> ggplot(PlantGrowth, aes (x=group, y=weight)) + geom_boxplot ()
```

![](chapter08_坐标轴_files/figure-gfm/unnamed-chunk-1-1.png)<!-- -->

``` r
> ggplot(PlantGrowth, aes (x=group, y=weight)) + geom_boxplot() + coord_flip()
```

![](chapter08_坐标轴_files/figure-gfm/unnamed-chunk-1-2.png)<!-- -->

- 对于散点图来说，调换纵轴和横轴上显示的元素非常简单：仅仅交换映射到x和y的变量就可以了。但并不是所有ggplot2中的几何对象都会同等对待x轴和y轴。举例来说，箱线图依y轴对数据计算统计摘要，折线图中的线段只沿x轴移动，误差线只有一个单独的x值但具有若干y值，等等。如果你正在使用这些几何对象，并且希望在图形中交换它们的坐标轴，那么`coord_flip()`正是你所需要的。

- 有时在交换坐标轴后，各项的顺序可能正好与你想要的相反。在一幅有着标准x轴和y轴的图形上，与x对应的项目从左到右排列，这与正常从左到右的阅读方式一致。但是当你交换了坐标轴，各项仍是从原点开始向外排列，在这种情况下就是从下到上，与正常从上到下的阅读方式发生冲突。某些时候这是一个问题，某些时候又不是。如果x变量是一个因子型变量，则排列顺序可以通过使用`scale_x_discrete()`和参数`limits=rev(levels(...))`进行反转：

``` r
> ggplot(PlantGrowth, aes(x=group, y=weight)) + 
+   geom_boxplot() + 
+   coord_flip() + 
+   scale_x_discrete(limits=rev(levels(PlantGrowth$group)))
```

![](chapter08_坐标轴_files/figure-gfm/unnamed-chunk-2-1.png)<!-- -->

- 如果变量是连续型的，参见8.3节以反转其方向。

## 8.2 设置连续型坐标轴的值域

- 你可以使用`xlim()`或`ylim()`来设置一条连续型坐标轴的最小值和最大值。下图展示了一幅使用默认y轴范围的图形和另一幅手动设定y轴范围的图形：

``` r
> p1 <- ggplot(PlantGrowth, aes(x=group, y=weight)) + 
+   geom_boxplot() 
> # 显示基本图形
> p1
```

![](chapter08_坐标轴_files/figure-gfm/unnamed-chunk-3-1.png)<!-- -->

``` r
> p1 + ylim(0, max(PlantGrowth$weight))
```

![](chapter08_坐标轴_files/figure-gfm/unnamed-chunk-3-2.png)<!-- -->

- 第二个示例将y轴的值域设置为从0到weight列的最大值，当然此处使用一个常数值(如10)作为最大值也无妨。

- 使用`ylim()`来设定范围是通过`scale_y_continuous()`来设定范围的简便写法(对于`xlim()`和`scale_x_continuous()`同理)。以下两种表达方式等价:

      ylim(0,10)

      scale_y_continuous (limits=c(0,10))

- 有时，你需要设定`scale_y_continuous()`的其他属性，在这些情况下同时使用`ylim()`和`scale_y_continuous()`可能会让程序产生一些不可预知的行为，这是因为只有命令中的后一条会生效。在以下两个示例中，`ylim(0,10)`应当设定y的值域为从0到10，而`scale_y_continuous(breaks=c(0,5,10))`应将刻度线放置到0、5、10的位置。但是在这两个例子中，仅有第二条命令生效：

``` r
> p1 + ylim(0, 10) + scale_y_continuous(breaks=c(0, 5,10))
```

![](chapter08_坐标轴_files/figure-gfm/unnamed-chunk-4-1.png)<!-- -->

``` r
> p1 + scale_y_continuous(breaks=c(0, 5, 10)) + ylim(0,10)
```

![](chapter08_坐标轴_files/figure-gfm/unnamed-chunk-4-2.png)<!-- -->

- 要让两项修改均生效，舍弃`ylim()`并直接在`scale_y_continuous()`中同时设定limits和breaks即可：

``` r
> p1 + scale_y_continuous(limits=c(0, 10), breaks=c(0, 5, 10))
```

![](chapter08_坐标轴_files/figure-gfm/unnamed-chunk-5-1.png)<!-- -->

- ggplot2中有两种设置坐标轴值域的方式。第一种方式是修改标度，第二种方式是应用一个坐标变换。当你修改x标度和y标度的范围时，任何在范围以外的数据都会被移除，换言之，超出范围的数据不仅不会被展示，而且会被完全移出考虑处理的数据范围。

- 以上文的箱线图为例，如果你限制了y的值域，使得某些原始数据被剪除掉，则箱线图中统计量的计算都会基于修剪后的数据，而箱线的形状也会随之改变。

- 通过使用坐标变换，数据则不会被修剪；从本质上说，它只是将数据放大或缩小到指定的范围。下图展示了两种方式的区别：

``` r
> p1 + scale_y_continuous(limits = c(5,6.5)) # 与使用ylim()相同
```

![](chapter08_坐标轴_files/figure-gfm/unnamed-chunk-6-1.png)<!-- -->

``` r
> p1 + coord_cartesian(ylim = c(5, 6.5))
```

![](chapter08_坐标轴_files/figure-gfm/unnamed-chunk-6-2.png)<!-- -->

- 最后，通过使用`expand_limits()`来单向扩展值域也是可以的。不过，你不能使用它来缩减值域：

``` r
> p1 + expand_limits(y=0)
```

![](chapter08_坐标轴_files/figure-gfm/unnamed-chunk-7-1.png)<!-- -->

## 8.3 反转一条连续型坐标轴

- 使用scale_y\_reverse或scale_x\_reverse。坐标轴的方向也可通过指定反序的范围来反转，先写最大值，再写最小值：

``` r
> ggplot(PlantGrowth, aes(x=group, y=weight)) + geom_boxplot() + scale_y_reverse() #通过指定反序的范围产生类似的效果
```

![](chapter08_坐标轴_files/figure-gfm/unnamed-chunk-8-1.png)<!-- -->

``` r
> ggplot(PlantGrowth, aes(x=group, y=weight)) + geom_boxplot() + ylim(6.5, 3.5)
```

![](chapter08_坐标轴_files/figure-gfm/unnamed-chunk-8-2.png)<!-- -->

- 与`scale_y_continuous()`类似，`scale_y_reverse()`也无法与ylim配合工作(对x轴属性也一样)。如果你希望反转某条坐标轴并为它设定值域，则必须通过反序设定范围的方式，在`scale_y_reverse()`语句内完成：

``` r
> ggplot(PlantGrowth, aes(x=group, y=weight)) + geom_boxplot() + 
+   scale_y_reverse(limits=c(8, 0))
```

![](chapter08_坐标轴_files/figure-gfm/unnamed-chunk-9-1.png)<!-- -->

- 要反转离散型坐标轴项目的顺序，参见8.4节。

## 8.4 修改类别型坐标轴上项目的顺序

- 对于类别型(或者说离散型)坐标轴来说，会有一个因子型变量映射到它上面，坐标轴上项目的顺序可以通过设定`scale_x_discrete()`或`scale_y_discrete()`中的参数limits来修改。要手动设定坐标轴上项目的顺序，将一个依理想顺序排列的水平向量指定给limits即可。你也可以使用这个向量来忽略某些项目：

``` r
> p2 <- ggplot(PlantGrowth, aes(x=group, y=weight)) + 
+   geom_boxplot() 
> p2 + scale_x_discrete(limits=c("trt1", "ctrl", "trt2"))
```

![](chapter08_坐标轴_files/figure-gfm/unnamed-chunk-10-1.png)<!-- -->

- 你也可以使用以上方法在坐标轴上展示项目的子集。使用以下语句将仅显示ctrl和trt1：

``` r
> p2 + scale_x_discrete(limits=c("ctrl","trt1"))
```

![](chapter08_坐标轴_files/figure-gfm/unnamed-chunk-11-1.png)<!-- -->

- 要反转项目顺序，设定`limits=rev(levels(...))`，将因子型变量放入括号中即可。以下语句将反转因子PlantGrowth\$group的顺序：

``` r
> p2 + scale_x_discrete(limits=rev(levels(PlantGrowth$group)))
```

![](chapter08_坐标轴_files/figure-gfm/unnamed-chunk-12-1.png)<!-- -->

- 要根据另外一列数据的值对因子水平进行重排序，参见15.9节。

## 8.5 设置x轴和y轴的缩放比例

- 使用`coord_fixed()`。以下代码将得到x轴和y轴之间1:1的缩放结果：

``` r
> library(gcookbook)  # 为了使用数据集
> sp <- ggplot(marathon, aes(x=Half,y=Full)) + geom_point()
> sp + coord_fixed()
```

![](chapter08_坐标轴_files/figure-gfm/unnamed-chunk-13-1.png)<!-- -->

- marathon数据集中包含了跑步者的全程马拉松成绩和半程马拉松成绩。在这种情况下，强制相同的x轴和y轴缩放比例可能是有用的。

- 通过在`scale_y_continuous()`和`scale_x_continuous()`中调整参数breaks，从而将刻度间距设为相同，也会有所帮助：

``` r
> sp + coord_fixed() +  
+   scale_y_continuous(breaks=seq(0, 420,30)) + 
+   scale_x_continuous(breaks=seq(0, 420,30))
```

![](chapter08_坐标轴_files/figure-gfm/unnamed-chunk-14-1.png)<!-- -->

- 如果你希望为两个坐标轴之间指定其他的固定比例而非相同的比例，可以设置参数ratio。对于marathon数据集，我们可能想让对应半程马拉松时间的坐标轴被拉伸到全程马拉松时间坐标轴的两倍。我们也将在x轴上添加双倍的刻度线：

``` r
> sp + coord_fixed(ratio=1/2) + 
+   scale_y_continuous(breaks=seq(0,420,30)) + 
+   scale_x_continuous(breaks=seq(0,420,15))
```

![](chapter08_坐标轴_files/figure-gfm/unnamed-chunk-15-1.png)<!-- -->

## 8.6 设置刻度线的位置

- 通常来说`ggplot()`会自动将刻度线摆放在合适的位置，但如果你希望改变它们的位置，设置标度中的参数breaks即可：

``` r
> ggplot(PlantGrowth, aes(x=group, y=weight)) + geom_boxplot()
```

![](chapter08_坐标轴_files/figure-gfm/unnamed-chunk-16-1.png)<!-- -->

``` r
> ggplot(PlantGrowth, aes(x=group, y=weight)) + geom_boxplot() + scale_y_continuous(breaks=c(4, 4.25, 4.5, 5, 6, 8))
```

![](chapter08_坐标轴_files/figure-gfm/unnamed-chunk-16-2.png)<!-- -->

- 刻度线的位置决定了绘制主网格线的位置。如果该坐标轴表示一个连续型变量，那么颜色更暗且没有标签的次网格线将被默认绘制在每两个主网格线的正中间位置。

- 你也可以使用`seq()`函数或运算符`:`来生成刻度线的位置向量：

``` r
> seq(4, 7, by=.5)
[1] 4.0 4.5 5.0 5.5 6.0 6.5 7.0
> 5:10
[1]  5  6  7  8  9 10
```

- 如果坐标轴是离散型而不是连续型的，则默认会为每个项目生成一条刻度线。对于离散型坐标轴，你可以通过指定limits来修改项目的顺序或移除项目(参见8.4节)。设定breaks将会决定为哪些水平加上标签，但不会移除它们或是改变它们的顺序。下图展示了当你设定limits和breaks时将会发生的情况：

``` r
> # 为离散型坐标轴同时设定breaks和limits
> ggplot(PlantGrowth, aes(x=group, y=weight)) + 
+   geom_boxplot() + 
+   scale_x_discrete(limits=c("trt2", "ctrl"), breaks="ctrl")
```

![](chapter08_坐标轴_files/figure-gfm/unnamed-chunk-18-1.png)<!-- -->

- 要从图中移除刻度线和刻度线标签(不修改数据)，参见8.7节。

## 8.7 移除刻度线和标签

- 要像下图一样仅移除刻度标签，使用`theme(axis.text.y =element_blank())`(也可对`axis.text.x`做相同处理)即可。这种方法对于连续型和离散型坐标轴均有效：

``` r
> p3 <- ggplot(PlantGrowth, aes(x=group, y=weight)) + 
+   geom_boxplot()
> 
> p3 + theme(axis.text.y = element_blank())
```

![](chapter08_坐标轴_files/figure-gfm/unnamed-chunk-19-1.png)<!-- -->

- 要移除刻度线，可使用`theme(axis.ticks=element_blank())`。这样将会同时移除两轴的刻度线(无法仅隐藏单个坐标轴的刻度线)。在本例中，我们将隐藏所有的刻度线和y轴的刻度标签：

``` r
> p3 + theme(axis.ticks = element_blank(), axis.text.y = element_blank())
```

![](chapter08_坐标轴_files/figure-gfm/unnamed-chunk-20-1.png)<!-- -->

- 要移除刻度线、刻度标签和网格线，将breaks设置为NULL即可：

``` r
> p3 + scale_y_continuous(breaks=NULL)
```

![](chapter08_坐标轴_files/figure-gfm/unnamed-chunk-21-1.png)<!-- -->

- 这种方法仅对连续型坐标轴有效；如果像8.4节中那样使用limits从类别型坐标轴上移除项目，则含有对应值的数据将完全不被显示。

- 事实上，共有三种项目可以控制：刻度标签、刻度线和网格线。对于连续型坐标轴，`ggplot()`通常会在每个breaks值的位置放置刻度线、刻度标签和主网格线。对于类别型坐标轴，这些元素则出现在每个limits值的位置。

- 我们可以独立控制每条坐标轴上的刻度标签。但是，刻度线和网格线必须同时控制。

## 8.8 修改刻度标签的文本

- 考虑下图中的散点图，身高(变量heightIn)是以英寸的数值表示的：

``` r
> library(gcookbook) # 为了使用数据集
> hwp1 <- ggplot(heightweight, aes(x=ageYear, y=heightIn)) + 
+   geom_point()
> hwp1
```

![](chapter08_坐标轴_files/figure-gfm/unnamed-chunk-22-1.png)<!-- -->

- 要像下图一样任意设定标签，在标度中为breaks和labels赋值即可。其中的个标签含有一个换行符()，意为让`ggplot()`在那里另起一行：

``` r
> hwp1 + scale_y_continuous(breaks=c(50,56,60,66,72),
+                          labels=c("Tiny","Really\nshort", "Short", "Medium", "Tallish"))
```

![](chapter08_坐标轴_files/figure-gfm/unnamed-chunk-23-1.png)<!-- -->

- 除了完全任意地设置标签以外，更常见的情况是数据以某种格式存储，而我们希望以另外一种格式显示标签。举例来说，我们可能想让身高变量显示为英尺和英寸的格式(像5’6’’这样)，而不是仅仅显示一个英寸数值。要完成这项任务，我们可以定义一个格式刷(formatter)函数，这样的函数可以读入数值并返回相应的字符串。例如，以下函数可将英寸数值转换为英尺加英寸的格式：

``` r
> footinch_formatter <- function(x){
+   foot <- floor(x/12)
+   inch <- x%%12
+   return(paste(foot, "'", inch,"\"", sep=""))
+          }
```

- 下面是此函数对输入值56\~64的返回结果(反斜杠是转义符，用来区分字符串中所含的引号和字符串本身的定界引号)：

``` r
> footinch_formatter(56:64)
[1] "4'8\""  "4'9\""  "4'10\"" "4'11\"" "5'0\""  "5'1\""  "5'2\""  "5'3\"" 
[9] "5'4\"" 
```

- 现在就可以使用参数labels把我们的函数传递给标度了：

``` r
> hwp1 + scale_y_continuous(labels=footinch_formatter)
```

![](chapter08_坐标轴_files/figure-gfm/unnamed-chunk-26-1.png)<!-- -->

- 在图中，每隔五英寸放置了一个自动生成的刻度线，但是对于这个数据来说看起来有些古怪。我们可以通过指定参数breaks让`ggplot()`每隔四英寸设置一条刻度线取而代之：

``` r
> hwp1 + scale_y_continuous(breaks=seq(48,72,4), labels=footinch_formatter)
```

![](chapter08_坐标轴_files/figure-gfm/unnamed-chunk-27-1.png)<!-- -->

- 另一项常见任务是将时间测度转换为HH:MM:SS(时:分:秒)或者其他类似的格式。以下函数可以读入分钟的数值并将它们转换为这种格式，同时舍入到最接近的秒数(也可以按照你的特殊需要来自定义)：

``` r
> timeHMS_formatter <- function(x) {
+   h <- floor (x/60)
+   m <- floor(x %% 60)
+   s<- round (60*(x %% 1)) # 舍入到最接近的秒数
+   lab <- sprintf("%02d:%02d:%02d", h, m,s)  # 格式化字符串为HH:MM:SS的格式
+   lab <- gsub("^00:", "", lab) # 如果开头存在00:则移除
+   lab <- gsub ("^0", "", lab) # 如果开头存在0则移除
+   return (lab)
+   }
```

- 使用一些示例数值运行它会得到：

``` r
> timeHMS_formatter(c(.33, 50,51.25,59.32,60, 60.1, 130.23))
[1] "0:20"    "50:00"   "51:15"   "59:19"   "1:00:00" "1:00:06" "2:10:14"
```

- 随ggplot2安装的scales包自带了一些内建的格式化函数：

  - `comma()`在千、百万、十亿等位置向数字添加逗号。
  - `dollar()`添加一个美元符号并舍入到最接近的美分。
  - `percent()`乘以100，舍入到最接近的整数值，并添加一个百分号。
  - `scientific()`对大数字和小数字给出科学记数法表示，如3.30e+05。

- 如果你希望使用这些函数，必须首先使用library(scales)加载scales包。

## 8.9 修改刻度标签的外观问题

- 在下图中，我们手动设定了较长的标签一长到足以互相重叠：

``` r
> library(ggplot2)
> bp <- ggplot(PlantGrowth, aes(x=group, y=weight)) + 
+   geom_boxplot() + 
+   scale_x_discrete(breaks=c("ctrl", "trt1", "trt2"),
+                    labels=c("Control", "Treatment 1", "Treatment 2"))
> bp
```

![](chapter08_坐标轴_files/figure-gfm/unnamed-chunk-30-1.png)<!-- -->

- 要将文本逆时针旋转90°，只需使用：

``` r
> bp + theme(axis.text.x = element_text(angle=90, hjust=1, vjust=.5))
```

![](chapter08_坐标轴_files/figure-gfm/unnamed-chunk-31-1.png)<!-- -->

- 将文本旋转30°可以占用更小的纵向空间，并且可以让你在不转头的情况下还能容易地阅读：

``` r
> bp + theme(axis.text.x = element_text(angle=30, hjust=1, vjust=1))
```

![](chapter08_坐标轴_files/figure-gfm/unnamed-chunk-32-1.png)<!-- -->

- 参数hjust和vjust设置了横向对齐(左对齐1居中/右对齐)和纵向对齐(顶部对齐/居中/底部对齐)。

- 除了旋转以外，其他的文本属性，如大小、样式(粗体/斜体/常规)和字体族(如Times或Helvetica)可以使用`element_text()`进行设置：

``` r
> bp + theme(axis.text.x = element_text(family="Times", face="italic",    
+                                       colour="darkred", size=rel(0.9)))
```

![](chapter08_坐标轴_files/figure-gfm/unnamed-chunk-33-1.png)<!-- -->

- 在本例中，size(文字大小)被设为rel(0.9)，意为当前主题基础字体大小的0.9倍。

- 这些命令仅仅控制了单个坐标轴上刻度标签的外观，并不影响其他坐标轴、坐标轴标签、整体的标题或图例。要同时控制所有这些元素的外观，可以使用主题系统，如9.3节中所讨论的那样。

- 参见9.2节以了解更多关于如何控制文本外观的信息。

## 8.10 修改坐标轴标签的文本

- 使用`xlab()`或`ylab()`来修改坐标轴标签的文本：

``` r
> library(gcookbook) # 为了使用数据集
> hwp2 <- ggplot(heightweight, aes(x=ageYear, y=heightIn, colour=sex)) + 
+   geom_point()
> # 使用默认的坐标轴标签
> hwp2
```

![](chapter08_坐标轴_files/figure-gfm/unnamed-chunk-34-1.png)<!-- -->

``` r
> 
> # 设置坐标轴标签
> hwp2 + xlab("Age in years") + ylab("Height in inches")
```

![](chapter08_坐标轴_files/figure-gfm/unnamed-chunk-34-2.png)<!-- -->

- 默认情况下，图形将直接使用数据框中的列名作为坐标轴标签。这对于探索数据来说可能还好，但是在对外呈现数据时，你也许会希望使用更具描述力的坐标轴标签。除了`xlab()`和`ylab()`，也可以使用`labs()`：

``` r
> hwp2 + labs(x = "Age in years", y = "height in inches")
```

![](chapter08_坐标轴_files/figure-gfm/unnamed-chunk-35-1.png)<!-- -->

- 设置坐标轴标签的另一种方法是在标度中指定，就像这样：

``` r
> hwp2 + scale_x_continuous(name="Age in years")
```

![](chapter08_坐标轴_files/figure-gfm/unnamed-chunk-36-1.png)<!-- -->

- 这种方法看起来可能有点别扭，不过可能在你同时设定标度的其他属性(如刻度线位置、值域等)时会比较有用。

- 当然，这种方法同样适用于其他的坐标轴标度，如`scale_y_continuous()`、`scale_x_discrete()`等。

- 还可以使用`\n`来添加换行：

``` r
> hwp2 + scale_x_continuous(name="Age\n(years)")
```

![](chapter08_坐标轴_files/figure-gfm/unnamed-chunk-37-1.png)<!-- -->

## 8.11 移除坐标轴标签

- 对于x轴标签，使用`theme(axis.title.x=element_blank())`。对于y轴标签，针对`axis.title.y`做同样处理。

- 我们将在本例中隐藏x轴标签：

``` r
> p4 <- ggplot(PlantGrowth, aes(x=group, y=weight)) + 
+   geom_boxplot()
> p4 + theme(axis.title.x=element_blank())
```

![](chapter08_坐标轴_files/figure-gfm/unnamed-chunk-38-1.png)<!-- -->

- 某些坐标轴标签对于上下文来说是冗余的或者是显而易见的，因此并不需要显示。在这个示例中，x轴表示变量group，但是这一点可以很明显地从上下文看出来。类似地，如果y轴在每个刻度标签上都标注kg(千克)或类似的单位，则坐标轴标签”weight”就没有必要显示了。

- 移除坐标轴标签的另一种方法是将其设为一个空字符串。但如果以这种方式去做，那么图中将仍为文本留出空间：

``` r
> p4 + xlab("")
```

![](chapter08_坐标轴_files/figure-gfm/unnamed-chunk-39-1.png)<!-- -->

- 当你使用`theme()`来设置`axis.title.x=element_blank()`时，x或y标度的名称是不会改变的，只是这样不会显示文本而且不会为其留出空间。当你设置标签为`""`时，标度的名称就改变了，并且实际上显示了(空白的)文本。

## 8.12 修改坐标轴标签的外观

- 要修改x轴标签的外观，使用`axis.title.x`即可：

``` r
> library(gcookbook) # 为了使用数据集
> hwp1 <- ggplot(heightweight, aes(x=ageYear, y=heightIn)) + 
+   geom_point()
> hwp1 + theme(axis.title.x=element_text(face="italic", colour="darkred", size=14))
```

![](chapter08_坐标轴_files/figure-gfm/unnamed-chunk-40-1.png)<!-- -->

- 对于y轴标签来说，有时不对文本进行旋转会比较有用，如下图所示。标签中的`\n`表示另起一行：

``` r
> hwp1 + ylab("Height\n(inches)") + 
+   theme(axis.title.y=element_text(angle=0, face="italic", size=14))
```

![](chapter08_坐标轴_files/figure-gfm/unnamed-chunk-41-1.png)<!-- -->

- 当调用`element_text()`时，默认的角度是0，所以如果设置了`axis.title.y`但没有指定这个角度，它将以文本的顶部指向上方的朝向显示。如果修改了`axis.title.y`中的其他任何属性并且希望它以正常朝向，即旋转90°显示，则必须手动指定这个角度：

``` r
> hwp1 + ylab("Height\n(inches)") + 
+   theme(axis.title.y=element_text(angle=90, face="italic", colour="darkred",
+                                   size=14))
```

![](chapter08_坐标轴_files/figure-gfm/unnamed-chunk-42-1.png)<!-- -->

- 参见9.2节以了解更多关于如何控制文本外观的信息。

## 8.13 沿坐标轴显示直线

- 使用主题设置中的`axis.line`：

``` r
> library(gcookbook) # 为了使用数据集
> p5 <- ggplot(heightweight, aes(x=ageYear, y=heightIn)) + 
+   geom_point() 
> p5 + theme(axis.line = element_line(colour="black"))
```

![](chapter08_坐标轴_files/figure-gfm/unnamed-chunk-43-1.png)<!-- -->

- 如果你最初使用的主题在绘图区域的周围就有一条边(如`theme_bw()`)，则需要同时重置参数`panel.border`：

``` r
> p5 + theme_bw() + 
+   theme(panel.border = element_blank(),
+         axis.line = element_line(colour="black"))
```

![](chapter08_坐标轴_files/figure-gfm/unnamed-chunk-44-1.png)<!-- -->

- 如果边界线比较粗，则它们的末端将仅会部分地重叠（左下角）：

``` r
> # 对于较粗的线条，只有一半重叠
> p5 + theme_bw() + 
+   theme(panel.border = element_blank(),
+         axis.line = element_line(colour="black", linewidth=4))
```

![](chapter08_坐标轴_files/figure-gfm/unnamed-chunk-45-1.png)<!-- -->

- 要让它们完全重叠（左下角），设置`lineend="square"`即可：

``` r
> # 完全重叠
> p5 + theme_bw() + 
+   theme(panel.border = element_blank(),
+         axis.line = element_line(colour="black", linewidth=4, lineend="square"))
```

![](chapter08_坐标轴_files/figure-gfm/unnamed-chunk-46-1.png)<!-- -->

- 关于主题系统工作原理的更多信息，参见9.3节。

## 8.14 使用对数坐标轴

- 使用`scale_x_log10()`和`/`或`scale_y_log10()`：

``` r
> library(MASS) # 为了使用数据集
> # 基本图形
> p6 <- ggplot(Animals, aes(x=body, y=brain, label=rownames(Animals))) + 
+   geom_text(size=3)
> p6
```

![](chapter08_坐标轴_files/figure-gfm/unnamed-chunk-47-1.png)<!-- -->

``` r
> # 使用对数x标度和对数y标度
> p6 + scale_x_log10() + scale_y_log10()
```

![](chapter08_坐标轴_files/figure-gfm/unnamed-chunk-47-2.png)<!-- -->

- 使用对数坐标轴时，视觉上某段给定的距离表示着常数倍的比例改变；举例来说，y轴上每增加1厘米可能表示数量乘以10。相对而言，使用线性坐标轴时，视觉上某段给定的距离表示着常数单位数量的改变；每增加1厘米可能表示数量上增加了10。

- 某些数据集在x轴上是呈指数分布的，而另一些则是在y轴上呈指数分布(或者两轴皆是)。例如，MASS库中的Animals数据集包含了各类哺乳动物平均脑质量(单位为g)和体重(单位为kg)数据，还加入了若干种恐龙的数据作为对照：

``` r
> head(Animals)
                    body brain
Mountain beaver     1.35   8.1
Cow               465.00 423.0
Grey wolf          36.33 119.5
Goat               27.66 115.0
Guinea pig          1.04   5.5
Dipliodocus     11700.00  50.0
```

- 如上图所示，我们可以绘制一幅散点图来对脑质量和体重之间的关系进行可视化。

- 在使用默认的线性标度坐标轴时，我们很难更好地理解这幅图。由于几种大型动物的存在，其余的动物都被挤到了左下角，这让老鼠(mouse)与三角龙(triceratops)看起来几乎没有区别！这就是一个数据在两条坐标轴上均呈指数分布的例子。

- 关于将刻度线放到何处的问题，ggplot2会试着做出明智的选择，但是如果你不喜欢这些刻度，那么可以通过指定breaks(也可再额外指定labels)来修改它们。在这个示例中，自动生成刻度线的间距较理想的间距更远。针对y轴的刻度线，我们可以像下面这样获得一个含有从10<sup>0到10</sup>3的10的各次幂的向量：

``` r
> 10^(0:3)
[1]    1   10  100 1000
```

- x轴刻度线的工作原理相同，不过由于这里的值域过大，R会自动将输出格式化为科学记数法的形式：

``` r
> 10^(-1:5)
[1] 1e-01 1e+00 1e+01 1e+02 1e+03 1e+04 1e+05
```

- 之后我们就可以使用这些值作为分割点了：

``` r
> p6 + scale_x_log10(breaks=10^(-1:5)) + 
+   scale_y_log10(breaks=10^(0:3))
```

![](chapter08_坐标轴_files/figure-gfm/unnamed-chunk-51-1.png)<!-- -->

- 要让刻度标签转而使用指数记数法，只要使用scales包中的函数`trans_format()`即可：

``` r
> library(scales)
> p6 + scale_x_log10(breaks=10^(-1:5),
+                    labels=trans_format("log10", math_format(10^.x))) + 
+   scale_y_log10(breaks=10^(0:3),
+                 labels=trans_format("log10", math_format(10^.x)))
```

![](chapter08_坐标轴_files/figure-gfm/unnamed-chunk-52-1.png)<!-- -->

- 使用对数坐标轴的另一种方法是，在将数据映射到x和y坐标之前，先对其进行变换。从技术上讲，坐标轴仍然是线性的，它表示对数变换后的数值：

``` r
> ggplot(Animals, aes(x=log10(body), y=log10(brain), 
+                     label=rownames(Animals))) + 
+   geom_text(size=3)
```

![](chapter08_坐标轴_files/figure-gfm/unnamed-chunk-53-1.png)<!-- -->

- 上例中仅使用了一个log10变换，不过使用其他的变换也是可以的，如以2为底的对数变换和自然对数变换，如下图所示。使用这些变换有点复杂，`scale_x_log10()`可以简写，但是对于其他的对数标度而言，我们需要完整地定义它们：

``` r
> library(scales)
> # 对x使用自然对数变换，对y使用log2变换
> p6 + scale_x_continuous(trans = log_trans(),
+                         breaks = trans_breaks("log", function(x) exp(x)), 
+                         labels = trans_format ("log", math_format(e^.x))) + 
+   scale_y_continuous(trans = log2_trans(),
+                      breaks = trans_breaks("log2", function(x) 2^x),
+                      labels = trans_format("log2", math_format(2^.x)))
```

![](chapter08_坐标轴_files/figure-gfm/unnamed-chunk-54-1.png)<!-- -->

- 我们也可以只使用一条对数坐标轴。这种做法对于呈现金融数据往往是有用的，因为这样能够更好地展示出按比例的变化。下图分别使用了线性和对数的y轴来展示苹果公司的股价变化情况。默认的刻度线间距对你的图来说可能并不够好；可以在标度中使用参数breaks来设置它们：

``` r
> library(gcookbook)  # 为了使用数据集
> ggplot(aapl, aes(x=date,y=adj_price)) + geom_line() 
```

![](chapter08_坐标轴_files/figure-gfm/unnamed-chunk-55-1.png)<!-- -->

``` r
> ggplot(aapl, aes(x=date,y=adj_price)) + geom_line() + 
+   scale_y_log10(breaks=c(2,10,50,250))
```

![](chapter08_坐标轴_files/figure-gfm/unnamed-chunk-55-2.png)<!-- -->

## 8.15 为对数坐标轴添加刻度

- 使用`annotation_logticks()`：

``` r
> library (MASS) # 为了使用数据集
> library(scales) # 为了使用trans和format相关函数
> ggplot(Animals, aes(x=body, y=brain, label=rownames(Animals))) + 
+   geom_text(size=3) + 
+   annotation_logticks() + 
+   scale_x_log10(breaks = trans_breaks("log10", function(x) 10^x),
+                 labels = trans_format("log10", math_format(10^.x))) + 
+   scale_y_log10(breaks = trans_breaks("log10", function(x) 10^x),
+                 labels = trans_format("log10", math_format(10^.x)))
```

![](chapter08_坐标轴_files/figure-gfm/unnamed-chunk-56-1.png)<!-- -->

- 使用`annotation_logticks()`创建的刻度线事实上是绘图区域中的几何对象。在每个10的幂次处有一条长刻度线，在每个5的位置处有一条中等长度的刻度线。

- 你可以使用`theme_bw()`让刻度线和网格线的颜色更协调一些。

- 默认情况下，次网格线在视觉上出现在两条主网格线的正中间，但这与对数标度下表示”5”的刻度线位置并不相同。要让两者位置相同，可以手动设定标度的`minor_breaks`参数。要完成这里的任务，我们需要将它们设置为`log10(5*10^(minpow:maxpow))`，也可以缩写为`log10(5) + minpow:maxpow`：

``` r
> library (MASS) # 为了使用数据集
> library(scales) # 为了使用trans和format相关函数
> ggplot(Animals, aes(x=body, y=brain, label=rownames(Animals))) + 
+   geom_text(size=3) + 
+   annotation_logticks() + 
+   scale_x_log10(breaks = trans_breaks("log10", function(x) 10^x),
+                 labels = trans_format("log10", math_format(10^.x)),
+                 minor_breaks = log10(5) + -2:5) + 
+   scale_y_log10(breaks = trans_breaks("log10", function(x) 10^x),
+                 labels = trans_format("log10", math_format(10^.x)), 
+                 minor_breaks = log10(5) + -1:3) + 
+   coord_fixed() + 
+   theme_bw()
```

![](chapter08_坐标轴_files/figure-gfm/unnamed-chunk-57-1.png)<!-- -->

- 关于控制x轴和y轴缩放比例的更多知识，参见8.5节。

## 8.16 绘制环状图形

- 使用`coord_polar()`。对于本例，我们将使用gcookbook包中的wind数据集。它包含了某一天中每隔5分钟的风速和风向样本。风向每隔15°。被分到一个组中，风速则按每5m/s分为子样本：

``` r
> library(gcookbook) # 为了使用数据集
> head(wind)
  TimeUTC Temp WindAvg WindMax WindDir SpeedCat DirCat
3       0 3.54    9.52   10.39      89    10-15     90
4       5 3.52    9.10    9.90      92     5-10     90
5      10 3.53    8.73    9.51      92     5-10     90
6      15 3.63    8.97    9.90      94     5-10     90
7      20 3.71    8.51    9.41      97     5-10     90
8      25 3.73    8.43    9.02      95     5-10     90
```

- 我们将使用`geom_histogram()`对每个speedCat和DirCat的类别绘制样本数量的计数值(见下图)。我们将binwidth设置为15以使直方图的boundary开始于-7.5的位置，这样每个扇形就会居中于0、15、30等位置：

``` r
> ggplot(wind, aes(x=DirCat, fill=SpeedCat)) + 
+   geom_histogram(binwidth=15, boundary=-7.5) + 
+   coord_polar() + 
+   scale_x_continuous(limits=c(0,360))
```

![](chapter08_坐标轴_files/figure-gfm/unnamed-chunk-59-1.png)<!-- -->

- 使用极坐标图时要小心，因为这种图形会扭曲对数据的感知。本例中，在210°的位置有15个风速为15-20的观测以及13个风速大于20的观测，但是对图形匆匆一瞥时，看起来好像风速大于20的观测更多一些。而且还存在三个风速10-15的观测，它们却几乎不可见。在这个例子中，我们可以通过反转图例、使用不同的调色板、添加外框线以及将分割点设置为某些更熟悉的值的方式，让图形稍微美观一些：

``` r
> ggplot(wind, aes(x=DirCat, fill=SpeedCat)) + 
+   geom_histogram(binwidth=15, boundary=-7.5, colour="black", linewidth=.25) + 
+   guides(fill=guide_legend(reverse=TRUE)) + 
+   coord_polar() + 
+   scale_x_continuous(limits=c(0,360), breaks=seq(0, 360, by=45),
+                      minor_breaks=seq(0, 360, by=15)) + 
+   scale_fill_brewer()
```

![](chapter08_坐标轴_files/figure-gfm/unnamed-chunk-60-1.png)<!-- -->

- 使用参数start设置图形起始的角度可能也是有用的，特别是当我们使用一个离散型变量映射为角度(theta)时。起始角度的值以弧度计，如果你知道要调整的角度，则必须将它转换为弧度：

  `coord_polar(start=-45 * pi / 180)`

``` r
> ggplot(wind, aes(x=DirCat, fill=SpeedCat)) + 
+   geom_histogram(binwidth=15, boundary=-7.5, colour="black", linewidth=.25) + 
+   guides(fill=guide_legend(reverse=TRUE)) + 
+   coord_polar(start=-45 * pi / 180) + 
+   scale_x_continuous(limits=c(0,360), breaks=seq(0, 360, by=45),
+                      minor_breaks=seq(0, 360, by=15)) + 
+   scale_fill_brewer()
```

![](chapter08_坐标轴_files/figure-gfm/unnamed-chunk-61-1.png)<!-- -->

- 极坐标可与其他几何对象搭配使用，包括线和点。在使用这些几何对象时有一些重要的问题要牢记于心。首先，默认情况下，对于映射到y(或者说r)的变量，最小值将被映射到中心；换句话说，数据中的最小值将被映射到视觉上半径为0的位置。你可能希望一个为0的数据值被映射到半径为0的位置，但是为了确保图形能这样绘制，需要设置对应的界限
  (limit)。

- 下一个问题是，在使用一个连续型的x(或者说theta)时，数据中的最小值和最大值是重合的。有时这样是可取的，有时却不是。要修改这种默认行为，你需要设置对应的界限。最后，极坐标的theta值不能环绕一周，目前还无法制作一个穿越过起始角度(通常为垂直方向)的几何对象。

- 我们将使用一个示例来阐明这些问题。以下代码根据时间序列数据集mdeaths创建了一个数据框并绘制了下图：

``` r
> # 将mdeaths的时间序列数据放入一个数据框
> md <- data.frame(deaths = as.numeric(mdeaths),
+                  month = as.numeric(cycle(mdeaths)))
> # 计算每个月的平均死亡数量
> library(plyr) # 为了使用ddply()函数
> md <- ddply(md, "month", summarise, deaths = mean (deaths)) 
> head(md)
  month   deaths
1     1 2129.833
2     2 2081.333
3     3 1970.500
4     4 1657.333
5     5 1314.167
6     6 1186.833
> #绘制基本图形
> p7 <- ggplot(md, aes (x=month, y=deaths)) + 
+   geom_line() + 
+   scale_x_continuous(breaks=1:12)
> # 使用coord_polar
> p7 + coord_polar()
```

![](chapter08_坐标轴_files/figure-gfm/unnamed-chunk-62-1.png)<!-- -->

- 第一个问题是，数据的值(范围大约是1000\~2100)被映射为半径，于是最小的数据值就处于半径为0的位置。我们将通过设置y(或者说r)的界限为从0到数据中的最大值来解决这个问题：

``` r
> # 使用coord_polar并将y(r)的下界设置为0
> p7 + coord_polar() + ylim(0, max(md$deaths))
```

![](chapter08_坐标轴_files/figure-gfm/unnamed-chunk-63-1.png)<!-- -->

- 下一个问题是最小和最大的month(月份)值1和12被展示在了同样的角度上。我们将通过设置x的界限为0\~12来解决这个问题，绘制的图形为下图(注意`xlim()`的使用覆盖了p7中的`scale_x_continuous()`，所以它将不再为每个月份显示分割点；参见8.2节以了解更多信息)：

``` r
> p7 + coord_polar() + ylim(0, max(md$deaths)) + xlim(0,12)
```

![](chapter08_坐标轴_files/figure-gfm/unnamed-chunk-64-1.png)<!-- -->

- 还有最后一个首尾不相接的问题。要解决这个问题，我们需要修改数据框，添加一个月份为0，对应值与12月相同的行。这将使得起点和终点变得相同，如下图所示(或者，我们可以添加一个13月，而非0月)：

``` r
> # 通过添加一个值与12的值相同的0来连接曲线
> mdx <- md[md$month==12,]
> mdx$month <- 0
> mdnew <- rbind(mdx,md)
> # 通过使用`%+%`，绘制与之前相同的图形，只是使用的数据不同
> p7 %+% mdnew + coord_polar() + ylim(0, max(md$deaths))
```

![](chapter08_坐标轴_files/figure-gfm/unnamed-chunk-65-1.png)<!-- -->

- **注意运算符`%+%`的使用。当你使`%+%`向一个ggplot对象添加一个数据框时，它会替换ggplot对象中的默认数据框。在本例中，它将p7中默认的数据框从md改为了mdnew。**

- 参见10.4节了解更多关于反转图例方位的信息。

- 参见8.6节以了解更多关于指定哪些值将拥有刻度线(分割点)和刻度标签的方法。

## 8.17 在坐标轴上使用日期

- 将一列类为Date的变量映射到x轴或y轴即可。本例中我们将使用economics数据集：

``` r
> # 观察数据结构
> str(economics)
spc_tbl_ [574 × 6] (S3: spec_tbl_df/tbl_df/tbl/data.frame)
 $ date    : Date[1:574], format: "1967-07-01" "1967-08-01" ...
 $ pce     : num [1:574] 507 510 516 512 517 ...
 $ pop     : num [1:574] 198712 198911 199113 199311 199498 ...
 $ psavert : num [1:574] 12.6 12.6 11.9 12.9 12.8 11.8 11.7 12.3 11.7 12.3 ...
 $ uempmed : num [1:574] 4.5 4.7 4.6 4.9 4.7 4.8 5.1 4.5 4.1 4.6 ...
 $ unemploy: num [1:574] 2944 2945 2958 3143 3066 ...
```

- date列是一个类为Date的对象，将其映射到x所得的结果如下图所示：

``` r
> ggplot(economics, aes(x=date, y=psavert)) + geom_line()
```

![](chapter08_坐标轴_files/figure-gfm/unnamed-chunk-67-1.png)<!-- -->

- ggplot2可以处理两类时间相关的对象：日期对象(类为Date的对象)和日期时间对象(类为POSIXt的对象)。两类对象的区别是，Date
  对象表示的是日期，分辨率为一天，而POSIXt对象则表示时刻，拥有精确到秒的小数部分的分辨率。

- 设置分割点与数值坐标轴的方式类似，主要的不同在于设置所要使用的日期序列。这里我们将使用economics数据集从1992年年中到1993年年中的一个子集。如果未指定分割点，则将自动选择：

``` r
> # economics的一个子集
> econ <- subset(economics, date >= as.Date("1992-05-01") & 
+                  date < as.Date("1993-06-01"))
> # 基本图形，不指定分割点
> p8 <- ggplot(econ, aes(x=date, y=psavert)) + geom_line() 
> p8
```

![](chapter08_坐标轴_files/figure-gfm/unnamed-chunk-68-1.png)<!-- -->

- 分割点可使用函数`seq()`来创建，给定起始和终止日期和一个步长区间即可：

``` r
> # 指定一个日期向量为分割点
> datebreaks <- seq(as.Date("1992-06-01"), as.Date("1993-06-01"), by="2 month")
> # 使用分割点并旋转文本标签
> p8 + scale_x_date(breaks=datebreaks) + 
+   theme(axis.text.x = element_text(angle=30, hjust=1))
```

![](chapter08_坐标轴_files/figure-gfm/unnamed-chunk-69-1.png)<!-- -->

- 注意，这里分割点(标签)的格式发生了改变，可以通过使用scales包中的`date_format()`函数来指定格式。这里我们将使用`"%Y %b`，结果的格式类似于”1992
  Jun”：

``` r
> library(scales)
> p8 + scale_x_date(breaks=datebreaks, labels=date_format("%Y %b")) + 
+   theme (axis.text.x = element_text(angle=30, hjust=1))
```

![](chapter08_坐标轴_files/figure-gfm/unnamed-chunk-70-1.png)<!-- -->

- 常用的日期格式选项列于下表中。它们应被放入一个字符串中传递`给date_format()`，然后这些格式说明符就会被合适的值所替换。举例来说，如果你使用”%B
  %d，%y”，所得的标签将类似于”June 01, 1992”。

| 选项 | 描述                                                          |
|------|---------------------------------------------------------------|
| %Y   | 含世纪的年份(2012)。                                          |
| %y   | 不含世纪的年份(12)。                                          |
| %m   | 十进制数表示的月份(08)。                                      |
| %b   | 当前区域设置（locale）的月份名缩写（Aug）。                   |
| %B   | 当前区域设置的月份名全称（August）。                          |
| %d   | 十进制数表示的月份中的日期(04)。                              |
| %U   | 十进制数表示的一年中的第几周，星期日作为每周的第一天(00-53)。 |
| %W   | 十进制数表示的一年中的第几周，星期一作为每周的第一天(00-53)。 |
| %w   | 星期几(0-6，星期日为0)。                                      |
| %a   | 星期几的缩写名（Thu）。                                       |
| %A   | 星期几的全称（Thursday）。                                    |

- 以上选项中的一部分依赖于计算机的区域设置(locale)。月份和日期在不同的语言中会有不同的名称（本示例是使用美式区域设置生成的）。可以使用`Sys.setlocale()`来修改区域设置。例如，以下代码会将日期的格式修改为使用意大利的区域设置：

``` r
> # Mac和Linux
> Sys.setlocale('LC_TIME','it_IT.UTF-8')
[1] "it_IT.UTF-8"
> # Windows
> Sys.setlocale('LC_TIME','italian')
[1] ""
```

- **注意，区域的名称可能视平台的不同而有所区别，并且你的计算机必须支持这些在操作系统层面己经安装的区域设置。**

- 另见参见`?Sys.setlocale`了解更多关于如何设定区域设置的信息。

- 参见`?strptime`以了解关于如何将字符串转换为日期以及格式化日期输出的信息。

## 8.18 在坐标轴上使用相对时间

- 时间值通常以数字的形式存储。举例来说，钟表上的时刻能够以一个表示小时的数字来存储。时间也能以从某个起始时间经过的分钟数或秒数来存储。在这些情况下，你应当将一个值映射到x轴或y轴上，并使用一个格式刷来生成合适的坐标轴标签：

``` r
> # 转换时间序列对象WWWusage为数据框
> www <- data.frame(minute = as.numeric(time(WWWusage)),
+                   users = as.numeric(WWWusage))
> # 定义一个格式刷函数，可将以分钟表示的时间转换为字符串
> timeHM_formatter <- function(x){
+   h <- floor(x/60) 
+   m <- floor(x%%60)
+   lab <- sprintf('%d:%02d',h,m) # 将字符串格式化为H:MM(时:分)的格式
+   return(lab)
+   }
> # 默认的x轴
> ggplot(www,aes(x=minute,y=users)) + geom_line() 
```

![](chapter08_坐标轴_files/figure-gfm/unnamed-chunk-72-1.png)<!-- -->

``` r
> # 使用格式化后的时间
> ggplot(www,aes(x=minute,y=users)) + geom_line() + 
+   scale_x_continuous(name="time",breaks=seq(0,100,by=10),
+                      labels=timeHM_formatter)
```

![](chapter08_坐标轴_files/figure-gfm/unnamed-chunk-72-2.png)<!-- -->

- 在某些情况下，手动指定分割点和标签可能会简单一些，就像这样：

      scale_x_continuous(breaks=c(0, 20, 40, 60, 80, 100),
                       labels=c('0:00','0:20','0:40','1:00','1:20','1:40'))

- 在前面的示例中，我们使用了函数`timeHM_formatter()`来将数值时间(以分钟表示)转换为一个类似于”1:10”的字符串：

``` r
> timeHM_formatter(c(0,50,51,59,60,130,604))
[1] "0:00"  "0:50"  "0:51"  "0:59"  "1:00"  "2:10"  "10:04"
```

- 要将其转换为HH:MM:SS(时时:分分:秒秒)的格式，你可以使用以下格式刷函数：

``` r
> timeHMS_formatter <- function(x) {
+   h <- floor(x/3600)
+   m <- floor((x/60) %% 60)
+   s <- round (x %% 60) # 舍入到最接近的秒数
+   lab <- sprintf("%02d:%02d:%02d", h, m,s) # 格式化字符串为HH:MM:SS的格式
+   lab <- sub("^00:","", lab) # 如果开头存在00:则移除
+   lab <- sub("^0", "", lab) #如果开头存在0则移除
+   return (lab)
+   }
```

- 使用一些示例数值运行它会得到：

``` r
> timeHMS_formatter(c(20, 3000,3075,3559.2,3600,3606,7813.8))
[1] "0:20"    "50:00"   "51:15"   "59:19"   "1:00:00" "1:00:06" "2:10:14"
```

- 参见15.21节以了解关于如何转换时间序列对象为数据框的信息。
