#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'Alex Qian'

'''
web application using asyncio/aiohttp.
'''

import logging; logging.basicConfig(level=logging.INFO)

import asyncio, os, json, time
from datetime import datetime

from aiohttp import web

def index(request):
    return web.Response(body=b'<h1>Awesome</h1>',headers={'content-type':'text/html'})

async def init():
    app = web.Application()
    app.router.add_route('GET', '/', index)
    
    runner = web.AppRunner(app)
    await runner.setup()

    site = web.TCPSite(runner,'127.0.0.1', 8080)
    logging.info('server started at http://127.0.0.1:8080...')
    await site.start()
    
loop = asyncio.get_event_loop()
loop.run_until_complete(init())
loop.run_forever()