from importlib.metadata import PackageNotFoundError, version

#from CWMSpy.cwms_loc import *
#from CWMSpy.cwm,s_ts import *
#from CWMSpy.utils import *
from .core import CWMS

try:
    __version__ = version('cwms-python')
except PackageNotFoundError:
    __version__ = 'version-unknown'
