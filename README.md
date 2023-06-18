

========

## 开始

请将kbengine_demos_assets整个文件夹放置于服务端引擎根目录中，通常是这样:

![demo_configure](http://kbengine.github.io/assets/img/screenshots/demo_copy_kbengine.jpg)


## 启动服务端

使用固定参数来启动：(参数的意义:http://www.kbengine.org/cn/docs/startup_shutdown.html)
	
	首先进入对应的资产库kbengine/kbengine_demos_assets目录中，然后在命令行执行如下命令：

	Linux:
		start_server.sh

	Windows:
		start_server.bat


## 关闭服务端

快速杀死服务端进程:

	首先进入对应的资产库kbengine/kbengine_demos_assets目录中，然后在命令行执行如下命令： 

	Linux:
		kill_server.sh

	Windows:
		kill_server.bat


	(注意：如果是正式运营环境，应该使用安全的关闭方式，这种方式能够确保数据安全的存档，安全的告诉用户下线等等)

	Linux:
		safe_kill.sh

	Windows:
		safe_kill.bat


## 直接从代码定义实体（不需要def文件）

https://github.com/kbengine/kbengine_demos_assets/tree/py_entity_def