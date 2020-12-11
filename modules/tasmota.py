import requests
import sys

# import config, logger
import config, utils

api_url = "http://{ip}/cm?"
status_parameters = "&cmnd=Status"
power_on_parameters = "&cmnd=Power%20On"
power_off_parameters = "&cmnd=Power%20Off"
api_auth_parameters = "&user={username}&password={password}"

def main():
    if not config.IP_ADDRESS:
        print("Please set IP_ADDRESS in config file")
        sys.exit(0)

    api_command(power_off_parameters)


def start_charging():
    try:
        utils.logger.info("Starting the charge")
        api_command(power_on_parameters)
    except:
        raise


def stop_charging():
    try:
        utils.logger.info("Stoping the charge")
        api_command(power_off_parameters)
    except:
        raise

def api_command(parameters):
    request_url = api_url.format(ip=config.IP_ADDRESS) + parameters
    if config.USERNAME and config.PASSWORD:
        request_url += api_auth_parameters.format(username=config.USERNAME, password=config.PASSWORD)

    response = requests.request("GET", request_url)
    json_response = response.json()
    #print(json_response)
