import importlib
import os

from .Application import Application

__all__ = [Application]


def auto_import():
    """
    Automatically import all modules in the same directory as this file
    if they are not imported already.
    """
    cwd = os.path.dirname(os.path.abspath(__file__))
    for filename in os.listdir(cwd):
        if not filename.endswith(".py") or filename == "__init__.py":
            continue

        module_name = filename[:-3]

        # check if module is already imported
        if globals().get(module_name) is not None:
            continue

        # get attributes from module
        module = importlib.import_module(f".{module_name}", __package__)
        attrs = [
            getattr(module, name) for name in dir(module) if not name.startswith("_")
        ]

        # debug print attrs
        # export attributes to this module
        for attr in attrs:
            globals()[attr.__name__] = attr


auto_import()
