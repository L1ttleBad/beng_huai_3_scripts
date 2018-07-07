#########################################################################
# File Name: update.sh
# Author: wushenxiaohuai
# mail: 74166738@qq.com
# Created Time: Fri 06 Jul 2018 10:07:39 PM DST
#########################################################################
#!/bin/bash

git add .
git commit -m "$1"

git push -u origin master
