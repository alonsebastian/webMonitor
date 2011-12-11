import time, os 
while True:
    route = "google.com"
    ping_route = "ping -c 1 -W 2 " + route + ' | grep "packet loss"'
    print ping_route

    result = os.popen(ping_route).read()
    if "100% packet loss" in result:
        print "server down"
        #server down, do procedure

    time.sleep (10)

