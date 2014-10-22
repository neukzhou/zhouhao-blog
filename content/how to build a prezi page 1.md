title: 如何制作一个Prezi式的页面(1)：基本的滑动窗口
date: 2014-04-19 10:09
category: 瞎鼓捣
tags: Prezi, HTML5, jQuery, CSS
author: ZhouHao
slug: how_to_build_a_prezi_page_1

*作者：ZhouHao 出处：http://www.zhouhao.me 欢迎转载，但也请保留这段声明。谢谢！*

最近有人给我推荐了一个[**基于css3的prezi页面**](http://bartaz.github.com/impress.js)，看了以后让人心潮澎湃。于是，我也用**Bartaz**的GitHub上的[**impress.js**](https://github.com/bartaz/impress.js.git)自己做了一个博客的[**about页面**](http://www.zhouhao.me/about.htm)。

本系列的文章将会逐步讲解about页面的制作过程。从利用impress-demo.css到根据需要自己编写css，从利用impress.js到自己改进js文件。

目前我的about页面还基本是使用的**Bartaz**提供的impress.js，随着文档的推进，我也将试着编写自己的impress.js。

这部分的内容是在页面上实现滑动的窗口，以及不同外观的窗口（如Zsh）。
<!-- PELICAN_END_SUMMARY -->

**注意：**
本部分最终的页面可以在[**这里**](http://www.zhouhao.me/demo1.htm)查看。文件可以在[**demo1.zip**](http://www.zhouhao.me/static/extra/demo1.zip)打包下载。

## 放置页面

### 1. 二维页面

放置二维的页面很简单，只需要重写下面这一段代码即可

	<div class="step slide" data-x="页面x方向的位置" data-y="页面y方向的位置">
        <q>
        	你的内容应该写在这个位置
        </q>
    </div>

其中，类型step是指页面的统一模型，所有页面将共用step类型。类型slide表示具体的页面类型，在这里就是我们可以滑动的窗口类型。data-x和data-y就像是坐标轴上的坐标一样，规定了不同页面的位置。具体的位置你可以任意尝试，但是必须要提醒你，**一个slide的长和宽都是1000px**。

按照上面的设置以后就可以得到一个滑动窗口的页面了，如下：

<img src="/static/img/prezi_1-1.png" title="博客生成结果" width="600" />

对了，如果你需要首先看到某一个页面，就在该页面的div中添加一个`id="step-1"`作为入口。

好了，很简单吧！下面你可以根据自己的需要添加不同的页面了。不知道你注意到没有，按空格键页面出现的顺序就跟你html文件中代码的顺序是一样的。

### 2. 添加概览页面

impress.js里面还定义了可以查看整体概览的页面，它的id是overview，你只需要复制下面的代码就可以了：

	<div id="overview" class="step" data-x="页面x方向的位置" data-y="页面y方向的位置" data-scale="3">
    </div>

上面的data-x和data-y可以随自己需要修改，如果需要将所有slide页面显示在浏览器中心，那么分别设置x和y是最左最右、最上最下页面x、y的平均值即可。

注意一下，这里出现了新的属性`data-scale`，它对应overview页面的视觉尺度，就是相对于slide页面的缩放大小。你可以调整它的大小看看有什么效果。经过我的测试，对于一个2*4的页面，它取到三最合适。

添加完成以后，你可以按几次空格键找找概览页面在哪里。不出意外的话，你将得到下面的显示：

<img src="/static/img/prezi_1-2.png" title="博客生成结果" width="600" />

### 2. 三维页面

impress.js提供三维页面的支持，就比如上面图片中第三个页面，它的代码如下：

	<div class="step slide" data-x="2000" data-y="-1500" data-rotate-x="-30" data-rotate-y="10" data-rotate-y="10">
        <q>还是——</q><br/>
        <q>你喜欢<b style="color:red">三维</b>的<strong>感觉</strong>~<br><br>
        </q>
    </div>

很明显，data-rotate-x/y/z就表示的时三个维度的旋转角度。在这里还可以补充一点，之前没有提到data-z。它是表示页面的纵深位置的，有兴趣也可以尝试。

## 自定义页面

相信可以发现，上面的图中出现了一个伪geek的页面。它看上去很像一个Linux中的终端。这是我自己定义的一个页面，格式存在demo.css文件中的#terminal里。代码如下：
	
	/*
		下面定义了终端的基本元素，有长宽，还有上下、左右的文本边界。还定义了背景颜色和透明度。
	*/
	#terminal {
    display: block;

    width: 900px;
    height: 700px;
    padding: 40px 60px;

    background-color: rgb(58, 58, 58);
    border: 1px solid rgba(0, 0, 0, .3);
    border-radius: 10px;
    box-shadow: 0 2px 6px rgba(0, 0, 0, .1);

    font-family: "Courier New", Courier, monospace;
    font-size: 30px;
    line-height: 36px;
    letter-spacing: -1px;
	}
	
	/*
		主要是定义了文本的默认颜色还有一些字体的属性。white-space: pre-wrap极大的方便了内容的输入。
	*/
	#terminal q {
    display: block;
    font-size: 35px;
    line-height: 45px;
    margin-top: 50px;
    white-space: pre-wrap;
    color: rgb(187, 187, 187);
	}
	
	/* 命令行中的提示符是粗体且不换行。 */
	#terminal q b {
    white-space: nowrap;
	}

html代码如下：

	<div id="terminal" class="step" data-x="3000" data-y="-1500" data-z="0" data-rotate-x="0" data-rotate-y="0" data-scale="1">
        <q><b style="color:rgb(85, 255, 85);">zhouhao@BUPT </b><b style="color:rgb(85, 85, 255);">~ $</b> man zhouhao

	<strong>Name:</strong>       周昊
	<strong>Address:</strong>    BUPT, Beijing, China
	<strong>Website:</strong>    http://www.zhouhao.me
	<strong>Interests:</strong>  Mathematics, Computer Vision, Linux and Python
	<strong>Likes:</strong>      Eating without cooking, keeping fit without sweating and googling without frequently asking
	<strong>Socials:</strong>    GitHub, Stack Overflow, V2EX, indie blogs
            </q>
    </div>

注意一下其中的颜色的取值。

下面你也可以自定义自己的页面了。本部分最终的页面可以在[这里](http://www.zhouhao.me/demo1.htm)查看。

文件可以在[demo1.zip](http://www.zhouhao.me/static/extra/demo1.zip)打包下载。