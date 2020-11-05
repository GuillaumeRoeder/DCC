import maya.cmds as cmds
from pipeline.engines import engine


cmds.loadPlugin( 'AbcExport.mll' )
cmds.file(r"D:\projets\artfx\TD4\py_dcc\scene_Test.mb", o=True )
command = "-frameRange 1 25 -uvWrite -root pSphere1 -file D:/projets/artfx/TD4/py_dcc/alambic_exporter/esportABC/" + engine.objectName
cmds.AbcExport( j =command)
