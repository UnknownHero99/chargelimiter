from tuyaha import TuyaApi
from time import sleep
import sys
# CHECK platform
if sys.platform == 'linux':
    # check if android - need to install tuyaha and requests first using pip in qpython
    from os import environ
    if 'ANDROID_STORAGE' in environ:
        import androidhelper
        droid = androidhelper.Android()
        droid.batteryStartMonitoring()
        battery_percentage = lambda : droid.batteryGetLevel().result
        battery_charging = lambda : droid.batteryGetPlugType().result
        import requests
        requests.packages.urllib3.util.ssl_.DEFAULT_CIPHERS = "TLS13-CHACHA20-POLY1305-SHA256:TLS13-AES-128-GCM-SHA256:TLS13-AES-256-GCM-SHA384:ECDHE:!COMPLEMENTOFDEFAULT"

    else: # for a normal linux
        import psutil
        battery_percentage = lambda : psutil.sensors_battery().percent
        battery_charging = lambda : psutil.sensors_battery().power_plugged
else: # Check if this works on windows and osx
    import psutil
    battery_percentage = lambda : psutil.sensors_battery().percent
    battery_charging = lambda : psutil.sensors_battery().power_plugged


import logging, sys
logger = logging.getLogger("chargingLimit")
loglevel = "INFO"
log_level = "DEBUG"
log_handler = logging.StreamHandler(sys.stdout)
log_handler.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))
logger.setLevel(log_level)
logger.addHandler(log_handler)


USERNAME = "xxx.xxx@xxx.xxx"
PASSWORD = "xxx"
REGION = "eu" # us, ...

START_CHARGING_PERCENTAGE = 40
STOP_CHARGING_PERCENTAGE = 60
SLEEP_TIME = 100
#FULL_CHARGE = 100 # maybe add later
#FULL_CHARGE_TIME =  # make this take time and then calculate to charge fully by that time



#DEVICE_ID = '24005020a4cf12d7983a' # EXAMPLE OF Id - SET YOUR OWN
DEVICE_ID = '' # uncoment this line to get a list of all devices


def get_token(api):
    logger.info("Getting a new token")
    api.init(USERNAME, PASSWORD, REGION)



def start_charging(socket, api):
    try:
        logger.info("Starting the charge")
        socket.turn_on()
    except:
        get_token(api)

def stop_charging(socket, api):
    try:
        logger.info("Stoping the charge")
        socket.turn_off()# maybe add reconnecting if needed
    except:
        get_token(api)

if __name__ == "__main__":
    api = TuyaApi()
    get_token(api)
    if not DEVICE_ID:
        print(api.get_all_devices())
        sys.exit(0)

    socket = api.get_device_by_id(DEVICE_ID)
    while True:
        if battery_percentage() > STOP_CHARGING_PERCENTAGE and battery_charging():
            stop_charging(socket,api)
        elif battery_percentage() < START_CHARGING_PERCENTAGE and not battery_charging():
            start_charging(socket,api)
        logger.debug("Battery percentage at " + str(battery_percentage()))
        sleep(SLEEP_TIME)


    #plugged = "Plugged In" if plugged else "Not Plugged In"
    #print(percent+'% | '+plugged)
