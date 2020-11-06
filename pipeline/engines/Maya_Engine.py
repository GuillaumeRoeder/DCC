from pipeline.engines import engine
import os
import maya.cmds as cmds




class MayaEngine(engine.Engine):

    def open(self, path):   
        os.system(path)


    def Alembic_export(self, path):

        import subprocess  
        subprocess.call(["D:/installation/maya2019/Maya2019/bin/mayabatch.exe","-command", "python(\"execfile('./alambic_exporter/exporterMaya.py')\");", path])

        subprocess.call(["D:/installation/houdini_non_com/bin/hython.exe", "./alambic_exporter/create_scene.py"])
        subprocess.call(["D:/installation/houdini_non_com/bin/hython.exe", "./save.hip", "./alambic_exporter/import_script.py"])

                
    def save(self, path):
        pass