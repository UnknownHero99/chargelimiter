from time import sleep
import sys
import config
import utils

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


if __name__ == "__main__":
    config.module.main()
    while True:
        if battery_percentage() > config.STOP_CHARGING_PERCENTAGE and battery_charging():
            config.module.stop_charging()
        elif battery_percentage() < config.START_CHARGING_PERCENTAGE and not battery_charging():
            config.module.start_charging()
        utils.logger.debug("Battery percentage at " + str(battery_percentage()))
        sleep(config.SLEEP_TIME)


    #plugged = "Plugged In" if plugged else "Not Plugged In"
    #print(percent+'% | '+plugged)
