import sys
sys.path.append(r'C:\Python27\Lib\site-packages')
sys.path.append(r'D:\projets\artfx\TD4\py_dcc\Qt.py-1.3.2')
from Qt import QtWidgets, QtCompat, QtGui


ui_path = r'D:\projets\artfx\TD4\py_dcc\pipeline\ui\SaveAndOpen.ui'





class Engine():
    def open(self, path):
        pass
        
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
        #self.SelectedEngine = engine
        #print(self.SelectedEngine)
        self.engine = get_current()
        

        # setup ui
        QtCompat.loadUi(ui_path, self)


        self.Open_Button.clicked.connect(self.select)
        
    def select(self):
        fname, __ = QtWidgets.QFileDialog.getOpenFileName(self, 'Open file') # , 'c:\\') #,"Image files (*.jpg *.gif)")
        self.engine.open(fname)

        


   

