#/bin/sh
dst_lib=/lib
dlibs=`ldd $1 |grep not |gawk -F ' ' '{print $1}'|gawk BEGIN{RS=EOF}'{gsub(/\n/," ");print}'`
echo $dlibs

