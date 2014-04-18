title: 也谈建站(2)：关于主题和插件
date: 2014-03-17 12:19
category: 瞎鼓捣
tags: 技术博客, Pelican
author: ZhouHao
slug: how_to_build_a_blog_2

*作者：ZhouHao 出处：http://www.zhouhao.me 欢迎转载，但也请保留这段声明。谢谢！*

上回谈到了如何建立自己的站点，相信按照步骤完成就已经能够看到一个有一篇测试文章的站点了。但是从效果图来看，那个站点还略显单调。因此我希望这个博客也能像QQ一样换主题，我也希望能够自己定制一些必要的插件，比如评论功能，比如微博显示。这里就需要介绍pelican-themes和pelican-plogins这两个git包了，并且将会介绍一些需要注意到的细节。
<!-- PELICAN_END_SUMMARY -->

## 定制主题

### 1. 下载pelican-themes包

首先从github上吧pelican-themes包下载下来：
	
	git clone https://github.com/getpelican/pelican-themes.git
	cd pelican-themes
	
进入pelican_themes文件夹中后，可以依次尝试所有的主题再做决定，只需要将文件夹名（包括路径）加入pelicanconf.py的参数里就可以了，比如：

	THEME = 'pelican-bootstrap3'

然后make html，就可以查看主题的效果了。

当然，每个主题都在其文件夹中提供了screenshot.png文件以供查看。如果你觉得不够直观，可以从别的开源博客中将content文件夹拷贝到自己的博客中的content文件夹里，这样就可以直观地看主题的效果了。


### 2. 挑选主题

pelican-themes中的主题基本都具有一定的可定制性，这个主要是在主题文件夹下的Template文件夹中选择。当然，选择好了需要的组件，还需要在pelicanconf.py中进行相应的设置才能使用。

由于pelican-themes使用的是Jinja2语言，这里就主题中所使用到的内容稍作介绍。

Jinja是基于Python的模版引擎，可类比Ruby的Liquid、PHP的Smarty。Jinja2要求Python2.4以上的版本。

在Jinja中，以下内容表示一个程序块，其中写语句，比如if语句、for语句：

	{% for user in users %}{% endif %}
	{% if sidebar %}{% endfor %}
	# 以下表示一个title块，要使用的时候子模板会嵌入title中
	{% block title %}{% endblock %}
	
以下内容表示一个变量：

	{{ COMPUTERS }}

以下内容代表注释，并不在程序中起作用：

	{# This is a line of comment #}
	
例如(archives.html)：

	{% extends "base.html" %}
	{% block title %}Archives - {{ SITENAME }}{% endblock %}
	{% block breadcrumbs %}
    	{% if DISPLAY_BREADCRUMBS %}
    	<ol class="breadcrumb">
        	<li><a href="{{ SITEURL }}" title="{{ SITENAME }}"><i class="fa fa-home fa-lg"></i></a></li>
        	<li class="active">Archives</li>
    	</ol>
    	{% endif %}
	{% endblock %}

	{% block content %}
		<section id="content">
        	<h1>Archives for {{ SITENAME }}</h1>

        	<dl>
            	{% for article in dates %}
                	<dt>{{ article.locale_date }}</dt>
                	<dd><a href='{{ SITEURL }}/{{ article.url }}'>{{ article.title }}</a></dd>
            	{% endfor %}
        	</dl>
    	</section>
	{% endblock %}

介绍完语法之后，就到了如何配置pelicanconf.py让组件显示出来的问题了。（如果上面的内容不够清楚，未来我会基于一个主题完整地介绍Jinja的内容。）

要让组件显示出来很简单，就拿刚刚提到的breadcrumbs来说，只需在pelicanconf.py中添加一句
	
	DISPLAY_BREADCRUMBS = True
	
保存之后make html，然后重启8000端口即可看到效果。

好了，从上面可以看出来pelicanconf.py和主题中Templates文件夹下各html文件之间的关系了。我们可以认为：

> 各个html文件提供了接口(一般都是条件接口，如{% if DISPLAY_BREADCRUMBS %})，pelicanconf.py控制这些条件是否成立(甚至有时候可以赋不同的值)，从而调用接口。

那么，对于Templates中的条件语句，都可以尝试在pelicanconf.py中对其操作，然后看看效果，最终选出最喜欢的效果。

此外，bootstrap还提供了多种配色方案，这些都可以在./static/css/文件夹下找到。要尝试不同的配色方案，只需在pelicanconf.py中写入以下参数(以bootstrap.amelia.min.css为例)：

	BOOTSTRAP_THEME = 'amelia'

### 3. 个性化定制网页元素

个性化定制主要是修改相应地css文件，Google Chrome浏览器提供了一个非常好地开发工具。进入Chrome后点击`cmd+option+i`(在Windows下是ctrl+alt+i)，然后选择弹出框中左上角放大镜，之后鼠标移到页面中就可以选择相应地元素，选择后点击在弹出框右侧可以选择相应地元素进行修改，此后点击所改元素css文件，将其修改的部分复制到自己本地地css中即可。

<img src="/static/img/Chrome.png" title="开发者模式" width="600" />

## 定制插件

**第三方评论系统**

在Disqus上申请一个站点，拷贝shortname（就是自己的id）。 在pelicanconf.py添加：
	
	DISQUS_SITENAME = shortname
	
如果国外站点不稳定可以考虑国内的[多说][4-1]


**sitemap**

在pelicanconf.py中加入如下内容：

	PLUGIN_PATH = u"pelican-plugins"
	PLUGINS = ["sitemap"]
	SITEMAP = {
    	"format": "xml",
    	"priorities": {
        	"articles": 0.7,
        	"indexes": 0.5,
        	"pages": 0.3,
    	},
    	"changefreqs": {
        	"articles": "monthly",
        	"indexes": "daily",
        	"pages": "monthly",
    	}
	}

*注意：以下需要首先拥有一个域名。*
	
**Google Analysis**

在Google Analytics申请账号，复制ID添加到pelicanconf.py中：

	GOOGLE_ANALYTICS = YOUR_ID


**Google Webmasters**

直接在[Google Webmasters][4-2]上注册就可以了。

[4-1]: http://duoshuo.com/
[4-2]: http://www.google.com/webmasters

## 发布到GitHub/GitCafé上

首先本地设置git的用户名和邮箱：

	git config --global user.name 'your_name'
	git config --global user.email 'your_mail@domain'
	
然后创建本地的SSH Key：

	ssh-keygen -t rsa -C "*******@gmail.com" -f ~/.ssh/gitcafe/
	

打开公钥文件：

	vim ~/.ssh/gitcafe/id_rsa.pub

登录GitHub或GitCafé，选择`账户设置-SSH公钥管理-添加新的公钥`，填入名称，然后将id_rsa.pub中所有内容复制到公钥中，保存就完成了。之后新建一个与用户名一样的项目。

之后就可以将本地文件传到项目中了，按如下步骤：

	# 进入静态页面输出目录  
	cd output

	# 初始化 git 仓库  
	git init

	# 创建一个gitcafe-pages的分支，并切换到该分支  
	git checkout -b gitcafe-pages

	# 添加所有文件  
	git add .

	# 提交  
	git commit -m "init"

	# 添加远程仓库  
	git remote add origin git@gitcafe.com:your_name/your_name.git

	# push 到 GitCafé 仓库  
	git push -u origin gitcafe-pages

## 申请独立域名

最后，只需要在[Godaddy][6-1]购买你所喜欢的域名并按照提示配置A(host)即可。PS：GoDaddy第一年购买有优惠，只要60+～～～

[6-1]: https://www.godaddy.com/