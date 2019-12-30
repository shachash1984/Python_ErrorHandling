#!/usr/bin/python
import logging

logger = logging.Logger("logi")

"""
def func2():
    try:
        f = open("sdfdff", "r")
    except FileNotFoundError as err:
        logger.error("File doesn't exist")
        logger.exception(err)
        exit(2)
    except Exception as err:
        pass
    else:
        # no errors (not commonly used)
        pass
    finally:
        print("File doesn't exist!")
        pass


def func():
    func2()


func()
"""
# TODO
# Try to write to a file in a non existent directory
# (which will yield an error)
# handle the exception using try-except block
# make sure to point to the screen "end write"
# even when an exception occurred


def write_to_file():
    try:
        f = open("games/settings.txt", "w")
    except FileNotFoundError as err:
        logger.error("File or directory not found")
        logger.exception(err)
    finally:
        print("end write")


write_to_file()
