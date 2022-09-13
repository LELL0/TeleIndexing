# TeleIndexing
 Returns the last n messages From a chosen Telegram Channel.

## Input:

```
usage: teleIndexer.py [-h] -c CHANNEL -i XLASTMESSAGES

-c <channel> -i <XLastMessages>

options:
  -h, --help            show this help message and exit
  -c CHANNEL, --channel CHANNEL
                        A Channel Name, URL, or ID is required.
  -i XLASTMESSAGES, --XLastMessages XLASTMESSAGES
                        Last n Messages to fetch from the channel.                    
```
## Examples:

```
teleIndexer.py -c 569691 -i 10
```

```
teleIndexer.py -channel https://t.me/programminginc --XLASTMESSAGES 25
```

```
teleIndexer.py -c programminginc -i 50
```


# Docker:

## build the docker:

```
sudo docker build . -t teleIndexer:1.0.0
```

## examples running the docker:
```
sudo docker run -it teleIndexer:1.0.0 -c 569691 -i 10
```

```
sudo docker run -it teleIndexer:1.0.0 -c https://t.me/programminginc -i 25
```

```
sudo docker run -it teleIndexer:1.0.0 -c programminginc -i 50
```

## Output:

JSON file:
![image](https://user-images.githubusercontent.com/81851926/189934606-b5a1230c-2504-498c-8b6e-52c83ec75a19.png)

Commandline:
![image](https://user-images.githubusercontent.com/81851926/189935164-005b3c41-a9a7-473d-9c25-0b214ef406bb.png)


### the output filename is named: "telegram_messages.json".

## First Run:

### For the script to run correctly you need to add an API_ID & an API_HASH on lines 8 & 9 (You can get those values at "my.telegram.org/apps"): 

![image](https://user-images.githubusercontent.com/81851926/189935825-8e51a412-8872-440d-8c95-edc3597d197a.png)

### At the first run, you will also need to log in to your telegram account:

![image](https://user-images.githubusercontent.com/81851926/189939106-82e746d1-4458-4869-8664-220d6cf00980.png)
