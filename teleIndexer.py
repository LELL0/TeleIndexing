import argparse
import time
from telethon import TelegramClient
from telethon.tl.types import (PeerChannel)
import json


API_ID = <API ID >          # int val
API_HASH = "<API ID>"       # string val

client = TelegramClient("anon", API_ID, API_HASH)


def getKeyword():
    parser = argparse.ArgumentParser(
        description="-c <channel> -i <XLastMessages>")

    parser.add_argument("-c", "--channel", type=str, required=True,
                        help="A Channel Name, URL or ID is required.")

    parser.add_argument("-i", "--XLastMessages", type=int, required=True,
                        help="Last n Messages to fetch from the channel.")

    try:
        user_input_channel = str(parser.parse_args().channel).lower()
        if not ("t.me" in user_input_channel or user_input_channel.isdigit()):
            user_input_channel = "t.me/"+user_input_channel

        XLastMessages = parser.parse_args().XLastMessages

    except:
        print("error with the arguments!")
        quit()

    return user_input_channel, XLastMessages


def displayResultFromJson(fileName):
    try:
        f = open(fileName+".json")
        print(f.read())
    except:
        pass


def appendToFile(fileName, dictionary):
    try:
        with open(fileName+".json", "w") as outfile:
            json.dump(dictionary, outfile)
    except:
        pass


async def getChannel(user_input_channel):
    if user_input_channel.isdigit():
        entity = PeerChannel(int(user_input_channel))

    else:
        entity = user_input_channel
    try:
        tChannel = await client.get_entity(entity)

    except:
        print("Channel NOT available Please Enter a Valid channel")
        quit()
    return tChannel


async def getMessage(tChannel, XLastMessages):
    try:
        msgsList = list()
        async for message in client.iter_messages(tChannel, limit=XLastMessages):
            msgDict = dict()
            msgDict["message_id"] = message.id
            msgDict["message_text"] = message.text
            msgDict["message_date"] = str(
                message.date.strftime("%m-%d-%Y; %H:%M:%S"))
            msgDict["message_url"] = "t.me/" + \
                str(tChannel.username)+"/"+str(message.id)
            msgsList.append(msgDict)
            dataDict = dict()
            dataDict["Messages"] = msgsList
        return dataDict
    except ValueError as e:
        print("Have to sleep", e.seconds, "seconds")
        time.sleep(e.seconds)


with client:
    user_input_channel, XLastMessages = getKeyword()

    tchannel = client.loop.run_until_complete(getChannel(user_input_channel))

    msgData = list()
    msgData = client.loop.run_until_complete(
        getMessage(tchannel, XLastMessages))

    appendToFile("telegram_messages", msgData)

    displayResultFromJson("telegram_messages")
