#!/usr/bin/python3
from __future__ import print_function
import sys


def safe_function(fct, *args):
    try:
        res_ = fct(*args)
    except Exception as e_:
        print("Exception: {}".format(e_), file=sys.stderr)
        return None
    else:
        return res_
