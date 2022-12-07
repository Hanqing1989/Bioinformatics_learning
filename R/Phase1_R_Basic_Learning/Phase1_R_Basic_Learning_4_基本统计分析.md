R语言进阶学习（第二阶段）——基本统计分析
================

- <a href="#7-基本统计分析" id="toc-7-基本统计分析">7 基本统计分析</a>
  - <a href="#71-描述性统计分析" id="toc-71-描述性统计分析">7.1
    描述性统计分析</a>
    - <a href="#711-方法云集" id="toc-711-方法云集">7.1.1 方法云集</a>
    - <a href="#712-更多方法" id="toc-712-更多方法">7.1.2 更多方法</a>

Source：

1.  《R语言实战（中文第二版）》

2.  [【B站】从零开始学 R
    语言，带你玩转医学统计学](https://www.bilibili.com/video/BV1JU4y1f7zg/?spm_id_from=333.1007.top_right_bar_window_custom_collection.content.click&vd_source=fa22bae99c47db3f7bc43573bd9b3ed3)

# 7 基本统计分析

## 7.1 描述性统计分析

- 本节中，关注分析连续型变量的中心趋势、变化性和分布形状的方法。使用(mtcars)数据集，关注焦点是每加仑汽油行驶英里数(mpg)、马力(hp)和车重(wt)。

``` r
> myvars <- c("mpg", "hp", "wt")  
> head(mtcars[myvars])  # head()函数查看前六种车
                  mpg  hp  wt
Mazda RX4          21 110 2.6
Mazda RX4 Wag      21 110 2.9
Datsun 710         23  93 2.3
Hornet 4 Drive     21 110 3.2
Hornet Sportabout  19 175 3.4
Valiant            18 105 3.5
```

### 7.1.1 方法云集

- 代码清单7-1 通过`summary()`计算描述性统计量

``` r
> myvars <- c("mpg", "hp", "wt") 
> summary(mtcars[myvars])
      mpg           hp            wt     
 Min.   :10   Min.   : 52   Min.   :1.5  
 1st Qu.:15   1st Qu.: 96   1st Qu.:2.6  
 Median :19   Median :123   Median :3.3  
 Mean   :20   Mean   :147   Mean   :3.2  
 3rd Qu.:23   3rd Qu.:180   3rd Qu.:3.6  
 Max.   :34   Max.   :335   Max.   :5.4  
```

- `summary()`函数提供了最小值、最大值、四分位数和数值型变量的均值，以及因子向量和逻辑型向量的频数统计。

- `apply()`函数或`sapply()`函数计算所选择的任意描述性统计量。对于`sapply()`函数，其使用格式为：

<!-- -->

    sapply(x, FUN, options)

- 其中的x是数据框(或矩阵)，FUN为一个任意的函数。如果指定了options，它们将被传递给FUN。可以在这里插入的典型函数有`mean()`、`sd()`、`var()`、`min()`、`max()`、`median()`、`length()`、`range()`和`quantile()`。函数`fivenum()`可返回图基五数总括(Tukey’s
  five-number
  summary，即最小值、下四分位数、中位数、上四分位数和最大值)。

- 代码清单7-2 通过`sapply()`计算描述性统计量

``` r
> mystats <- function(x, na.omit=FALSE){         
+   if (na.omit)                     
+     x <- x[!is.na(x)]              
+   m <- mean(x)              
+   n <- length(x)            
+   s <- sd(x)               
+   skew <- sum((x-m)^3/s^3)/n       
+   kurt <- sum((x-m)^4/s^4)/n - 3          
+   return(c(n=n, mean=m, stdev=s, skew=skew, kurtosis=kurt))        
+   } 
> myvars <- c("mpg", "hp", "wt") 
> sapply(mtcars[myvars], mystats)
           mpg     hp     wt
n        32.00  32.00 32.000
mean     20.09 146.69  3.217
stdev     6.03  68.56  0.978
skew      0.61   0.73  0.423
kurtosis -0.37  -0.14 -0.023
```

- 对于样本中的车型，每加仑汽油行驶英里数的平均值为20.1，标准差为6.0。分布呈现右偏(偏度+0.61)，并且较正态分布稍平(峰度–0.37)。

- **注意，如果你只希望单纯地忽略缺失值，那么应当使用`sapply(mtcars[myvars], mystats, na.omit=TRUE)`。**

### 7.1.2 更多方法

- Hmisc、pastecs和psych包提供了计算描述性统计量的函数，在首次使用之前先进行安装。

- Hmisc包中的`describe()`函数可返回变量和观测的数量、缺失值和唯一值的数目、平均值、分位，以及五个最大的值和五个最小的值。

- 代码清单7-3 通过Hmisc包中的`describe()`函数计算描述性统计量

``` r
> library(Hmisc) 
> myvars <- c("mpg", "hp", "wt") 
> describe(mtcars[myvars])
mtcars[myvars] 

 3  Variables      32  Observations
--------------------------------------------------------------------------------
mpg 
       n  missing distinct     Info     Mean      Gmd      .05      .10 
      32        0       25    0.999    20.09    6.796    12.00    14.34 
     .25      .50      .75      .90      .95 
   15.43    19.20    22.80    30.09    31.30 

lowest : 10 13 14 15 15, highest: 26 27 30 32 34
--------------------------------------------------------------------------------
hp 
       n  missing distinct     Info     Mean      Gmd      .05      .10 
      32        0       22    0.997    146.7    77.04    63.65    66.00 
     .25      .50      .75      .90      .95 
   96.50   123.00   180.00   243.50   253.55 

lowest :  52  62  65  66  91, highest: 215 230 245 264 335
--------------------------------------------------------------------------------
wt 
       n  missing distinct     Info     Mean      Gmd      .05      .10 
      32        0       29    0.999    3.217    1.089    1.736    1.956 
     .25      .50      .75      .90      .95 
   2.581    3.325    3.610    4.048    5.293 

lowest : 1.5 1.6 1.8 1.9 2.1, highest: 3.8 4.1 5.2 5.3 5.4
--------------------------------------------------------------------------------
```
