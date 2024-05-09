"""
# -*- coding: utf-8 -*-
# @Time    : 2024/4/26 11:08 
# @File    : videoReptile.py
# @Author  : li
# @Software: PyCharm
"""
import requests
url="https://vd3.bdstatic.com/mda-pew1q57ahc8h8gwx/720p/h264/1685495552595736351/mda-pew1q57ahc8h8gwx.mp4?pd=19&vt=1"
resp=requests.get(url)
if resp.status_code==200:
    print("访问成功！")
    video=resp.content
    # file=open("video/01.mp4","wb")        #操作文件
    # file.write(video)                     #写入数据
    # file.close()                          #关闭文件
    with open('video/03.mp4','wb') as file:
        file.write(video)



else:
    print("访问失败！")