title: 专注写作：Markdown介绍
date: 2014-03-19 20:20
category: 瞎鼓捣
tags: Markdown, Mou, 写作
author: ZhouHao
slug: intro_to_markdown

*作者：ZhouHao 出处：http://www.zhouhao.me 欢迎转载，但也请保留这段声明。谢谢！*

当你在使用Office Word编辑文档的时候，肯定会需要调整字体的大小。对于老手，可能知道用版式来进行调整，使得整体布局有层次化；但对于很多经验不足的人，可能仅仅是通过改变字号来实现这一功能。还有时候，我们需要输入一组公式，那Word带来的体验不可谓不糟糕了。即便在Word 2007后的内置公式编辑器可以通过一些快捷键来帮助（要是你还不知道，赶紧点[这儿][1]，省时又省力），但整体来说，很多大型公式的输入还是很不方便。当然会有人说，有Mathtype神器支持LaTeX公式输入。但我想，疯狂点击ctrl+s估计也是难忘的回忆吧。

那于是，在很多的论坛都可以看到各种大神介绍LaTeX，感觉一式在手，天下我有。但是，当我打开LaTeX的Mannual的时候，我决定还是继续使用Word了。原因在于，LaTeX提供的内容太全面了，每个细节都有相应的语法，而且即使在你创作的时候，还要不时注意这里是不是用到了一个特殊字符、那里是不是需要新加一个package。当在整理自己的思路的同时还需要分出一条进程来完成排版的工作，我实在无法做到。

当然，Word仍然是一款在写作和排版中取得最好平衡的一款软件。而LaTeX排版的定制程度最高。当常常我们会遇到一个这样的问题，也许：

> 我只是在写一份文档、一篇博客，或者只是记录自己的想法，我并不需要一个多么绚丽的版面，我只是需要分层次、简单地表达我地观点。

如果你也有这样的目的，那么Markdown绝对是你“不二“的选择。选择Markdown，拒绝犯二。

[1]:http://office.microsoft.com/en-us/word-help/linear-format-equations-and-math-autocorrect-in-word-2010-HA101861025.aspx

<img src="/static/img/md1.png" title="Mou界面" width="600" />


<!-- PELICAN_END_SUMMARY -->

## 基本语法

Markdown，可以算作轻型的标记语言。所谓“轻型”，就是语法很简单。而Markdown可以称作基本了，他的语法就像我们做笔记时用的一些简单的记号。比如你想加粗一句话，就直接用`**`放在这句话两侧就可以了，比如

> \*\*这句话会加粗显示\*\*
	
显示结果如下：

> **这句话会加粗显示**

是不是很简单！

不仅这样，Markdown的语法可以用800个字就介绍完毕（在Mou中）。而且大部分Markdown编辑器都支持`即写即看`，你在一边编写的时候，显示的结果就会完整展现出来。

好了，你肯定会问Markdown有哪些语法。我只好告诉你，我不会在这里介绍它的语法，因为实在是太(mei)简(yu)单(fa)啊！如果你一定要看看有多简单，[这里][2]是一个在线的markdown编辑器，左侧是输入内容，右侧是输出内容，上下滚动会同步显示。

你绝对会为它的简单而惊讶！

[2]: https://www.zybuluo.com/mdeditor?url=https://www.zybuluo.com/static/editor/md-help.markdown

## Markdown与LaTeX

最初的Markdown版本，并不支持LaTeX中的数学公式。但是，现在很多的版本已经实现支持了。这意味着，你若是只想写一份文档与小伙伴们分享，并不需要那么正式的版面，Markdown绝对是最佳的选择。下面的这个公式就是由Markdown编写得到：

$$\frac{df(x)}{dt}=lim_{x \to 0}{\frac{f(x+h)-f(x)}{h}}$$

关于LaTeX的数学公式，参见：[LaTeX/数学公式][3]

[3]: http://zh.wikibooks.org/zh-cn/LaTeX/%E6%95%B0%E5%AD%A6%E5%85%AC%E5%BC%8F

## Markdown的局限与解决办法

一个如此简单地语言，不可能完备地代替其他的语言。Markdown还有很多目前无法解决的问题，比如字体。但是，好在排版也符合2/8原则，只需要少数的功能就能涵盖日常大部分的需要。

因此，在此我想指出Markdown语言能做的，然后再说明如果碰到不能实现的，如何寻找折中的方法。

### 1. Markdown能做的

- 分级的标题
- 加粗、斜体
- 插入链接、图片、表格
- 有序或无序的列表
- 代码表示和引用
- 公式
- 以及`这篇文章展示的所有效果`，因为这篇文章就是使用Markdown编写的

### 2. Markdown不能做的

- 复杂的排版
- 要求正式文体的场合
- ...

还有很多很多。还是那句话，Markdown无法支持所有的排版要求，它只适合想法的分享。

### 3. 可行的解决办法

如果你只是需要brainstorming，并不需要严格的版式，但你恰好又没在Markdown的语法中找到合适的语法，那该怎么办？

不用急，办法还是有的。

Markdown是基于HTML语言编写的，换句话说就是：

> 它支持所有的HTML语法。

如果你只是需要添加一个小的功能，而Markdown又不具有，那不妨考虑一下用简单的HTML语言替代。

比如，如果你发现一张图片插入进来以后特别大，显得特别突兀，那么你可以查找HTML语言中插入图片的语法：

	<img src="PATH" title="you_image_title" width="600" />

上面的语句可以在不改变图片长宽比的情况下将宽度设置为600。

同样地，如果以后碰到这种小问题，也可以采用上面简单的办法。

## Markdown编辑器推荐

Mou，只此一家别无分店。
界面如下：

<img src="/static/img/md2.png" title="Mou界面" width="600" />

## Markdown的格式转换

如果需要严格的格式，但又希望能够专注写作，这里还有一个折中的方法——先在Markdown下完成文稿，然后将文稿转换成其他格式再调整排版。

Pandoc就是这样一种工具，它可以实现markdown、docx、tex等各种主流文本格式之间的转换，并且保证格式的适配。

### 1. Pandoc的安装

Pandoc的安装十分简单，就跟一般的程序一样，在[官网][4]选择对应平台下载安装即可。

[4]: http://johnmacfarlane.net/pandoc/installing.html

### 2. Pandoc编辑器

一切操作都可以在Shell中实现。不过，Pandoc社区也提供基于已有编辑器的插件。

我主要使用的是Sublime Text 2。

安装插件方式也很简单，首先打开Sublime Text 2的Installed Plugins文件夹，下载官方的Package Control包：

	cd ~/Library/Application\ Support/Sublime\ Text\ 2/Installed\ Packages
	wget https://sublime.wbond.net/Package%20Control.sublime-package
	
然后下载GitHub上的SublimePandoc插件方能够在Package文件夹中：

	cd ~/Library/Application\ Support/Sublime\ Text\ 2/Packages
	git clone git://github.com/jclement/SublimePandoc.git
	
重启Sublime Text 2即可。

更多编辑器、插件请参考：[Pandoc-Extras][5]

[5]: https://github.com/jgm/pandoc/wiki/Pandoc-Extras