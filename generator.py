def generate_functions(name):
    function_str = "def $name(chat_id, message): \
    bot = Bot(token=TELEGRAM_TOKEN)\
    bot.sendMessage(chat_id=chat_id, text=message)"

    function_str.replace("$name", name)

    return function_str


def generate_callback(name):
    callback_str = "def $name(ch, method, properties, body):\
    pass"
    callback_str.replace("$name", name)
    
    return callback_str


def generate_subscriber():
    subscriber_str = "def subscribe_topic(channel, topic):\
    channel.queue_declare(queue=topic)\
    channel.basic_consume(queue=topic,\
                          auto_ack=True,\
                          on_message_callback=callback)"

    return subscriber_str