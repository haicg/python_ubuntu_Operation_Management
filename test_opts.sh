#/bin/bash -

lib_path_list=(/lib	/lib64 /lib/x86_64-linux-gnu)
while getopts "d:l:" arg;
do
	case $arg in
		d)
			echo "DIRECTORY "  $OPTARG;;
		l)
			echo "libs" $OPTARG;;
		:)
			echo "unknow" $OPTARG
	esac
done
shift $(($OPTIND - 1))
echo $*

#echo $@
