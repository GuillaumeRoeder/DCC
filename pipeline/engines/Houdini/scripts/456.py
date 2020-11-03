import sys

print ('starting up pipe config')

if "\\multifct\tools\pipeline\global\packages" not in sys.path:
    sys.path.append("\\multifct\tools\pipeline\global\packages")
    sys.path.append("D:\py_dcc")

from pipeline.engines import engine

print ('done pipeline config')