from generator import *
import json

if __name__ == "__main__":
    str_file = ""
    with open("templates/app.py", "r") as f:
        for line in f:
            str_file += line
        str_file = insert_string(str_file, generate_subscriber(), "#callf")
        str_file = insert_string(str_file, generate_callback("callback"), "#callf")
        str_file = insert_string(str_file, generate_functions("send_message"), "#callf")

        print(str_file)
