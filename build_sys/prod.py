import json
import platform
from time import sleep
# os.system()
import os
import sys
from tools import test, sanitize, debug, benchmark
from build import build
def prod(data):
    test(data)
    sanitize(data)
    debug(data)
    benchmark(data)
    build(data, )
