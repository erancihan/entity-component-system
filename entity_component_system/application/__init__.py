import importlib
import os


def auto_import():
    """Automatically import all modules in the same directory as this file."""
    cwd = os.path.dirname(os.path.abspath(__file__))
    for filename in os.listdir(cwd):
        if not filename.endswith(".py") or filename == "__init__.py":
            continue

        # get attributes from module
        module_name = filename[:-3]
        module = importlib.import_module(f".{module_name}", __package__)

        attrs = [
            getattr(module, name) for name in dir(module) if not name.startswith("_")
        ]

        # debug print attrs
        print(f":: {__file__} {module_name}: {attrs}")

        # export attributes to this module
        for attr in attrs:
            globals()[attr.__name__] = attr


auto_import()
