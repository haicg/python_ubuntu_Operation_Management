# python_ubuntu_Operation_Management
Ubuntu  系统管理脚本（python）
=============================

Ubuntu system Operation and Maintenance Management with Python
主要用python和shell语言来编写脚本管理和维护Ubuntu 系统。
<ol>
<li><h2>auto_mount_ntfs.py :用于将NTFS的分区自动挂载到/media文件夹下 </h2></li>
请使用root权限来执行该程序  sudo ./auto_mount_ntfs.py
<li><h2> stardict_offline_dict_install.sh : 用于安装stardict 的本地词库</h2></li>
使用方法：
第一步：先到对应的网站下载需要的词库，下面给出一些下载链接:</br>
http://pan.baidu.com/s/138Hx8 -包含三个词库：金山、牛津双解、Etymonline<br/>
其他的下载网站有：http://abloz.com/huzheng/stardict-dic/dict.org/
和http://abloz.com/huzheng/stardict-dic/
<br/>
第二步：解压下载下来的离线包，到dict 目录，可以手动创建，也可以直接运行脚本，会自动生成dict目录。
解压的命令是“tar -zxvf xxx -C dict”

第三步：运行脚本将dict下的文件复制到/usr/share/stardict/dic目录下，这个不需要手动复制。
</br>
说明：如果怕麻烦，可以直接运行脚本，会帮你安装一个金山和Etymonline. </br>




<ol>
