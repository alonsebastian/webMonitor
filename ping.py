import os

def ping(route):
    ping_route = "ping -c 1 -W 2 " + route + ' | grep "packet loss"'
    #ping -c 1 = count 1, -W 2 = timeout 2 seconds

    result = os.popen(ping_route).read()
    return result
