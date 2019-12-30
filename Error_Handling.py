#!/usr/bin/python
import logging

class UnsupportedFileExtensionError(Exception):
    pass

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


def write_to_file(path):
    assert path, "path is empty"
    if '.cli' in path:
        raise UnsupportedFileExtensionError("cli files are not supported")
    try:
        f = open(path, "w")
    except FileNotFoundError as err:
        raise
        logger.error("File or directory not found")
        logger.exception(err)
    finally:
        print("end write")

path = "games/settings.cli"
write_to_file(path)
