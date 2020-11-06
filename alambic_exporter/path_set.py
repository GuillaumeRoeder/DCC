import maya.cmds as cmds
import sys

cmds.file(sys.argv, o=True )
print("SYSTEME ARG : "  sys.argv)