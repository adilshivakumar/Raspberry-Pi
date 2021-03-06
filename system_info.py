import time
import asyncio
from datetime import timedelta
from aiohttp import web
import netifaces as ni
import get_time 
import memory_free
import disk_free
import cpu_load
import clock

import up_time

async def show_cpu(request): # print the cpu
    cpu_string = cpu_load.get_CPU()
    #uptime_string = str(timedelta(seconds = uptime_seconds))
    print('cpu= ' + cpu_string)
    return web.Response(content_type='text/html', text=cpu_string)

async def show_clock(request): # print the clock
    clock_string = clock.clock()
    #uptime_string = str(timedelta(seconds = uptime_seconds))
    print('clock= ' + clock_string)
    return web.Response(content_type='text/html', text=clock_string)

async def show_disk(request): # print the disk
    disk_string = disk_free.get_diskfree()
    #uptime_string = str(timedelta(seconds = uptime_seconds))
    print('disk= ' + disk_string)
    return web.Response(content_type='text/html', text=disk_string)


async def show_memory(request): # print the memory
    memory_string = memory_free.get_memory()
    #uptime_string = str(timedelta(seconds = uptime_seconds))
    print('memory= ' + memory_string)
    return web.Response(content_type='text/html', text=memory_string)

async def show_time(request): # print the time
    time_string = get_time.get_time()
    #uptime_string = str(timedelta(seconds = uptime_seconds))
    print('time= ' + time_string)
    return web.Response(content_type='text/html', text=time_string)

async def show_ip(request):
    for interface in ni.interfaces():
        if interface == ni.gateways()['default'][ni.AF_INET][1]:
            try:
                routingIPAddr = ni.ifaddresses(interface)[ni.AF_INET][0]['addr']
            except KeyError:
                pass
    print(routingIPAddr)
    return web.Response(content_type='text/html', text=routingIPAddr)


async def bellon(request): # enable auto bell
    print('bell on')
    return web.Response(content_type='text/html', text='Auto bell is enabled')

async def show_uptime(request): # print the uptime
    uptime_string = up_time.get_uptime()
    #uptime_string = str(timedelta(seconds = uptime_seconds))
    print('uptime= ' + uptime_string)
    return web.Response(content_type='text/html', text=uptime_string)


if __name__ == '__main__':
    app = web.Application()
    app.router.add_get('/time', show_time)
    app.router.add_get('/uptime', show_uptime)
    app.router.add_get('/ip', show_ip)
    app.router.add_get('/memory', show_memory)
    app.router.add_get('/disk', show_disk)
    app.router.add_get('/cpu', show_cpu)
    app.router.add_get('/clock', show_clock)
    web.run_app(app, port=8000)

