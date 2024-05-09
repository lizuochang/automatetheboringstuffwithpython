"""
# -*- coding: utf-8 -*-
# @Time    : 2024/4/27 12:11 
# @File    : searchpath.py
# @Author  : li
# @Software: PyCharm
"""
import numpy as np
from queue import PriorityQueue

class Map:#地图
    def __init__(self,width,height)->None:
        self.width=width
        self.height=height
        self.neighbor=[[] for i in range(width*height)]
    # #添加边
    def addEdge(self,from_:int,to_:int):
        if (from_ not in range(self.width*self.height)) or (to_ not in range(self.width*self.height)):
            return 0
        self.neighbor[from_].append(to_)
        self.neighbor[to_].append(from_)
    #由序号获得该点在迷宫的x,y坐标
    def get_x_y(self,num:int):
        if num not in range(self.width*self.height):
            return -1,-1
        x=num%self.width
        y=num//self.width
        return x,y
class Astar:#A*寻路算法
    def __init__(self,_map,start:int,end:int)->None:
        self.run_map=_map
        self.start=start
        self.end=end
        #open集
        self.open_set=PriorityQueue()
        #cost_so_far表示到达某个节点的代价，也可相当于close集使用
        self.cost_so_far=dict()
        #每个节点的前序节点
        self.came_from=dict()
        #将起点放入，优先级设为0，无所谓设置多少，因为总是第一个被取出
        self.open_set.put((0,start))
        self.came_from[start]=-1
        self.cost_so_far[start]=0
    # h函数计算，即启发式信息
    def heuristic(self,a,b):
        x1,y1=self.run_map.get_x_y(a)
        x2,y2=self.run_map.get_x_y(b)
        return abs(x1-x2)+abs(y1-y2)

    #运行A*寻路算法，如果没找到路径返回0，找到返回1
    def find_way(self):
        # open 表不为空
        while not self.open_set.empty():
            # 从优先队列中取出代价最短的节点作为当前遍历的节点，类型为（priority,node)
            current=self.open_set.get()
            if current[1]==self.end:      # 找到终点
                break
            for next in self.run_map.neighbor[current[1]]:   # 遍历邻接节点
                new_cost=self.cost_so_far[current[1]]+1      # 新的代价
                # 没有到达过的点 或 比原本已经到达过的点的代价更小
                if (next not in self.cost_so_far) or (new_cost<self.cost_so_far[next]):
                    self.cost_so_far[next]=new_cost
                    priority=new_cost+self.heuristic(next,self.end)
                    self.open_set.put((priority,next))
                    self.came_from[next]=current[1]
        if self.end not in self.cost_so_far:
            return 0
        return 1
    def show_way(self):
        # 记录路径经过的节点
        result = []
        current = self.end
        # 不断寻找前序节点
        while self.came_from[current] != -1:
            result.append(current)
            current = self.came_from[current]
        # 加上起点
        result.append(current)
        # 翻转路径
        result.reverse()
        print(result)




theMap=Map(4,4)
theMap.addEdge(0, 1)
theMap.addEdge(1, 2)
theMap.addEdge(2, 6)
theMap.addEdge(3, 7)
theMap.addEdge(4, 5)
theMap.addEdge(5, 6)
theMap.addEdge(6, 7)
theMap.addEdge(4, 8)
theMap.addEdge(5, 9)
theMap.addEdge(7, 11)
theMap.addEdge(8, 9)
theMap.addEdge(9, 10)
theMap.addEdge(10, 11)
theMap.addEdge(8, 12)
theMap.addEdge(10, 14)
theMap.addEdge(12, 13)
theMap.addEdge(13, 14)
theMap.addEdge(14, 15)
# A* 算法寻路
theAstar = Astar(theMap, 0, 15)
theAstar.find_way()
theAstar.show_way()