from tuyaha import TuyaApi
import sys

#import config, logger
import config, utils


def main():
    global api
    api = TuyaApi()
    config.module.get_token(api)
    if not config.DEVICE_ID:
        print(api.get_all_devices())
        sys.exit(0)

    global socket
    socket = api.get_device_by_id(config.DEVICE_ID)

def get_token():
    utils.logger.info("Getting a new token")
    api.init(config.USERNAME, config.PASSWORD, config.REGION)

def start_charging():
    try:
        utils.logger.info("Starting the charge")
        socket.turn_on()
    except:
        get_token()

def stop_charging():
    try:
        utils.logger.info("Stoping the charge")
        socket.turn_off()# maybe add reconnecting if needed
    except:
        get_token()
