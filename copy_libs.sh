#/bin/bash -

lib_path_list=(/lib	/lib64 /lib/x86_64-linux-gnu /usr/lib/x86_64-linux-gnu )
libs=
dst=""

while getopts "d:" arg;
do
	case $arg in
		d)
			dst="$OPTARG";;
		:)
			echo "unknow" $OPTARG
	esac
done

echo dst = $dst
shift $(($OPTIND - 1))
libs=$*
echo libs = $libs
for lib in $libs;
do
	#echo libname = $lib;
	#echo ${lib_path_list[@]}
	for lib_path in ${lib_path_list[@]};
	do
		if [ -d $lib_path ] ;
		then
			if [ -f $lib_path/$lib ];
			then
				str=$lib_path/$lib;
				lib_names=${str%%.*}"*"
				cp $lib_names $dst -rf
				echo "copy $lib_names finish"
			fi
		fi
	done;
done;

