"""
import sys

print ('starting up pipe config')

#if "\\multifct\tools\pipeline\global\packages" not in sys.path:
if "D:/projets/artfx/TD4/py_dcc" not in sys.path:

    #sys.path.append("\\multifct\tools\pipeline\global\packages")
    sys.path.append("D:/projets/artfx/TD4/py_dcc")

from pipeline.engines import engine

print ('done pipeline config')

"""



import sys
print('Starting up Pipeline in Houdini')

here = hou.getenv('HOUDINI_SCRIPT_PATH').split(';')[-1]   # os.path.dirname(__file__) not working in 456.py

deployment_root = here.split('/pipeline/')[0]
print('Script root {}'.format(deployment_root))

sys.path.append(deployment_root)  # path to pipeline 
sys.path.append(r'D:\projets\artfx\TD4\py_dcc\Qt.py-1.3.2')  # path to Qt package

print('Done Pipeline config')


try:
    import hou
    node = hou.node('obj')
    alembicImport = node.createNode('alembicarchive')
    parameter = alembicImport.parm('fileName')
    parameter.set('D:/projets/artfx/TD4/py_dcc/alambic_exporter/esportABC/pSphere1.abc')
    alembicImport.parm('buildHierarchy').pressButton()
except:
    print("No alembic(s) found to import")

