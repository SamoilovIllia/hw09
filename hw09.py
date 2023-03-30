import re
from collections import defaultdict
from pprint import pprint


TEL_DICT = defaultdict(str)


def input_errors(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            print(f"Error: {e}")
            return 'The phone number must be ten digits long.\nThe name and phone number must be separated by only a space.\nFor example:\nadd Petro 0987456321\nchange Petro 0987123004'
    return wrapper


@input_errors
def exit_input(text: str):
    return 'Good bye!'


@input_errors
def hello_input(text: str):
    return 'How can I help you?'


@input_errors
def add_input(text: str):
    name = str(re.findall("\s[a-z]+\s", text))
    TEL_DICT[str(re.findall("[a-z]+", name)[0]).title()
             ] = re.findall("\d{10}", text)[0]
    name_print = str(re.findall("[a-z]+", name)[0]).title()
    return f"Contact \"{name_print}\" add successful"


@input_errors
def change_input(text: str):
    name = str(re.findall("\s[a-z]+", text))
    # and TEL_DICT.get(str(re.findall("[a-z]+", key)[0]).title()):
    TEL_DICT[str(re.findall("[a-z]+", name)[0]).title()
             ] = re.findall("\d{10}", text)[0]


@input_errors
def phone_input(text: str):
    key = str(re.findall("\s[a-z]+", text))
    return TEL_DICT.get(str(re.findall("[a-z]+", key)[0].title()))


@input_errors
def show_input(text: str):
    return '\n'.join([f"{k} : {v}" for k, v in TEL_DICT.items()])


@input_errors
def unknown_input(text=None):
    return 'Unknown command. Try again.'


@input_errors
def parse_command(text):
    if text == 'good bye' or text == 'close' or text == 'exit' or text == '.':
        return exit_input
    if text == 'hello':
        return hello_input
    if text.startswith('add '):
        return add_input
    if text.startswith('change '):
        return change_input
    if text.startswith('phone '):
        return phone_input
    if text == 'show all':
        return show_input
    return unknown_input


@input_errors
def main_f():

    while True:
        user_input = input('>>> ').lower()

        command = parse_command(user_input)

        print(command(user_input))
        if command == exit_input:
            break


if __name__ == '__main__':
    main_f()
