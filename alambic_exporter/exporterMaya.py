import maya.cmds as cmds
from pipeline.engines import engine
import sys


cmds.loadPlugin( 'AbcExport.mll' )
cmds.file(sys.argv[3], o=True )
print("SYSTEME ARG!!!!!!!!!!!!!!!!!!!!!!!!!!! : " + str(sys.argv))

#cmds.file(r"D:\projets\artfx\TD4\py_dcc\scene_Test.mb", o=True )

command = "-frameRange 1 25 -uvWrite -dataFormat ogawa -root " + engine.exportObjectName + " -file D:/projets/artfx/TD4/py_dcc/alambic_exporter/esportABC/" + engine.exportObjectName + ".abc"
cmds.AbcExport( j =command)
