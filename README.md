# Reveive MQTT data 
Reveice MQTT data and save the data into a local csv file

## File
```
Receive-MQTT-data
    |_start_receive.py
```

## Environmenet
```
python3
```

## Dependencies
```
    time
    json
    paho-mqtt
    pandas
```

## Configuration 
```
Go to start_receive.py
Fill all placeholders
```

## Run
To start: go to dir of start_receive.py, run command:
```
    python3 start_receive.py
```
To stop: "Ctrl + c" then the data reveived automatcally saved into the given path

## License
MIT license for this repo.

## References
```
https://www.jianshu.com/p/ef546f476322

https://blog.csdn.net/weixin_41656968/article/details/80848542#1onconnect

https://www.npmjs.com/package/mqtt#api

http://www.steves-internet-guide.com/loop-python-mqtt-client/#:~:text=To%20stop%20the%20loop%20use,be%20stopped%20by%20calling%20loop.
```