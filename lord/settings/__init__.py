from lord.settings.base import *

try:
    from lord.settings.local import *

    live = False

except ImportError:

    live = True

if live:
    from lord.settings.production import *
