import pika
import json

from telegram import Bot

TELEGRAM_TOKEN="911910503:AAGZ8DkBGcKX8p7o4yCN9IYHOny6jR8B7Kw"

#### CALLBACK FUNCTIONS ####

#callf

if __name__ == "__main__":
    connection = pika.BlockingConnection(pika.ConnectionParameters('0.0.0.0'))
    ch = connection.channel()

    with open("conf.json") as f:
        config = json.load(f)

        for topic in config["topics"]:
            print(topic["name"])
            subscribe_topic(ch, topic["name"])

    print(' [*] Waiting for messages. To exit press CTRL+C')
    ch.start_consuming()
