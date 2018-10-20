# -*- coding: utf-8 -*-
"""
Created on Fri Oct 19 17:45:47 2018

@author: Owner
"""
# -*- coding: utf-8 -*-

from turtle import *
def rose_window_recursion(points, ratio, depth):
    rectangle(points)
    new_points = deviding_points(points, ratio)
    if depth == 0:
        up()
        setpos(-200, -200)
    else:
        rose_window_recursion(new_points, ratio, depth - 1)


def deviding(p0, p1, x):
    return p0 * (1 - x) + p1 * x

# rectangle(四角形の4頂点)
def rectangle(points):
    [[x0, y0], [x1, y1], [x2, y2], [x3, y3]] = points
    up()
    setpos(x0, y0)
    down()
    setpos(x1, y1)
    setpos(x2, y2)
    setpos(x3, y3)
    setpos(x0, y0)

# 2点の内分点を求める
# devidng_point(点A, 点B, 内分比)
def deviding_point(p0, p1, ratio):
    [x0, y0] = p0
    [x1, y1] = p1
    xr = deviding(x0, x1, ratio)
    yr = deviding(y0, y1, ratio)
    return [xr, yr]

# 四角形の各辺の内分点を求める
# deviding_points(四角形の4頂点, 内分比)
def deviding_ppints(points, ratio):
    [p0, p1, p2, p3] = points
    pr0 = deviding_point(p0, p1, ratio)
    pr1 = deviding_point(p1, p2, ratio)
    pr2 = deviding_point(p2, p3, ratio)
    pr3 = deviding_point(p3, p0, ratio)
    return [pr0, pr1, pr2, pr3]
