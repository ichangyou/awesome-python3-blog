#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'ChangYou'

'''
async web application.
使用aiohttp库创建一个简单的异步Web服务器的Python代码段
'''

import logging; logging.basicConfig(level=logging.INFO)

import asyncio, os, json, time
from datetime import datetime

# 导入aiohttp库中的web模块，该模块用于创建Web应用程序和处理HTTP请求和响应
from aiohttp import web

def index(request):
    return web.Response(body=b'<h1>Awesome</h1>',headers={'content-type':'text/html'})

# 异步协程函数，它初始化Web应用程序并启动HTTP服务器
async def init(loop):
    # 创建一个Web应用程序实例
    app = web.Application(loop=loop)
    # 将index处理函数与HTTP GET请求方法和根路径("/")关联
    app.router.add_route('GET', '/', index)
    # 创建一个HTTP服务器，并将其绑定到本地IP地址127.0.0.1和端口9000。这将在指定的IP地址和端口上监听HTTP请求
    srv = await loop.create_server(app.make_handler(), '127.0.0.1', 9000)
    # 在控制台上输出服务器已启动的信息
    logging.info('server started at http://127.0.0.1:9000...')
    return srv

# 首先获取一个事件循环（Event Loop）
# 然后通过loop.run_until_complete(init(loop))运行init协程函数，以初始化Web应用程序和服务器。
# 最后，通过loop.run_forever()启动事件循环，使服务器一直运行，等待处理来自客户端的HTTP请求
loop = asyncio.get_event_loop()
loop.run_until_complete(init(loop))
loop.run_forever()
