Title: Postfix邮件服务器的建立
Date: 2014-03-16 09:30
Category: 邮件服务器
Tags: 邮件, 邮件服务器, Postfix, Extmail, Webmail
Author: ZhouHao
Slug: postfix_extmail


*作者：ZhouHao 出处：http://www.zhouhao.me 欢迎转载，但也请保留这段声明。谢谢！*

本文介绍了基于Postfix+Extmail的邮件服务器的建立过程。
<!-- PELICAN_END_SUMMARY -->
系统：CentOS 6.5 x86_64  
软件源：EMOS－1.6为主

本教程基于[官方教程][-1]，许多步骤可以在其中找到。但是，[官方教程][-1]基于的系统版本（centos 5）和yum源版本（EMOS-1.5）都比较老了，因此有很多地方需要更新。此外，[官方教程][-1]中也存在很多地方的错误，这些在本文中都得到了更新。

[-1]: http://wiki.extmail.org/extmail_solution_for_centos-5 "email_soulution_for_centos-5"

** 文档中假设域名为：pris.cn，IP为：10.103.13.34  
若需要针对自己的域名进行设置，请将其修改为自己的域名 **

## 制作yum库
由于Extmail与很多软件包新版本的兼容性不好，因此需要加入Extmail官方提供的yum库，同时库中未包含的包再通过默认yum源安装。**由于官方未给出新版本的在线yum源，建议使用下载好的iso包建立本地yum源。**下载地址为：[EMOS-1.6][0]，建议使用迅雷等加速器下载。  
注意：EMOS-1.6目前只推出了64位版本，只能用于64位系统。如需在32位系统上实现，请下载EMOS-1.5 i386版本。

[0]: http://mirror.extmail.org/iso/emos/EMOS_1.6_x86_64.iso "EMOS-1.6官方下载地址"

### 1. 下载软件包
	$ su - root
	# mkdir /root/rpm
	# cd /root/rpm
	# wget http://mirror.extmail.org/iso/emos/EMOS_1.6_x86_64.iso

### 2. 建立本地yum库
建立iso包的映射  

	# yum install createrepo
	# mkdir /mnt/EMOS
	# mount -o loop /root/rpm/EMOS_1.6_x86_64.iso /mnt/EMOS
	# cd /mnt
	# createrepo .

### 3. 建立本地yum库文件
	# cd /etc/yum/repos.d
	# mkdir backup
	# mv *.repo ./backup
	# vim EMOS.repo
加入如下内容：

```
[EMOS]
 name=EMOS
 baseurl=file:///mnt/
 enabled=1
 gpgcheck=0
```

之后若需要使用官方yum源只需如下操作：

	# mv /etc/yum/repos.d/backup/*.repo /etc/yum/repos.d/

更新一下yum库的信息：

	# yum clean all
	# yum list

## 配置MTA：Postfix
### 1. 安装Postfix
因为本地Postfix要求低版本的mysql和mysql-libs，因此安装前需要先把高版本卸载：

	# yum remove postfix mysql mysql-libs
	# yum install postfix


	# mv /etc/postfix/main.cf /etc/postfix/main.cf.bak # mv /etc/postfix/main2.cf /etc/postfix/main.cf

加入如下内容：

```
# 注意下方的网络号需要改成当前服务器所在的网络号。
mydestination = $mynetworks, $myhostname
smtpd_banner = $myhostname, ESMTP, $mail_name
message_size_limit = 5242880
mailbox_size_limit = 5242880
show_user_unknown_table_name = no
bounce_queue_lifetime = 1d
maximal_queue_lifetime = 1d
```


## 配置Courier-AuthLib
### 1. 安装courier-authlib

	# yum install courier-authlib
	# yum install courier-authlib-mysql
	
删除并新建authmysqlrc：

	# rm /etc/authlib/authmysqlrc
	# vim /etc/authlib/authmysqlrc
	
加入以下内容：

```
MYSQL_SERVER            localhost
# 如果需要修改原始用户名和密码，请修改下面两项
```

修改authdaemonrc：

	# vim /etc/authlib/authdaemonrc
	
修改以下内容：

```
authmodulelist="authmysql"
```

### 2. 启动courier-authlib

	＃ service courier-authlib start
	
如启动正常将返回如下信息：  

> Starting Courier authentication services: authdaemond

修改authdaemonrc socket权限，以保证maildrop和postfix访问的正确性：

	# chmod 755 /var/spool/authdaemon/
	
## 配置Maildrop
### 1. 安装maildrop

	# yum install maildrop
	
修改master.cf以保证Postfix支持maildrop。在master.cf中找到maildrop的信息，注销掉之前的内容，改成如下内容：

```
maildrop   unix        -       n        n        -        -        pipe
```

其中flags前面必须保留两个（或以上）空格，以表示其是上一行的延续，且与上一个参数pipe是不同参数。  
maildrop的更多配置请参阅[maildrop官方文档][1]，master.cf的具体作用和配置方法请参阅[master.cf官方文档][2]。

[1]: http://www.postfix.org/MAILDROP_README.html "maildrop_README"
[2]: http://www.postfix.org/master.5.html "master.cf"

由于maildrop不支持一次接收多个收件人，因此需要在main.cf中添加如下约束：

	＃ maildrop_destination_recipient_limit = 1

### 2. 测试maildrop对authlib的支持

	# maildrop -v

如果显示如下，则表示支持正常：

> maildrop 2.1.0 Copyright 1998-2005 Double Precision, Inc.  




NameVirtualHost *:80
Include conf/vhost_*.conf




# VirtualHost for ExtMail Solution
# 请根据自己的服务器设置


	# service httpd start
	# chkconfig httpd on

## 配置Extmail
### 1. 安装Extmail

	# yum install extsuite-webmail
	
### 2. 配置Extmail

	# cd /var/www/extsuite/extmail
	# cp webmail.cf.default webmail.cf
	# vim webmail.cf
	
修改如下内容：  

```
# 以下两项根据之前设置的mysql账户密码修改
SYS_MYSQL_USER = extmail
```

授权给extmail，否则会报Permission denied错误：

	# chown -R vuser:vgroup /var/www/extsuite/extmail/cgi/
	
## 配置管理后台Extman
### 1. 安装Extmail

	# yum install extsuite-webman
	
同样进行授权：

	# chown -R vuser:vgroup /var/www/extsuite/extman/cgi/
	
创建邮件存放目录：

	# mkdir /tmp/extman
	# chown -R vuser:vgroup /tmp/extman

这里说明以下，tmp目录在RedHat和CentOS系统中会定期清理（由相应daemon执行），因此，如要确保邮件不丢失，请修改此目录的路径，同时在main.cf中进行相应修改。当然，最好的保护方式还是`备份`。

### 2. 数据库初始化
启动MySQL

	# yum install mysql*
	# service mysqld start
	# chkconfig mysqld on
	
导入mysql数据结构，密码可自行设置：

	# mysql -u root -p < /var/www/extsuite/extman/docs/extmail.sql
	# vim /var/www/extsuite/extman/docs/init.sql

将里面所有的extmail.org都修改成你需要的域名，这是初始化文件，包括root账户和postmaster账户的初始化，其中**root**账户的初始密码为**Extmail\*123\***，**postmaster**初始密码为**extmail**。  
导入mysql初始化数据结构：

	# mysql -u root -p < /var/www/extsuite/extman/docs/init.sql
	
### 3. 设置虚拟域和虚拟用户配置文件

	# cd /var/www/extsuite/extman/docs
	# cp mysql_virtual_*.cf /etc/postfix/

配置main.cf，在其最后加入如下内容：

```
# extmail配置
```

启动postfix：

	# service postfix start
	
### 4. 测试authlib
建立刚才导入mysql的postmaster@pris.cn账号的Maildir格式邮件存储路径。关于mailbox和Maildir两种邮箱格式的讨论请见[Comments on mailbox vs. Maildir][3]。

[3]: http://www.linuxmail.info/mbox-maildir-mail-storage-formats/ "mailbox vs. Maildir"

	# cd /var/www/extsuite/extman/tools
	# ./maildirmake.pl /home/domains/pris.cn/postmaster/Maildir
	# chown -R vuser:vgroup /home/domains/pris.cn
	
执行 authtest(如果失败,尝试 find –name authtest,找到绝对地址再试):

	# /usr/sbin/authtest -s login postmaster@pris.cn extmail

显示结果如下则表面extman安装正确。courier-authlib也可正确连接到mysql数据库中：

> Authentication succeeded.
> Quota: 104857600S






Cyrus－Sasl主要是支持SMTP协议传输的组件。
安装EMOS库中支持authdaemon的包(如果装不上就把之前官方的几个 yum 源包括进来)

	# yum install cyrus-sasl
	
### 2. 配置main.cf
	
	# vim /etc/postfix/main.cf
	
添加以下内容：

```
# smtpd related config
```

### 3. 配置smtpd
新建smtpd，32位系统请将lib64换成lib：

	# rm /usr/lib64/sasl2/smtpd.conf
	# vim /usr/lib64/sasl2/smtpd.conf
	
写入如下内容：

```
pwcheck_method: authdaemond
```



通过以下命令获得postmaster@pris.cn的用户名及密码的MIMEBase64编码：

	# perl -e 'use MIME::Base64; print encode_base64("postmaster\@pris.cn")'

结果为：  

> cG9zdG1hc3RlckBwcmlzLmNu

	

结果为：






334 VXNlcm5hbWU6  
235 2.0.0 Authentication successful  







	# vim /usr/lib/courier-imap/etc/imapd
	
关闭IMAP：

```
IMAPDSTART=NO
```

	# vim /usr/lib/courier-imap/etc/imapd-ssl
	
关闭IMAPSSL：

	IMAPDSSLSTART=NO
	
重启courier-imap:

	# service courier-imap restart
	
### 3. 测试POP3
	# telent localhost 110
过程如下：

> Trying 127.0.0.1...  
OK Hello there.  
OK Password required.  
+OK logged in.  
OK POP3 clients that break here, they violate STD53.  
OK Bye-bye.  

## 补充
### 1. 在Extmail上显示所需域名
登录Extmail，因为使用IP访问，所以域名老是显示为IP，而非默认域名，登录起来每次都需要修改且无法完成注册功能。现在解决这个问题，让Webmail默认显示域名，方法如下：

	#vim /var/www/extsuite/extmail/html/default/index.html
	
找到并添加Value值：

```
 INPUT TYPE="text" class="input_n" NAME="domain" Value="pris.cn"
```

添加带框的内容即可。**事实上，所有登录界面中的元素都可以在这个文件中修改。**

### 2. 去除登陆时验证码
如果在测试阶段可以先将登录验证码去掉，否则某次都要输入，十分麻烦。修改方法如下：

	vim /var/www/extsuite/extman/webman.cf
	
修改下面的参数即可：

```
SYS_CAPTCHA_ON = 0
```