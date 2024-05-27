#Don't Edit Anything [Support @im_piro | @PiroHackz]



from aiohttp import web

routes = web.RouteTableDef()

@routes.get("/", allow_head=True)
async def root_route_handler(request):
    return web.json_response("CodeXBotz")
