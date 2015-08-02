#!/bin/bash
#词典的下载链接：http://pan.baidu.com/s/138Hx8
#请用浏览器下载，里面主要有三个常用的字典：金山、牛津双解、Etymonline
#其他的下载网站有：http://abloz.com/huzheng/stardict-dic/dict.org/
#和http://abloz.com/huzheng/stardict-dic/
#将下载好的离线安装包解压到本程序生成的dict文件夹下，
#也可以自己手动创建dict
#然后再运行本脚本，本脚本会讲dict目录下所有的词典文件都复制到/usr/share/stardict/dic目录下
if [ ! -e stardict-powerword2011_1_900-2.4.2.tar.bz2 ];
then
    wget http://abloz.com/huzheng/stardict-dic/PowerWord/2011/stardict-powerword2011_1_900-2.4.2.tar.bz2
fi

if [ ! -e stardict-cedict-gb-2.4.2.tar.bz2 ]
then
    wget http://abloz.com/huzheng/stardict-dic/zh_CN/stardict-cedict-gb-2.4.2.tar.bz2
fi


if [ ! -d dict ]
then
    mkdir dict
fi
tar -jxvf "stardict-powerword2011_1_900-2.4.2.tar.bz2" -C dict
tar -jxvf "stardict-cedict-gb-2.4.2.tar.bz2" -C dict
#tar -jxvf "stardict-oald-cn-2.4.2.tar.bz2" -C dict



for file in `ls dict`
do
    echo "file:"$file
    if [ -d "./dict/$file" ]
    then
        sudo cp  ./dict/$file/*.* /usr/share/stardict/dic
        #ls "./dict/$file/"
    else
        echo "Error"
    fi
done
