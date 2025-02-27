chapter05_工具箱
================

- <a href="#5-工具箱" id="toc-5-工具箱">5 工具箱</a>
  - <a href="#51-简介" id="toc-51-简介">5.1 简介</a>
  - <a href="#52-图层叠加的总体策略" id="toc-52-图层叠加的总体策略">5.2
    图层叠加的总体策略</a>
  - <a href="#53-基本图形类型" id="toc-53-基本图形类型">5.3 基本图形类型</a>
  - <a href="#54-展示数据分布" id="toc-54-展示数据分布">5.4 展示数据分布</a>
  - <a href="#55-处理遮盖绘制问题" id="toc-55-处理遮盖绘制问题">5.5
    处理遮盖绘制问题</a>
  - <a href="#56-曲面图" id="toc-56-曲面图">5.6 曲面图</a>
  - <a href="#57-绘制地图" id="toc-57-绘制地图">5.7 绘制地图</a>
  - <a href="#58-揭示不确定性" id="toc-58-揭示不确定性">5.8 揭示不确定性</a>
  - <a href="#59-统计摘要" id="toc-59-统计摘要">5.9 统计摘要</a>
  - <a href="#510-添加图形注解" id="toc-510-添加图形注解">5.10
    添加图形注解</a>
  - <a href="#511-含权数据" id="toc-511-含权数据">5.11 含权数据</a>

# 5 工具箱

## 5.1 简介

- 本章分为以下几节：

- 基本的图形类型，详见5.3，绘制常见的、“有名有姓”的图形，如散点图和折线图；

- 展示分布，详见5.4，包括连续型分布和离散型分布、一维分布和二维分布、联合分布和条件分布；

- 应对散点图中的遮盖绘制问题，详见5.5，这是大型数据集带来的一项挑战；

- 绘制曲面图，详见5.6，即在二维平面上展示三维曲面；

- 统计汇总，详见5.9，展示信息丰富的数据摘要；

- 绘制地图，详见5.7；

- 揭示数据中的不确定性和误差，详见5.8，用到多种一维和二维区间；

- 为图形添加注解，详见5.10，使用补充信息来标注、描述并解释图形；

- 绘制加权的数据，详见5.11。

- 本节中的示例将混合使用`ggplot()`和`qplot()`，这更接近于实际的用法。如果你需要关于如何在这两者间转化的提示，请参阅附录A.2。这些示例并不艰深，我们希望读者在阅读完本章后即可绘制出想要的图形。

## 5.2 图层叠加的总体策略

- 在添加图层之前弄清楚它的作用是十分必要的。总体来说，图层有三种用途：

- 用以展示数据本身。我们绘制原始数据的目的可能有很多，这依赖于我们辨识数据的整体结构、局部结构以及离群点等模式的技巧。本层几乎在每幅图形上都会出现。在探索数据的初始阶段，本层通常也是唯一的图层。

- 用以展示数据的统计摘要。随着数据探索和建模的深入，在数据的背景下来展示模型的预测效果是很有用的。我们可以从数据摘要中进一步理解数据，同时对模型作出评价。展示数据本身可以帮助我们改善模型，而展示模型可以帮助我们揭示数据的微妙之处，这也是我们可能漏掉的信息。本层通常绘制在数据层之上。如果回顾前述章节中的示例，可能会发现许多示例图形的数据层上都叠加了一些图层，用以展示某种统计摘要。

- 用以添加额外的元数据(metadata)、上下文信息和注解。元数据层展示了背景的上下文信息，也可为原始数据赋予有现实意义的注解。元数据作为图形背景和图形前景时同样有用。地图就经常作为空间数据的背景层。在绘制作为背景的元数据时，它不应该影响到主数据的展示，因此它往往被放置在主数据的下层，且在配色上尽可能不要太突出。也就是说，如果我们专注地看背景，我们可以很轻松地看到它，但它并不会在我们随意浏览图形时突兀地浮现。其他的元数据可以用来强调数据中的重要特征(feature)。例如，你也许希望为一些拐点或离群点加上解释性的标签，并希望它们尽可能地突出显示。这种情况下，我们希望这种图层是最后绘制的图层。

## 5.3 基本图形类型

- 以下几何对象是ggplot2图形的基本组成部分。每种几何对象自身即可独立构建图形，同时也可以组合起来构建更复杂的几何对象。这些几何对象基本上都关联了一种常见的图形：当某幅图形只使用了一种几何对象构建时，这幅图往往拥有一个特定的名称。

- 这些几何对象均是二维的，故x和y两种图形属性都是不可或缺的。同时，它们都可以接受colour和size图形属性，另外，填充型几何对象（条形、瓦片(tile)和多边形)还可以接受fill图形属性。点使用shape图形属性，线和路径接受linetype图形属性。这些几何对象可用于展示原始数据，另行计算得到的数据摘要和元数据。

- `geom_area()`用于绘制面积图(area
  plot)，即在普通线图的基础上，依y轴方向填充了下方面积的图形。对于分组数据，各组将按照依次堆积的方式绘制。

- `geom_bar(stat="identity")`绘制条形图。我们需要指定stat =
  “identity”，因为默认的统计变换将自动对“值”进行计数（所以本质上这是一个一维的几何对象，参见5.4)。而统计变换identity将保持数据不变。默认情况下，相同位置的多个条形图将以依次向上堆积的形式绘制。

- `geom_line()`绘制线条图。图形属性group决定了哪些观测是连接在一起的；参考4.5.3节以了解更多细节。geom_path与geom_line类似，但geom_path中的线条是根据它们在数据中出现的顺序进行连接的，而非从左至右进行连接。

- `geom_point()`绘制散点图。

- `geom_polygon()`绘制多边形，即填充后的路径。数据中的每一行代表了多边形的一个顶点。在绘图之前将多边形的顶点坐标数据和原始数据进行合并往往会更方便。5.7节以地图数据为例详细地阐明了这个概念。

- `geom_text()`可在指定点处添加标签。它是这些几何对象中唯一一个需要额外图形属性的：它需要指定label参数。我们可以通过设置可选的图形属性hjust和vjust来控制文本的横纵位置；此外，可以设置图形属性angle来控制文本的旋转。你可以参考附录B以了解更多。

- `geom_tile()`用来绘制色深图(image plot)或水平图(level
  plot)。所有的瓦片(tile)构成了对平面的一个规则切分，且往往将fill图形属性映射至另一个变量。

- 使用以下代码绘制以上几何对象，结果如图5.1所示。

``` r
> library(ggplot2)
> df <- data.frame(x=c(3,1,5),y=c(2,4,6),label =c("a","b","c"))
> p1 <- ggplot(df,aes(x,y)) + xlab(NULL) + ylab(NULL) 
> p1 + geom_point() + labs(title = "geom_point") 
```

![](chapter05_工具箱_files/figure-gfm/unnamed-chunk-1-1.png)<!-- -->

``` r
> p1 + geom_bar(stat="identity") + labs(title = "geom_bar(stat=\"identity\")") 
```

![](chapter05_工具箱_files/figure-gfm/unnamed-chunk-1-2.png)<!-- -->

``` r
> p1 + geom_line() + labs(title = "geom_line") 
```

![](chapter05_工具箱_files/figure-gfm/unnamed-chunk-1-3.png)<!-- -->

``` r
> p1 + geom_area() + labs(title = "geom_area") 
```

![](chapter05_工具箱_files/figure-gfm/unnamed-chunk-1-4.png)<!-- -->

``` r
> p1 + geom_path() + labs(title = "geom_path")
```

![](chapter05_工具箱_files/figure-gfm/unnamed-chunk-1-5.png)<!-- -->

``` r
> p1 + geom_text(aes(label=label)) + labs(title = "geom_text") 
```

![](chapter05_工具箱_files/figure-gfm/unnamed-chunk-1-6.png)<!-- -->

``` r
> p1 + geom_tile() + labs(title = "geom_tile") 
```

![](chapter05_工具箱_files/figure-gfm/unnamed-chunk-1-7.png)<!-- -->

``` r
> p1 + geom_polygon() + labs(title = "geom_polygon")
```

![](chapter05_工具箱_files/figure-gfm/unnamed-chunk-1-8.png)<!-- -->

- 图5.1
  使用不同的基本几何对象绘制相同数据的效果。从左上到右下的图形名称分别为：散点图、条形图、线条图、面积图、路径图、含标签的散点图、色深图/水平图和多边形图。注意观察条形图、面积图和瓦片图的坐标轴范围：这三种几何对象占据了数据本身范围以外的空间，于是坐标轴被自动拉伸了。

## 5.4 展示数据分布

- 有一些几何对象可以用于展示数据的分布，具体使用哪种取决于分布的维度、分布是连续型或是离散型，以及我们感兴趣的是条件分布还是联合分布。

- 对于一维连续型分布，最重要的几何对象是直方图。图5.2使用直方图展示了diamond数据中的depth变量。为了找到一个表现力强的视图，多次测试组距的布局细节是必不可少的。例如，我们可以改变组距宽度(binwidth)或者显式地精确指定切分位置(breaks)。

``` r
> qplot(depth, data = diamonds, geom = "histogram")
```

![](chapter05_工具箱_files/figure-gfm/unnamed-chunk-2-1.png)<!-- -->

``` r
> qplot(depth, data = diamonds, geom = "histogram", 
+       binwidth = 0.1, xlim = c(55,70))
```

![](chapter05_工具箱_files/figure-gfm/unnamed-chunk-2-2.png)<!-- -->

- 图5.2
  永远不要指望依靠默认的参数就能对某个具体的分布获得一个表现力强的图形(左图)。（右图）对x轴进行了放大，x1im=c(55,70)，并选取了一个更小的组距宽度，binwidth=0.1，较左图揭示出了更多细节。我们可以发现这个分布是轻度右偏的。同时别忘了在标题中写上重要参数（如组距宽度）的信息。

- 有多种方式可以用来进行分布的跨组比较：同时绘制多个小的直方图，`facets=.~var`；使用频率多边形(frequency
  polygon)，geom=“freqpoly”；或者使用条件密度图，position=“fill”。以下代码演示了这些方式，效果参见图5.3。

``` r
> depth_dist <- ggplot(diamonds,aes(depth)) + xlim(58,68) 
> depth_dist + geom_histogram(aes(y =..density..),binwidth =0.1) + facet_grid(cut ~.)
```

![](chapter05_工具箱_files/figure-gfm/unnamed-chunk-3-1.png)<!-- -->

``` r
> depth_dist + geom_histogram(aes(fill=cut),binwidth=0.1,position="fill")
```

![](chapter05_工具箱_files/figure-gfm/unnamed-chunk-3-2.png)<!-- -->

``` r
> depth_dist + geom_freqpoly(aes(y =..density..,colour=cut), binwidth=0.1)
```

![](chapter05_工具箱_files/figure-gfm/unnamed-chunk-3-3.png)<!-- -->

- 图5.3
  钻石数据切割和深度分布的三种视图。从上至下分别是分面直方图、条件密度图和频率多边形图。它们都显示了出一个有趣的模式：随着钻石质量的提高，分布逐渐向左偏移且愈发对称。

- 作为几何对象的直方图和频率多边形均使用了stat_bin统计变换。此统计变换生成了两个输出变量count和density。变量count为默认值，因为它的可解释性更好。而变量density基本上相当于count除以count的总数，此变量在我们想要比较不同分布的形状而不是数据的绝对大小时更有用。特别地，我们经常使用此变量来比较数据中不同大小子集的分布。

- 和分布相关的许多几何对象都是以几何对象(geom)/统计变换(stat)的形式成对出现的。这些几何对象中大多数的本质都是别名(alias)：一个基本几何对象结合一个统计变换，即可绘制出想要的图形。表面上看，箱线图(boxplot)似乎是一个例外，但在幕后实现上，geom_boxplot同样是使用基本的条、线和点组合而成的。

- geom_boxplot = stat_boxplot +
  geom_boxplot：箱线图，即一个连续型变量针对一个类别型变量取条件所得的图形。当类别型变量有许多独立的取值时，这种图形比较有用。不过当类别型变量的取值很少时，仿照上文直接研究分布的具体形状更佳。箱线图也可对连续型变量取条件，前提是数据预先经过巧妙地封箱(binning)处理。图5.4展示了针对类别型或连续型变量取条件所得的箱线图。

``` r
> library(plyr)
> qplot(cut,depth,data = diamonds,geom = "boxplot") 
```

![](chapter05_工具箱_files/figure-gfm/unnamed-chunk-4-1.png)<!-- -->

``` r
> qplot(carat,depth,data = diamonds,geom = "boxplot", group = round_any(carat,0.1,floor),xlim = c(0,3))
```

![](chapter05_工具箱_files/figure-gfm/unnamed-chunk-4-2.png)<!-- -->

- 图5.4
  箱线图可以用于观察针对一个类别型变量（如cut)取条件时（左图），或连续型变量(如carat)取条件时（右图），连续型变量的分布情况。对于连续型变量，必须设置group图形属性以得到多个箱线图。此处使用了`group = round_any(carat,0.1,floor)`来获得针对变量carat以0.1个单位为大小封箱后的箱线图。

- geom_jitter = position_jitter +
  geom_point：通过在离散型分布上添加随机噪声以避免遮盖绘制问题，这是一种较为粗糙的方法。使用以下代码绘制的图5.5展示了这样的一个例子。

``` r
> qplot(class,cty,data = mpg,geom = "jitter") 
```

![](chapter05_工具箱_files/figure-gfm/unnamed-chunk-5-1.png)<!-- -->

``` r
> qplot(class,drv,data = mpg,geom = "jitter")
```

![](chapter05_工具箱_files/figure-gfm/unnamed-chunk-5-2.png)<!-- -->

- 图5.5几何对象jitter可在二维分布中有一个离散型变量时绘制出一个较为粗略的图形。总体来说，这种数据打散的处理对小数据集更有效。上图展示了mpg数据集中离散型变量class和连续型变量city,下图则将连续型变量city替换为离散型变量drv。

- geom_density = stat_density +
  geom_area：基于核平滑方法进行平滑后得到的频率多边形，如2.5.3节中所述。请仅在已知潜在的密度分布为平滑、连续且无界的时候使用这种密度图。可以使用参数adjust来调整所得密度曲线的平滑程度。使用以下代码绘制的图5.6展示了这样一个例子。

``` r
> qplot(depth,data = diamonds,geom = "density",xlim =c(54,70)) 
```

![](chapter05_工具箱_files/figure-gfm/unnamed-chunk-6-1.png)<!-- -->

``` r
> qplot(depth,data = diamonds,geom = "density",xlim =c(54,70), fill = cut,alpha = I(0.2))
```

![](chapter05_工具箱_files/figure-gfm/unnamed-chunk-6-2.png)<!-- -->

- 图5.6
  密度图实际上就是直方图的平滑化版本。它的理论性质比较理想，但难以由图回溯到数据本身。左图为变量depth的密度图。右图为按照变量cut的不同取值上色的版本。

## 5.5 处理遮盖绘制问题

- 散点图是研究两个连续型变量间关系的重要工具。但是当数据量很大时，这些点经常会出现重叠现象，从而掩盖真实的关系。在极端情况下，我们甚至只能看到数据所在的大致范围，根据这种图形作出的任何结论都是值得怀疑的。这种问题被称为遮盖绘制(overplotting)，对付它有许多方法：

- 小规模的遮盖绘制问题可以通过绘制更小的点加以缓解，或者使用中空的符号，如图5.7所示。所用数据是从两个独立的正态分布中抽样所得的2000个点，所用代码如下：

``` r
> df <- data.frame(x = rnorm(2000),y = rnorm(2000)) 
> norm <- ggplot(df,aes(x,y)) 
> norm + geom_point()
```

![](chapter05_工具箱_files/figure-gfm/unnamed-chunk-7-1.png)<!-- -->

``` r
> norm + geom_point(shape = 1)
```

![](chapter05_工具箱_files/figure-gfm/unnamed-chunk-7-2.png)<!-- -->

``` r
> norm + geom_point(shape =".") # 点的大小为像素级
```

![](chapter05_工具箱_files/figure-gfm/unnamed-chunk-7-3.png)<!-- -->

- 图5.7修改使用的符号可以帮助我们处理轻微到中等程度的遮盖绘制问题。从左至右分别为：默认的shape、shape=1(中空的点)，以及shape=“.”(像素大小的点)。

- 对于更大的数据集产生的更为严重的遮盖绘制问题，我们可以使用α混合（调整透明度）让点呈现透明效果。假设我们以比值形式指定α的值，则分母代表的是一个位置的颜色变为完全不透明时所需重叠点的数量。在R中，可用的最小透明度为1/256，所以对于严重的遮盖绘制问题，这种方法的效果并不会太好。图5.8演示了一些取值的效果，代码如下。

``` r
> norm + geom_point(colour = "black",alpha =1/3) 
```

![](chapter05_工具箱_files/figure-gfm/unnamed-chunk-8-1.png)<!-- -->

``` r
> norm + geom_point(colour = "black",alpha =1/5) 
```

![](chapter05_工具箱_files/figure-gfm/unnamed-chunk-8-2.png)<!-- -->

``` r
> norm + geom_point(colour = "black",alpha = 1/10)
```

![](chapter05_工具箱_files/figure-gfm/unnamed-chunk-8-3.png)<!-- -->

- 图5.8
  以从一个二元正态数据中抽样所得的数据为例，使用α混合来减轻遮盖绘制问题。α值从左至右分别为：1/3，1/5，1/10。

- 如果数据存在一定的离散性，我们可以通过在点上增加随机扰动来减轻重叠。特别是在与透明度一起使用时，这种方法很有效。默认情况下，增加的扰动量是数据分辨率(resolution)的40%，这样可为数据中的邻接区域留下一定的小间隙。在图5.9中，diamond数据中的变量table依最近的整数作取整处理，所以此处也可以设置两个连续整数间距的一半（即0.5）作为打散的宽度。完整的代码如下。

``` r
> td <- ggplot(diamonds,aes(table,depth)) + 
+   xlim(50,70) + ylim(50,70) 
> td + geom_point() 
```

![](chapter05_工具箱_files/figure-gfm/unnamed-chunk-9-1.png)<!-- -->

``` r
> td + geom_jitter()
```

![](chapter05_工具箱_files/figure-gfm/unnamed-chunk-9-2.png)<!-- -->

``` r
> jit <- position_jitter(width = 0.5) 
> td + geom_jitter(position = jit)
```

![](chapter05_工具箱_files/figure-gfm/unnamed-chunk-9-3.png)<!-- -->

``` r
> td + geom_jitter(position = jit,colour = "black",alpha = 1/10) 
```

![](chapter05_工具箱_files/figure-gfm/unnamed-chunk-9-4.png)<!-- -->

``` r
> td + geom_jitter(position = jit,colour = "black",alpha = 1/50) 
```

![](chapter05_工具箱_files/figure-gfm/unnamed-chunk-9-5.png)<!-- -->

``` r
> td + geom_jitter(position = jit,colour = "black",alpha = 1/200)
```

![](chapter05_工具箱_files/figure-gfm/unnamed-chunk-9-6.png)<!-- -->

- 图5.9
  diamond数据中的变量table和变量depth组成的图形，展示了如何使用数据打散和α混合来减轻离散型数据中的遮盖绘制问题。从左至右为：不加任何处理的点，使用默认扰动参数打散后的点，横向扰动参数为0.5（横轴单位距离的一半）时打散后的点，α取值1/10，a取值1/50，a取值1/200。

- 受此启发，我们也可以认为遮盖绘制问题是一种二维核密度估计问题，于是又可引申出以下两种方法：

- 将点分箱并统计每个箱中点的数量，然后通过某种方式可视化这个数量(直方图的二维推广)。将图形划分为小的正方形箱可能会产生分散注意力的视觉假象。Carr等人(I987)建议使用六边形代之，这类图形可以使用geom_hexagon这一几何对象实现，它使用了hexbin包(Carr
  et
  al,.2008)提供的功能。图5.10对比了正方形箱和六边形箱的效果，使用了参数bins和binwidth来控制箱的数量和大小。完整代码如下：

``` r
> d <- ggplot(diamonds,aes(carat,price)) + xlim(1,3) + theme(legend.position = "none") 
> d + stat_bin2d()
```

![](chapter05_工具箱_files/figure-gfm/unnamed-chunk-10-1.png)<!-- -->

``` r
> d + stat_bin2d(bins = 10)
```

![](chapter05_工具箱_files/figure-gfm/unnamed-chunk-10-2.png)<!-- -->

``` r
> d + stat_bin2d(binwidth = c(0.02,200)) 
```

![](chapter05_工具箱_files/figure-gfm/unnamed-chunk-10-3.png)<!-- -->

``` r
> d + stat_binhex()
```

![](chapter05_工具箱_files/figure-gfm/unnamed-chunk-10-4.png)<!-- -->

``` r
> d + stat_binhex(bins = 10)
```

![](chapter05_工具箱_files/figure-gfm/unnamed-chunk-10-5.png)<!-- -->

``` r
> d + stat_binhex(binwidth = c(0.02,200))
```

![](chapter05_工具箱_files/figure-gfm/unnamed-chunk-10-6.png)<!-- -->

- 图5.10
  第一行使用正方形显示分箱，第二行使用六边形显示。左栏使用默认分箱参数，中栏使用参数bins=10，右栏使用参数binwidth=c(0.02,200)。为了节约空间，均略去了图例。

- 使用stat_density2d作二维密度估计，并将等高线添加到散点图中，或以着色瓦片(colored
  tiles)直接展示密度，或使用大小与分布密度成比例的点进行展示。图5.11展示了部分选项的效果，代码如下：

``` r
> d + geom_point() + geom_density2d()
```

![](chapter05_工具箱_files/figure-gfm/unnamed-chunk-11-1.png)<!-- -->

``` r
> d + stat_density2d(geom ="point",aes(size =..density..), contour = F) + scale_size_area()
```

![](chapter05_工具箱_files/figure-gfm/unnamed-chunk-11-2.png)<!-- -->

``` r
> d + stat_density2d(geom = "tile",aes(fill =..density..), contour = F)
```

![](chapter05_工具箱_files/figure-gfm/unnamed-chunk-11-3.png)<!-- -->

``` r
> last_plot() + scale_fill_gradient(limits = c(1e-5,8e-4))
```

![](chapter05_工具箱_files/figure-gfm/unnamed-chunk-11-4.png)<!-- -->

- 图5.11
  使用密度估计对点的密度建模并进行可视化。上图为基于点和等高线的密度展示，下图为基于色深的密度展示。

- 如果我们对给定x时y的条件分布感兴趣，那么2.5.3节中所述的技术也会是有用的。

- 对付遮盖绘制问题的另外一种方法是在图形上添加数据摘要，以指引人眼在茫茫数据中发现所寻模式的真实形状。例如，我们可以使用geom_smooth添加一条平滑曲线来展示数据的中心。本书5.9节中给出了更多的思路。

## 5.6 曲面图

- ggplot2暂不支持真正的三维曲面图。但具有在二维平面上展现三维曲面的常见工具：等高线图，着色瓦片(colored
  tiles)以及气泡图。这些图形在上节中被用来绘制二维密度分布面。对于三维交互式图形和真实三维曲面的绘制，建议关注一下RGL,<http://rgl.neoscientists,org/about.shtml>。

## 5.7 绘制地图

- ggplot2提供了一些工具，让使用maps包绘制的地图与其他ggplot2图形的结合变得十分方便。较新版本的ggplot2中引人的几何对象`geom_map()`，可以大大简化等高线图的绘制过程。关于中国地图的绘制，可参考[R
  语言画中国地图](https://xiangyun.rbind.io/2022/02/draw-china-maps/)一文。我们使用地图数据可能有两种主要原因：一是为空间数据图形添加参考轮廓线，二是通过在不同的区域填充颜色以构建等值线图(choropleth
  map)。

- 添加地图边界可通过函数`borders()`来完成。函数的前两个参数指定了要绘制的地图名map以及其中的具体区域region,其余的参数用于控制边界的外观：如边界的颜色colour和线条粗细size。如果我们想要的是填充颜色的多边形而不是单纯的边界，可以通过设定参数fill来实现。以下代码使用`borders()`展示了图5.12中的空间数据。

``` r
> library(maps)
> data(us.cities)
> big_cities <- subset(us.cities,pop > 500000)
> qplot(long,lat,data = big_cities) + borders("state",size =0.5) 
```

![](chapter05_工具箱_files/figure-gfm/unnamed-chunk-12-1.png)<!-- -->

``` r
> tx_cities <- subset(us.cities,country.etc =="TX") 
> ggplot(tx_cities,aes(long,lat)) + borders("county","texas",colour ="grey70") + 
+   geom_point(colour ="black",alpha = 0.5)
```

![](chapter05_工具箱_files/figure-gfm/unnamed-chunk-12-2.png)<!-- -->

- 图5.12
  函数`borders()`的使用实例。左图展示了美国(2006年1月)五十万人口以上的城市，右图为德克萨斯州的城市区划。

- 等值线图(choropleth
  map)则相对更难处理一些，自动化程度也没那么高，原因在于，要将我们数据中的标识符(identifier)同地图数据中的标识符完全匹配起来是有一定挑战性的。以下实例展示了如何使用`map_data()`将地图数据转换为数据框，此数据框可以在之后通过`merge()`操作与我们的数据相融合，最终绘制出等值线图。结果如图5.13所示。我们数据中的细节可能不同，但关键在于，我们的数据和地图数据中要有一列可以相互匹配。

``` r
> library(maps)
> states <- map_data("state") 
> arrests <- USArrests
> names(arrests) <- tolower(names(arrests)) 
> arrests$region <- tolower(rownames(USArrests))
> 
> choro <- merge(states,arrests,by = "region") 
> # 由于绘制多边形时涉及顺序问题
> # 且merge破坏了原始排序故将行重新排序
> choro <- choro[order(choro$order),]
> qplot(long,lat,data = choro,group = group, fill = assault, geom = "polygon") 
```

![](chapter05_工具箱_files/figure-gfm/unnamed-chunk-13-1.png)<!-- -->

``` r
> qplot(long,lat,data = choro,group = group, fill = assault / murder,geom = "polygon")
```

![](chapter05_工具箱_files/figure-gfm/unnamed-chunk-13-2.png)<!-- -->

- 图5.13
  左侧的等值线图展示了各州人身伤害案件的数量，右侧的等值线图展示了人身伤害和谋杀类案件的比率。

- 如果我们想对数据做进一步处理，函数`map_data()`也是很有用的。下例中，我们计算了爱荷华州每个郡的（近似）中心，然后利用这些中心位置数据在地图上对其名称进行标注。

``` r
> library(plyr) #ddply()在新版本中已被剥离并整合到plyr包中，这里先载入该包
> ia <- map_data("county","iowa")
> mid_range <- function(x) mean(range(x,na.rm = TRUE)) 
> centres <- ddply(ia,.(subregion),colwise(mid_range,.(lat,long))) 
> ggplot(ia,aes(long,lat)) + geom_polygon(aes(group = group), fill = NA,colour = "grey60") +
+   geom_text(aes(label = subregion),data = centres, size = 2,angle = 45)
```

![](chapter05_工具箱_files/figure-gfm/unnamed-chunk-14-1.png)<!-- -->

## 5.8 揭示不确定性

- 不论是从模型所得或是从对分布的假设而得，如果我们已经知道了一些关于数据中不确定性的信息，那么对这些信息加以展示通常是很重要的。在ggplot2中，共有四类几何对象可以用于这项工作，具体使用哪个取决于x的值是离散型还是连续型的，以及我们是否想要展示区间内的中间值，或是仅仅展示区间。这些几何对象列于表5.2中。它们均假设我们对给定x时y的条件分布感兴趣，并且都使用了图形属性ymin和ymax来确定y的值域。如果你想绘制出相反的结果，请参看7.3.3节中的coord_flip。

- 由于标准误的计算方式有很多，所以具体如何计算将由你自己决定。对于比较简单的情况，ggplot2提供了部分数据摘要计算函数（在5.9节中有阐述），不过，我们完全可以自行计算。对于线性模型，effects包(Fox,2008)非常适合提取其中的这类值。下例拟合了一个双因素含交互效应回归模型，并且展示了如何提取边际效应(marginal
  effects)和条件效应(conditional
  effects),以及如何将其可视化。图5.15侧重于对类别型变量color的研究，而图5.16侧重于对连续型变量carat的分析。

``` r
> d1 <- subset(diamonds,carat < 2.5 & rbinom(nrow(diamonds),1,0.2)==1) 
> d1$lcarat <- log10(d1$carat) 
> d1$lprice <- log10(d1$price)
> 
> # 剔除整体的线性趋势
> detrend <- lm(lprice ~ lcarat,data = d1) 
> d1$lprice2 <- resid(detrend)
> 
> mod <- lm(lprice2 ~ lcarat * color,data = d1)
> 
> library(effects)
> effectdf <-function(...){
+   suppressWarnings(as.data.frame(effect(...)))}
> color <- effectdf("color",mod)
> both1 <- effectdf("lcarat:color",mod)
> 
> carat <- effectdf("lcarat",mod,default.levels = 50) 
> both2 <- effectdf("lcarat:color",mod,default.levels = 3)
> 
> # 图5.14
> qplot(lcarat,lprice,data=d1,colour = color) 
```

![](chapter05_工具箱_files/figure-gfm/unnamed-chunk-15-1.png)<!-- -->

``` r
> qplot(lcarat,lprice2,data=d1,colour = color) 
```

![](chapter05_工具箱_files/figure-gfm/unnamed-chunk-15-2.png)<!-- -->

- 图5.14
  进行数据变换以移除显而易见的效应。左图对x轴和y轴的数据均取以10为底的对数以剔除非线性性。右图剔除了主要的线性趋势。

``` r
> # 图5.15
> fplot <- ggplot(mapping = aes(y = fit,ymin = lower,ymax = upper)) + 
+   ylim(range(both2$lower,both2$upper))
> fplot %+% color + aes(x = color) + geom_point() + geom_errorbar() 
```

![](chapter05_工具箱_files/figure-gfm/unnamed-chunk-16-1.png)<!-- -->

``` r
> fplot %+% both2 + aes(x = color,colour = lcarat,group = interaction(color,lcarat)) + 
+   geom_errorbar() + geom_line(aes(group=lcarat)) + 
+   scale_colour_gradient() 
```

![](chapter05_工具箱_files/figure-gfm/unnamed-chunk-16-2.png)<!-- -->

- 图5.15
  展示模型估计结果中变量color的不确定性。左图为color的边际效应。右图则是针对变量caret的不同水平(level),变量color的条件效应。误差棒显示了95%的逐点置信区间。

``` r
> # 图5.16
> fplot %+% carat + aes(x = lcarat) + geom_smooth(stat = "identity")
```

![](chapter05_工具箱_files/figure-gfm/unnamed-chunk-17-1.png)<!-- -->

``` r
> 
> ends <- subset(both1,lcarat = max(lcarat))
> fplot %+% both1 + aes(x = lcarat,colour = color) + geom_smooth(stat="identity") +
+   scale_colour_hue() + theme(legend.position = "none") + 
+   geom_text(aes(label = color,x = lcarat + 0.02),ends)
```

![](chapter05_工具箱_files/figure-gfm/unnamed-chunk-17-2.png)<!-- -->

- 图5.16
  展示模型估计结果中变量carat的不确定性。左图为caret的边际效应。右图则是针对变量color的不同水平，变量caret的条件效应。误差带显示了95%的逐点置信区间。

- 注意，在为这类图形添加题注时，我们需要细致地描述其中所含置信区间的本质，并说明观察置信区间之间的重叠是否有意义（说明：当比较不同组时，如果区间没有重叠，则说明差异显著)。即，这些标准误是针对单组的均值的，还是针对不同组件均值之差的。在计算和展示这些标准误时，multcomp包和multcompView包将非常有用，同时他们在多重比较中能正确地对自由度进行调整。

## 5.9 统计摘要

- 对于每个x的取值，计算对应y值的统计摘要通常是很有用的。在ggplot2中，这一角色由`stat_summary()`担当，它使用ymin，y和ymax等图形属性，为汇总y的条件分布提供了一种灵活的方式。

- 使用`stat_summary()`时，你既可以为每一个参数单独地指定摘要计算函数，也可以用一个统一的函数对它们进行组合。

## 5.10 添加图形注解

- 在使用额外的标签注解图形时要记住的重要一点是：这些注解仅仅是额外的数据而已。添加图形注解有两种基本的方式：逐个添加或批量添加。

- 逐个添加的方式适合少量的、图形属性多样化的注解。我们只要为所有想要的图形属性设置好对应的值就可以了。如果我们需要添加多个具有类似属性的注解，将它们放到数据框中并一次添加完成也许更有效。下面的例子中，我们分别用以上两种方式，向经济数据中加入了有关美国总统的信息。

``` r
> (unemp <- qplot(date,unemploy,data = economics,geom ="line", xlab ="",ylab="No.unemployed (1000s)"))
```

![](chapter05_工具箱_files/figure-gfm/unnamed-chunk-18-1.png)<!-- -->

``` r
> presidential <- presidential[-(1:3),]
> 
> yrng <- range(economics$unemploy) 
> xrng <- range(economics$date)
> unemp + geom_vline(aes(xintercept = as.numeric(start)),data = presidential)
```

![](chapter05_工具箱_files/figure-gfm/unnamed-chunk-19-1.png)<!-- -->

``` r
> library(scales)
> unemp + geom_rect(aes(NULL,NULL,xmin = start,xmax = end, fill = party),ymin = yrng[1],ymax = yrng[2],
+                   data = presidential,alpha =0.2) + 
+   scale_fill_manual(values =c("blue","red"))
```

![](chapter05_工具箱_files/figure-gfm/unnamed-chunk-20-1.png)<!-- -->

``` r
> last_plot() + geom_text(aes(x = start,y = yrng[1],label = name), data = presidential,size = 3,
+                         hjust = 0,vjust = 0)
```

![](chapter05_工具箱_files/figure-gfm/unnamed-chunk-21-1.png)<!-- -->

``` r
> caption <- paste(strwrap("Unemployment rates in the US have varied a lot over the years",40),collapse="\n") 
> unemp + geom_text(aes(x,y,label = caption), 
+                   data = data.frame(x = xrng[2],y = yrng[2]), hjust = 1,vjust = 1,size = 4)
```

![](chapter05_工具箱_files/figure-gfm/unnamed-chunk-22-1.png)<!-- -->

``` r
> highest <- subset(economics,unemploy == max(unemploy)) 
> unemp + geom_point(data = highest, size = 3,colour = "red",alpha =0.5)
```

![](chapter05_工具箱_files/figure-gfm/unnamed-chunk-23-1.png)<!-- -->

- geom_text可添加文字叙述或为点添加标签。对于多数图形，为所有观测都添加标签是无益的。然而，（使用取子集的方式）抽取部分观测添加标签可能会非常有用一我们往往希望标注出离群点或其他重要的点。
- geom_vline，geom_hline：向图形添加垂直线或水平线。
- geom_abline：向图形添加任意斜率和截距的直线。
- geom_rect可强调图形中感兴趣的矩形区域。geom_rect拥有xmin，xmax，ymin和ymax几种图形属性。
- geom_line，geom_path和geom_segment都可以添加直线。所有这些几何对象都有一个arrow参数，可以用来在线上放置一个箭头。我们也可以使用`arrow()`函数绘制箭头，它拥有angle，length，ends以及type几个参数。

## 5.11 含权数据

- 在处理整合后的数据(aggregated
  data)时，数据集的每一行可能代表了多种观测值，此时我们需要以某种方式把权重变量考虑进去。这里以2000年美国人口普查中，中西部各州的统计数据为例。此数据中主要包含的是比例型数据(例如白种人比例、贫困线以下人口比例、有大学学历的人口比例和每个郡的基本信息（面积、人口总数、人口密度）。

- 有一些数据可能可以作为权重使用：

- 什么都不用，即直接观察郡的数量。

- 总人数，与原始的绝对数配合使用。

- 面积，用于研究地缘效应。

- 权重变量的不同将极大地影响图形内容以及观察结论。有两种可以用于表现权重的可调图形属性。首先，对于线和点这类简单的几何对象，我们可以根据点的数量调整图形属性size来改变点的大小，代码如下所示，结果见图5.18。

``` r
> qplot(percwhite,percbelowpoverty,data = midwest) 
```

![](chapter05_工具箱_files/figure-gfm/unnamed-chunk-24-1.png)<!-- -->

``` r
> qplot(percwhite,percbelowpoverty,data = midwest,
+       size = poptotal / 1e6) + scale_size_area("Population\n(millions)", breaks=c(0.5,1,2,4))
```

![](chapter05_工具箱_files/figure-gfm/unnamed-chunk-24-2.png)<!-- -->

``` r
> qplot(percwhite,percbelowpoverty,data=midwest,size = area) + scale_size_area()
```

![](chapter05_工具箱_files/figure-gfm/unnamed-chunk-24-3.png)<!-- -->

- 图5.18
  使用点的大小来展示权重：无权重（左图），以人口数量为权重（中图），以面积为权重（右图）。

- 对于更复杂的、涉及到统计变换的情况，我们通过修改weight图形属性来表现权重。这些权重将被传递给统计汇总计算函数。在权重有意义的情况下，各种元素基本都支持权重的设定，例如：各类平滑器、分位回归、箱线图、直方图以及各类密度图。我们无法直接看到这个权重变量，而且它也没有对应的图例，但它却会改变统计汇总的结果。图5.19显示了作为权重的人口密度如何影响了白种人比例和贫困线以下人口比例的关系。

``` r
> lm_smooth <- geom_smooth(method = lm,size =1)
> qplot(percwhite,percbelowpoverty,data = midwest) + lm_smooth 
```

![](chapter05_工具箱_files/figure-gfm/unnamed-chunk-25-1.png)<!-- -->

``` r
> qplot(percwhite,percbelowpoverty,data = midwest, weight = popdensity,size = popdensity) + lm_smooth
```

![](chapter05_工具箱_files/figure-gfm/unnamed-chunk-25-2.png)<!-- -->

- 图5.19
  未考虑权重的最优拟合曲线（左图）和以人口数量作为权重的最优拟合曲线（右图）。

- 在我们使用总人口作为权重去修改直方图或密度图的时候，我们的视角将从对郡数量分布的观察转向对人口数量分布的观察。图5.20以一幅贫困线以下人口比例的直方图，显示了这两种视角的不同之处。

``` r
> qplot(percbelowpoverty,data = midwest,binwidth =1) 
```

![](chapter05_工具箱_files/figure-gfm/unnamed-chunk-26-1.png)<!-- -->

``` r
> qplot(percbelowpoverty,data = midwest,weight = poptotal, binwidth =1) + ylab("population")
```

![](chapter05_工具箱_files/figure-gfm/unnamed-chunk-26-2.png)<!-- -->

- 图5.20
  不含权重信息（左侧）以及含权重信息（右侧）的直方图。不含权重信息的直方图展示了郡的数量，而含权重信息的直方图展示了人口数量。权重的加人的确极大地改变了对图形的解读！
