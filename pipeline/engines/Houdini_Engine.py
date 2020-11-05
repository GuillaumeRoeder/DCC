from pipeline.engines import engine
import hou 
import os


class HoudiniEngine(engine.Engine):

    def open(self, path):
    	os.system(path)
        

        pass

    def save(self, path):
        pass