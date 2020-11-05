from pipeline.engines import engine
import os
import maya.cmds as cmds
import maya.mel as ml


class MayaEngine(engine.Engine):

    def open(self, path):   
        os.system(path)


    def Alembic_export(self, path):

        import subprocess  
        subprocess.call(["D:/installation/maya2019/Maya2019/bin/mayabatch.exe","-command", "python(\"execfile('D:/projets/artfx/TD4/py_dcc/alambic_exporter/exporterMaya.py')\");", path, "D:/projets/artfx/TD4/py_dcc/alambic_exporter/esportABC", "pSphere1"])
        
    def save(self, path):
        pass