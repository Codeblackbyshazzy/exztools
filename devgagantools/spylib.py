import warnings
from exztools.exzlib import *

warnings.warn(
    "devgagantools.spylib is deprecated and has been renamed to exztools.exzlib. "
    "Please update your imports as this shim will be removed in a future version.",
    DeprecationWarning,
    stacklevel=2
)
