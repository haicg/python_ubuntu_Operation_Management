#!/bin/sh -
if [ $# != 1 ];then
    echo "Please input right parm"
else
    echo $1

    jdk_name=""
    if [ ! -e JDK ]; then
        mkdir JDK
    fi
    tar -zxvf $1 -C JDK
    for file in `ls JDK`
    do
        echo "file:"$file
        if [ -d JDK/$file ];
        then
            jdk_name=$file
            echo $jdk_name
            break
        else
            echo "Not a dir"
        fi
    done

    java_path_file=java_path.sh
    sudo mv -f JDK /usr/
    echo "java_home $jdk_name"
    #if [ ! -e $java_path_file ]; then
(
cat <<EOF
#/bin/sh -
export JAVA_HOME=/usr/JDK/$jdk_name
export JRE_HOME=\${JAVA_HOME}/jre
export CLASSPATH=.:\${JAVA_HOME}/lib:\${JRE_HOME}/lib
export PATH=\${JAVA_HOME}/bin:\$PATH
EOF
) > $java_path_file
    #fi
    if [ -d /etc/profile.d/ ]; then
        #sudo chmod +x java_path.sh
        sudo cp -rf $java_path_file /etc/profile.d/
        rm $java_path_file
    fi
fi

