# Chargelimiter
Limit battery charging level using a smart socket (like this one for example: https://m.blitzwolf.com/3680W-16A-WIFI-Smart-Socket-p-453.html).

This is a simple python script you can run on a device in order regulate chraging between a maximum and minimum % of battery capacity and through this extend battery life.

## Requirements
A device capable of running python (with internet access) connected to its chrager which is plugged into a smart socket (that can be operated using tuyaha library).

## SETUP

- download and install smartlife (android link: https://play.google.com/store/apps/details?id=com.tuya.smartlife&hl=sl&gl=US)
- register and conenct to your smart socket based on instructions in the app.
- Download the charging_limit.py script to your device
- Change the following fields in the charging_limit.py:
```
      USERNAME = "xxx.xxx@xxx.xxx"
      PASSWORD = "xxx"
      REGION = "eu" # us, ...
```
   and set them to the values you used for the smart life app

- Install software requirements (For installing the software requirements read the sections bellow.)

- Run the script once and read the device ids that are displayed as avaliable -> copy the one that your device is connected to
- Change the following fields in the charging_limit.py:
```
 DEVICE_ID = '' 
 START_CHARGING_PERCENTAGE = 40
 STOP_CHARGING_PERCENTAGE = 60
 SLEEP_TIME = 100
```
  To set desired percentage for the chrage start/stop, the id of the socket your device is connected to (that you copied in the previous step), and to set the interval of checking the battery level (in seconds).

### Android software requirements
 - i suggest downlaoding QPython (https://play.google.com/store/apps/details?id=org.qpython.qpy3&hl=en_US&gl=US) or similar
 - In qpython use the pip console and execute the following:
 ```
  $ install tuyaha
  $ install requests
  ```
  
### Linux / other software requirements
 Open terminal and execute:
 ```
  $ pip install tuyaha
  $ pip install requests
  $ pip install psutil
  ```
  


