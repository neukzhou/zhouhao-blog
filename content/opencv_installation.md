title: Mac/Linux下安装openCV
date: 2014-03-19 20:20
category: 瞎鼓捣
tags: Sublime, openCV
author: ZhouHao
slug: config_sublime_to_work_with_opencv

*作者：ZhouHao 出处：http://www.zhouhao.me 欢迎转载，但也请保留这段声明。谢谢！*

一种非常简单的在Mac上配置Sublime使其可以导入openCV库的方法。

<!-- PELICAN_END_SUMMARY -->

## 安装openCV

### 1. Mac OS X

Mac上可以直接利用homebrew安装openCV及相关依赖：

	brew intsall homebrew/science/opencv
	
然后就可以在**/usr/local/Cellar/opencv/2.4.8.2/lib/pkgconfig/**下看到opencv的pkg-config配置文档opencv.pc。因此，可以通过pkg-config获得库，再用gcc编译链接。

	# 编译sample.c
	gcc -c `pkg-config --cflags glib-2.0` sample.c

	# 连接
	gcc sample.o -o sample `pkg-config --libs glib-2.0`
	
	# 编译和连接
	gcc sample.c -o sample `pkg-config --cflags --libs glib-2.0`
	
### 配置Sublime

打开Sublime，进入**Tools > Build System > New Build System**

复制以下代码：

	{
	 "cmd": ["g++", "-Wall", "-Wextra", "${file}", "-o", "${file_path}/${file_base_name}",
	 "-I/usr/local/Cellar/opencv/2.4.8.2/include/opencv",
	 "-I/usr/local/Cellar/opencv/2.4.8.2/include",
	 "/usr/local/Cellar/opencv/2.4.8.2/lib/libopencv_calib3d.dylib",
	 "/usr/local/Cellar/opencv/2.4.8.2/lib/libopencv_contrib.dylib",
	 "/usr/local/Cellar/opencv/2.4.8.2/lib/libopencv_core.dylib",
	 "/usr/local/Cellar/opencv/2.4.8.2/lib/libopencv_features2d.dylib",
	 "/usr/local/Cellar/opencv/2.4.8.2/lib/libopencv_flann.dylib",
	 "/usr/local/Cellar/opencv/2.4.8.2/lib/libopencv_gpu.dylib",
	 "/usr/local/Cellar/opencv/2.4.8.2/lib/libopencv_highgui.dylib",
	 "/usr/local/Cellar/opencv/2.4.8.2/lib/libopencv_imgproc.dylib",
	 "/usr/local/Cellar/opencv/2.4.8.2/lib/libopencv_legacy.dylib",
	 "/usr/local/Cellar/opencv/2.4.8.2/lib/libopencv_ml.dylib",
	 "/usr/local/Cellar/opencv/2.4.8.2/lib/libopencv_nonfree.dylib",
	 "/usr/local/Cellar/opencv/2.4.8.2/lib/libopencv_objdetect.dylib",
	 "/usr/local/Cellar/opencv/2.4.8.2/lib/libopencv_ocl.dylib",
	 "/usr/local/Cellar/opencv/2.4.8.2/lib/libopencv_photo.dylib",
	 "/usr/local/Cellar/opencv/2.4.8.2/lib/libopencv_stitching.dylib",
	 "/usr/local/Cellar/opencv/2.4.8.2/lib/libopencv_ts.dylib",
	 "/usr/local/Cellar/opencv/2.4.8.2/lib/libopencv_video.dylib",
	 "/usr/local/Cellar/opencv/2.4.8.2/lib/libopencv_videostab.dylib"],
	 "file_regex": "^(..[^:]*):([0-9]+):?([0-9]+)?:? (.*)$",
	 "working_dir": "${file_path}",
	 "selector": "source.c, source.c++",
 
	"variants":
	 [{
	"name": "Run",
	"cmd": ["bash", "-c", "g++ '${file}' -o '${file_path}/${file_base_name}' `/usr/bin/pkg-config --cflags --libs   /usr/Local/Cellar/opencv/2.4.8.2/lib/pkgconfig/opencv.pc` && '${file_path}/${file_base_name}' "]
	}]
	}
	
保存即可。

关于pkg-config的介绍，请见：  
[linux里命令pkg-config工具的使用](http://hi.baidu.com/3444542/item/a752144400cc4595833ae193)  
[pkg-config指南](http://blog.csdn.net/exbob/article/details/6991037)  
[Makefile好助手：pkgconfig](http://blog.csdn.net/absurd/article/details/599813)