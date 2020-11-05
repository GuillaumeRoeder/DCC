print("CREATE SCENE")

import hou

file =  "D:/projets/artfx/TD4/py_dcc/save.hip"
hou.hipFile.save(file_name=file, save_to_recent_files=False)

print("SCENE CREATED")