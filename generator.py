def generate_functions(function_name):
    return "def {}(chat_id, message):\n\
    bot = Bot(token=TELEGRAM_TOKEN)\
    bot.sendMessage(chat_id=chat_id, text=message)\n\n".format(function_name)


def generate_callback(function_name):
    return "def {}(ch, method, properties, body):\n\tpass\n\n".format(function_name)


def generate_subscriber():
    return "def subscribe_topic(channel, topic):\n\
    channel.queue_declare(queue=topic)\n\
    channel.basic_consume(queue=topic,\
    auto_ack=True, on_message_callback=callback)\n\n"


def insert_string(string, string_to_insert, tag):
    pos = string.find(tag)
    return string[:pos] + string_to_insert + string[pos:] + "\n"
