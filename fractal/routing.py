from channels.routing import route
from interactive.consumers import ws_message, ws_add, ws_disconnect
channel_routing = [

    route("websocket.connect", ws_add, path=r"^/(?P<room_type>[a-zA-Z0-9_]+)/(?P<room_label>[a-zA-Z0-9_]+)$"),
    route("websocket.receive", ws_message, path=r"^/(?P<room_type>[a-zA-Z0-9_]+)/(?P<room_label>[a-zA-Z0-9_]+)$"),
    route("websocket.disconnect", ws_disconnect, path=r"^/(?P<room_type>[a-zA-Z0-9_]+)/(?P<room_label>[a-zA-Z0-9_]+)$"),

]

