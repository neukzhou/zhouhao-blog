title: 也谈建站(1)：基本的建站步骤
date: 2014-03-17 09:09
category: 瞎鼓捣
tags: 技术博客, Pelican
author: ZhouHao
slug: how_to_build_a_blog_1

*作者：ZhouHao 出处：http://www.zhouhao.me 欢迎转载，但也请保留这段声明。谢谢！*

身为小白的我，在[@高(wu)帅(jie)富(cao)][1]的耐心指导下，终于也把自己的小站建起来了。跟[@高(wu)帅(jie)富(cao)][1]不同，我更能理解小白用户的血泪史，因此我打算将自己的建站经历整理出来，主要目的当然是为了以后自己再建的时候有个参考，顺便算是给小白用户的福利吧。

好了，闲扯就此打住。

[1]: http://www.liupeiyang.com

<!-- PELICAN_END_SUMMARY -->
## 准备阶段

### 1. 安装pip包管理工具

mac自带的python包管理工具是easy_install，pip取代了easy_install。相较easy_install而言，pip的好处主要有：包下载后才进行安装（这避免了安装的部分完整性），错误消息会提供一些指引（比如指出依赖包、版本问题）这有利于问题的排查，可以很好地删除包等等。具体可以参考[stackoverflow上面的讨论][2]。

好了，理由讲清楚了，现在就该说说怎么安装pip包管理工具了。很简单，可以直接用easy_install安装它：

	easy_install pip
	
好了，pip应该顺利装好了，现在可以使用pip了。但是，默认的PYPI源在国内的速度不好，因此建议导入[清华的pypi源][3](教育网优先考虑)，或者[v2ex的源][4]。然后添加配置文件：

	cd ~/.pip/pip.conf
	
加入如下内容：

	[global]
	# 根据教育网非教育网选择上面的源加入
	index-url = http://pypi.tuna.tsinghua.edu.cn/simple/
	timeout = 6000
好了，pip的设置也大功告成。下面介绍一下pip和easy_install的常用语法。
easy_install:

	easy_install help
	easy_install [name]
	easy_install '[name[==version]]'
	easy_install -U [name]
	
pip:

	pip help
	pip install [name]
	pip install '[name[==version]]'
	pip install -U [name]
	pip uninstall [name]
	pip freeze
	pip search [keyword]
	pip show [name]

[2]: http://stackoverflow.com/questions/3220404/why-use-pip-over-easy-install
[3]: http://pypi.tuna.tsinghua.edu.cn/simple/
[4]: http://pypi.v2ex.com/simple/


### 2. 建立python虚拟环境

virtualenv可以用于提供纯净的python环境，相互独立、没有依赖关系，这可以解决库的版本、依赖和权限的问题。需要删除应用时可以直接将该环境和应用的文件夹删除即可。virtualenv可以理解为python环境的虚拟机，我觉得这对我来说简直就是福音。详细介绍请猛戳[这儿][5]

virtualenv的安装很简单，直接使用pip安装即可：

	pip install viretualenv
	
进入博客目录，并建立虚拟环境：

	cd blog
	virtualenv blogenv

激活虚拟环境：

	cd blogenv
	sourve bin/activate
	cd ..

好了，已经进入了blogenv的虚拟环境了，如果使用的时zsh，应该还会有(blogenv)的标识。


[5]: http://blogs.360.cn/blog/how-360-uses-python-1-virtualenv/

### 3. 安装Pelican和Markdown

Pelican是基于Python的静态博客生成器，此外还有基于Ruby的Jekyll，至于你问我为什么选择Pelican而不是Jekyll，那是因为——[@高(wu)帅(jie)富(cao)][1]他会Python而不会Ruby。

那么现在就需要安装Pelican和Markdown了：

	pip install pelican
	pip install markdown
	
建立博客的框架（记住进入之前的虚拟环境）：

	mkdir myblog
	cd myblog
	pelican-quickstart
	
根据提示设置配置项，注意Makefile一定要选yes。设置完毕将生成如下目录结构：

	myblog/  
	├── content              # 存放博文和相关内容
	│   └── (pages)          # 存放静态页面（比如关于）  
	├── output               # 生成的输出文件
	├── develop_server.sh    # 启动测试服务器的脚本文件
	├── Makefile             # make html必备的文件  
	├── pelicanconf.py       # 主配置文件
	└── publishconf.py       # 主发布文件，可删除

在myblog/content目录下写下你的第一篇博文吧：

	cd content
	touch test.md
	open test.md
	
写入以下内容，然后保存：

	Title: 测试
	Date: 2014-03-17 10:30
	Category: 测试
	Tags: test
	Slug: article_test
	Author: ZhouHao
	
	This is the body of an article.
	这是正文部分。

回到myblog文件夹，生成博客的html文件：

	cd ..
	make html
	
下面有两种方法启动博客，一种是通过执行develop_server.sh，一种是通过使用python下的SimpleHTTPServer。两者默认都是打开的8000端口。前一种方法的好处是会自动检测content中是否有新的内容加入自动刷新，但是经常中断后没有kill掉，还会占用8000端口，因此需要手动kill，且kill掉有时候要重新make html才行；后一种方法虽然不能自动更新内容，但是比较稳定。可以根据自己的需要选择相应的方法。

第一种方法（在myblog文件夹下执行）：
	
	./develop_server.sh start[/restsart/stop] [port]
	
第二种方法（在output文件夹下执行）：
	
	python -m SimpleHTTPServer

好了，博客已经生成完毕，可以打开<http://localhost:8000>看看生成的效果，下一部分将介绍博客的个性化定制的部分。

演示结果如下：

<img src="/static/img/blog1-1.png" title="博客生成结果" width="600" />