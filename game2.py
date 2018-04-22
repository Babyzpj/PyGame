# -*- coding: utf-8 -*-

# Copyright @2017 R&D, CINS Inc. (cins.com)
#
# Author: PengjunZhu <1512568691@qq.com>
#
# Function: 第2个小游戏，比比谁更帅。
#       add function:
#            1、持续玩功能
#            2、加入颜值评测功能
#            2、添加exe文件图标
#
# time: 2018/04/22
#print u"欢迎来玩游戏：比比谁更帅"

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import random

print u"游戏开始，请输入任意两个人的名字，比较他们帅气程度..."


while True:
    a = raw_input("name1:")
    b = raw_input("name2:")

    print "\n"

    x1 = random.randint(50, 100)
    x2 = random.randint(50, 100)

    maxValue = max(x1, x2)
    minValue = min(x1, x2)

    if len(a) >= len(b):
        print u"最帅的人是：", a, u"，经评测ta的颜值分数为:",maxValue
        print u"最man的人是：", b, u"，经评测ta的颜值分数为:",minValue
    else:
        print u"最帅的人是：", b, u"颜值为:",maxValue
        print u"最man的人是：", a, u"颜值为:",minValue


    print "\n"

    flag = int(raw_input("game continue?, yes:1, no:0 \t"))

    if flag == 1:
        continue
    else:
        print "please any key quit:"
        break
