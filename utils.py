# -*- coding: utf-8 -*-

import os
import traceback

import tomli

import utils_env
from utils_ver import print_ver

# .....................
DATA = {}


def get_data() -> dict:
    """
    ..............................

    :return: ........................
    """
    print_ver()
    global DATA
    if DATA:
        return DATA

    if check_config := os.getenv("CHECK_CONFIG"):
        if not os.path.exists(check_config):
            print(f"..................... CHECK_CONFIG ..................... {check_config} ............")
            exit(1)
    else:
        check_config = utils_env.get_file_path("check.toml")
        if not check_config:
            print("................................................................................. CHECK_CONFIG .....................")
            exit(1)

    try:
        DATA = tomli.load(open(check_config, "rb"))
        return DATA
    except tomli.TOMLDecodeError:
        print(
            f"..................... {check_config} ........................ https://toml.io/cn/v1.0.0\n...............\n{traceback.format_exc()}"
        )
        exit(1)