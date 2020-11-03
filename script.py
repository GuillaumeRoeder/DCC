import sys

sys.path.append("D:\projets\artfx\TD4\py_dcc")

from pipeline.engines import engine
from Qt import QtWidgets

app = QtWidgets.QApplication(sys.argv)

engine.get_current()

win = engine.MyWindow()
win.show()

app.exec_()

