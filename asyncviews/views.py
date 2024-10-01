import asyncio
import httpx
from django.http import HttpResponse

async def http_call_async():
    for num in range(1, 6):
        await asyncio.sleep(1)  
        print(num)  
    async with httpx.AsyncClient() as client:
        r = await client.get("https://httpbin.org/") 
        print(r)  

async def async_view(request):
    asyncio.create_task(http_call_async()) 
    return HttpResponse('Non-blocking HTTP request')

#_________________________________________________________

# import time
# from django.http import JsonResponse

# def api(request):
#     time.sleep(1)
#     payload = {"message": "Hello World!"}
    
#     if "task_id" in request.GET:
#         payload["task_id"] = request.GET["task_id"]
#     return JsonResponse(payload)

#__________________________________________________________

# import asyncio
# import httpx
# from django.http import HttpResponse

# async def http_call_async():
#     for num in range(1, 6):
#         await asyncio.sleep(1)
#         print(num)
#     async with httpx.AsyncClient() as client:
#         r = await client.get("https://httpbin.org")
#         print(r)
        
# async def async_view(request):
#     loop = asyncio.get_event_loop()
#     loop.create_task(http_call_async())
#     return HttpResponse('Non-blocking HTTP request')

#___________________________________________________________

# import asyncio
# import httpx
# from django.http import HttpResponse
# from time import sleep

# async def http_call_async():
#     for num in range(1, 6):
#         await asyncio.sleep(1)
#         print(num)
#     async with httpx.AsyncClient() as client:
#         r = await client.get("https://httpbin.org")
#         print(r)

# def http_call_sync():
#     for num in range(1, 6):
#         sleep(1)
#         print(num)
#         r = httpx.get("https://httpbin.org/")
#         print(r)

# async def async_view(request):
#     loop = asyncio.get_event_loop()
#     loop.create_task(http_call_async())
#     return HttpResponse('Non-blocking HTTP request')

# def sync_view(request):
#     http_call_sync()
#     return HttpResponse("Blocking HTTP request")
