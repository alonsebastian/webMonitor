import time, os
import conf

while True:
    ping_route = "ping -c 1 -W 2 " + conf.route + ' | grep "packet loss"'
    print ping_route

    result = os.popen(ping_route).read()
    if "100% packet loss" in result:
        print "server down"
        #server down, do procedure
        Mailing.mail(conf.email, "Server is down", "The server you were monitoring is DOWN!")
        print "email sent"
        if conf.sms_alarm and conf.sms_company.lower() == "movistar":
            Mailing.mail(conf.sms_number+"@sms.movistar.net.ar", "", "The server you were monitoring is DOWN!")
        if conf.sms_alarm and conf.sms_company.lower() == "verizon":
            Mailing.mail(conf.sms_number+"@vtext.com", "", "The server you were monitoring is DOWN!")
        if conf.sms_alarm and conf.sms_company.lower() == "at&t":
            Mailing.mail(conf.sms_number+"@txt.att.net", "", "The server you were monitoring is DOWN!")
        if conf.sms_alarm and conf.sms_company.lower() == "sprint":
            Mailing.mail(conf.sms_number+"@messaging.sprintpcs.com", "", "The server you were monitoring is DOWN!")
        if conf.sms_alarm and conf.sms_company.lower() == "t-mobile":
            Mailing.mail(conf.sms_number+"@tmomail.net", "", "The server you were monitoring is DOWN!")
            
        time.sleep(600) #10 minutes

    time.sleep (10)

