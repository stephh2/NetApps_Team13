from __future__ import absolute_import, division, print_function, unicode_literals

""" Example of browsing for a service (in this case, HTTP) """
import socket
import sys
from time import sleep

LED_IP = ""
STORAGE_IP = ""


from zeroconf import ServiceBrowser, ServiceStateChange, Zeroconf

import subprocess

def get_ip_address():
    com = subprocess.Popen(["ifconfig"], stdout=subprocess.PIPE, shell=True)
    (out, err) = com.communicate()
    p = str(out)\
        
    i = p.find("wlan0")
    p = p[i:-1]
    i = p.find("inet")+5
    j = p.find("netmask")
    p = p[i:j]
    print("my IP address is : {}".format(p))
    
    return p


looking = True
def on_service_state_change(zeroconf, service_type, name, state_change):    
    if state_change is ServiceStateChange.Added:
        if name.find("LED13") is not -1 or name.find("STORAGE13") is not -1:
            info = zeroconf.get_service_info(service_type, name)
            if info:
                if info.properties:
                    if name.find("LED13") is not -1:
                        props = dict(info.properties)
                        global LED_IP
                        LED_IP = str(props[b'IP'])[2:-1]
                        print("Found LED address to be {}".format(LED_IP))
                    if name.find("STORAGE13") is not -1:
                        props = dict(info.properties)
                        global STORAGE_IP
                        STORAGE_IP = str(props[b'IP'])[2:-1]
                        print("Found STORAGE address to be {}".format(STORAGE_IP))
                    


def startZeroconf():
    get_ip_address()
    
    logging.basicConfig(level=logging.DEBUG)
    if len(sys.argv) > 1:
        assert sys.argv[1:] == ['--debug']
        logging.getLogger('zeroconf').setLevel(logging.DEBUG)

    zeroconf = Zeroconf()
    print("Browsing services, press Ctrl-C to exit...")
    browser = ServiceBrowser(zeroconf, "_http._tcp.local.", handlers=[on_service_state_change])
    
    try:
        while looking:
            sleep(0.1)
    except KeyboardInterrupt:
        pass
    finally:
        print("Found both IP addresses to be:")
        print("\t \t LED     : {}".format(LED_IP))
        print("\t \t STORAGE : {}".format(STORAGE_IP))
        zeroconf.close()

