print("IMPORT ABC IN HOUDINI")

import hou
node = hou.node('obj')
alembicImport = node.createNode('alembicarchive')


parameter = alembicImport.parm('fileName')
parameter.set('D:/projets/artfx/TD4/py_dcc/alambic_exporter/esportABC/pSphere1.abc')
alembicImport.parm('buildHierarchy').pressButton()


hou.hipFile.save(file_name=None, save_to_recent_files=True)

print("FINISH IMPORT ABC IN HOUDINI")