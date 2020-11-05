import sys
sys.path.append(r'C:\Python27\Lib\site-packages')
sys.path.append(r'D:\projets\artfx\TD4\py_dcc\Qt.py-1.3.2')
from Qt import QtWidgets, QtCompat, QtGui
import os

ui_path = r'D:\projets\artfx\TD4\py_dcc\pipeline\ui\SaveAndOpen.ui'


objectName = "pSphere1.abc" # ajouter un champ dans la fenter pour le nom de l'objet ?


class Engine():
    def open(self, path):
        os.system(path)

    def Alembic_export(self, path):
        import subprocess  
        subprocess.call(["D:/installation/maya2019/Maya2019/bin/mayabatch.exe","-command", "python(\"execfile('D:/projets/artfx/TD4/py_dcc/alambic_exporter/exporterMaya.py')\");", path, "D:/projets/artfx/TD4/py_dcc/alambic_exporter/esportABC", "pSphere1"])
        
    def save(self, path):
        pass



def get_current():
    engine = Engine()
    if 'Maya' in sys.executable:
        from pipeline.engines import Maya_Engine
        engine = Maya_Engine.MayaEngine()
        print(engine)
    if 'hou' in sys.executable:
        from pipeline.engines import Houdini_Engine
        engine = Houdini_Engine.HoudiniEngine()

    return engine



class MyWindow(QtWidgets.QMainWindow):
    
    def __init__(self):
        super(MyWindow, self).__init__()
        self.engine = get_current()        

        
        # setup ui
        QtCompat.loadUi(ui_path, self)

        self.Open_Button.clicked.connect(self.select)
        self.exportABC.clicked.connect(self.export)
        
    def select(self):
        print(" ENGINE IN USE: {}".format(self.engine) )
        fname, __ = QtWidgets.QFileDialog.getOpenFileName(self, 'Open file') # , 'c:\\') #,"Image files (*.jpg *.gif)")
        self.engine.open(fname)

    def export(self):
        print(" ENGINE IN USE: {}".format(self.engine) )
        fname, __ = QtWidgets.QFileDialog.getOpenFileName(self, 'Open file') # , 'c:\\') #,"Image files (*.jpg *.gif)")
        self.engine.Alembic_export(fname)
        



        


   

