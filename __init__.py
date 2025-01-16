import sys
import threading
import time

import pcbnew

from .rt_export_plugin import RtExportPlugin

plugin = RtExportPlugin()
plugin.register()
