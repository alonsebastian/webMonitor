import time, os
from urllib2 import urlopen
import conf

content = ""
while True:
    ping_route = "ping -c 1 -W 2 " + conf.route + ' | grep "packet loss"'
    #ping -c 1 = count 1, -W 2 = timeout 2 seconds
    print ping_route

    result = os.popen(ping_route).read()
    try:
        content = urlopen(conf.message_url).read()
    except urllib2.HTTPError:
        print "wrong url or server down"    #most like 404

    if "100% packet loss" in result:
        print "server down"
        if content != "":
            message = "server down!" + content
        else: message = "The server you were monitoring is DOWN!"
        #server down, do procedure

        Mailing.mail(conf.email, "Server is down", message)
        print "email sent"
        if conf.sms_alarm and conf.sms_company.lower() == "movistar":
            Mailing.mail(conf.sms_number+"@sms.movistar.net.ar", "", message)
        if conf.sms_alarm and conf.sms_company.lower() == "verizon":
            Mailing.mail(conf.sms_number+"@vtext.com", "", message)
        if conf.sms_alarm and conf.sms_company.lower() == "at&t":
            Mailing.mail(conf.sms_number+"@txt.att.net", "", message)
        if conf.sms_alarm and conf.sms_company.lower() == "sprint":
            Mailing.mail(conf.sms_number+"@messaging.sprintpcs.com", "", message)
        if conf.sms_alarm and conf.sms_company.lower() == "t-mobile":
            Mailing.mail(conf.sms_number+"@tmomail.net", "", message)
            
        time.sleep(600) #10 minutes

    time.sleep (10)
