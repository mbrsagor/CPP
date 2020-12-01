from time import sleep
from datetime import datetime
import json
from typing import Optional


def log(message, when=datetime.now()):
    print(f"{message} : {when}")


log("Hello")
sleep(1)
log("Hello Again")


def log2(message, when=None):
    if when is None:
        when = datetime.now()
    print(f"{message} : {when}")


log2('Hi there!')
sleep(0.1)
log2('Hello again!')

print('\n')


def decode(data, default={}):
    try:
        return json.loads(data)
    except ValueError:
        return default


foo = decode('bad data')
foo['stuff'] = 5

bar = decode('also bad')
bar['meep'] = 1

print('Foo:', foo)
print('Bar:', bar)


def decode_v2(data, default=None):
    try:
        return json.loads(data)
    except ValueError:
        if default is None:
            default = {}
        return default


foo = decode('bad data')
foo['stuff'] = 5
bar = decode('also bad')
bar['meep'] = 1
print('Foo:', foo)
print('Bar:', bar)
# assert foo is not bar

print('\n')


def log_typed(message: str, when: Optional[datetime] = None) -> None:
    if when is None:
        when = datetime.now()
    print(f"{when} : {message}")


log_typed("hello world")
