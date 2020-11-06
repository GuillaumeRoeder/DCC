import maya.cmds as cmds
from pipeline.engines import engine
import sys

cmds.loadPlugin( 'AbcExport.mll' )
cmds.file(sys.argv[3], o=True )
print("SYSTEME ARG!!!!!!!!!!!!!!!!!!!!!!!!!!! : " + str(sys.argv))
#cmds.file(r"D:\projets\artfx\TD4\py_dcc\scene_Test.mb", o=True )

selected_namespace = "namespace"

# Get all the object from the scene with the input namespace
namespace = "{}:*".format(selected_namespace)
nodes = cmds.ls(namespace, type='transform')


command_list = []
for node in nodes :
    print node
    command_list.append("-frameRange 1 25 -uvWrite -dataFormat ogawa -root {} -file D:/projets/artfx/TD4/py_dcc/alambic_exporter/esportABC/{}.abc".format(node, node.replace(':', '_')))


cmds.AbcExport( j =command_list, verbose=True)
