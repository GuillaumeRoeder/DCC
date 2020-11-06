print("IMPORT ABC IN HOUDINI")
import hou
import os
abc_files = os.listdir("D:/projets/artfx/TD4/py_dcc/alambic_exporter/esportABC")
print(os.listdir("D:/projets/artfx/TD4/py_dcc/alambic_exporter/esportABC"))


obj = hou.node('obj')
geo = obj.createNode('geo')

for abc in abc_files:
	alembic_node = geo.createNode('alembic')

	parameter = alembic_node.parm('fileName')
	parameter.set('D:/projets/artfx/TD4/py_dcc/alambic_exporter/esportABC/{}'.format(abc))
	#alembicImport.parm('buildHierarchy').pressButton()

	alembic_node.setCurrent(True, clear_all_selected=False)



merge = geo.createNode('merge')

geo.layoutChildren()
selected = hou.selectedNodes()

for node in selected:
    merge.setNextInput(node)


merge.setDisplayFlag(True)
merge.setRenderFlag(True)
merge.moveToGoodPosition()


hou.hipFile.save(file_name=None, save_to_recent_files=True)

print("FINISH IMPORT ABC IN HOUDINI")
