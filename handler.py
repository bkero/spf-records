#!/usr/bin/env python
"""This file adds an event handler to execute sender_policy_flattener binary"""
from subprocess import call, check_call


def handler(event, context):
    """This is the handler that AWS Lambda should execute (handler.handler)"""
    call("./bin/spflat -c settings.json", shell=True)
    if check_call is 0:
        exit(0)
    else:
        exit(1)
