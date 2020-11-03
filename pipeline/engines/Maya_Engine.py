from pipeline.engines import engine
import os
#import maya.standalone
#maya.standalone.initialize("Python")
import maya.cmds as cmds
import maya.mel as ml


##path = "C:/Users/guillaume/Documents/maya/projects/default/scenes/teste1.mb"

class MayaEngine(engine.Engine):

    def open(self, path):
    	
    	os.system(path)
    	#cmds.loadPlugin("Mayatomr")
    	#cmds.file(path, o=True )

        
    def save(self, path):
        pass