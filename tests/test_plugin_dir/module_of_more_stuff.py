import argparse
# intentional duplicate w.r.t. "stuff" module.
from pathlib import Path  # noqa: F401
import tests.test_plugin_dir.module_of_stuff as module_of_stuff


class NewCustomType(argparse.ArgumentParser):
    ...


class AnotherDerived(module_of_stuff.ClassDefinition):
    def cool_thing(self) -> str:
        """ Some implementation, content doesn't matter. """


nct_type = type(NewCustomType)
