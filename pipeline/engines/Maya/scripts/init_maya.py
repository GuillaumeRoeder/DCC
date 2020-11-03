#import sys
#sys.path.append(r"D:\projets\artfx\TD4\py_dc")



print('Starting up Python Pipeline in Maya')

import sys, os
here = os.path.dirname(__file__)

deployment_root = here.split('/pipeline/')[0]
print('Script root {}'.format(deployment_root))

sys.path.append(deployment_root)  # path to pipeline 
sys.path.append(r'D:\projets\artfx\TD4\py_dcc\Qt.py-1.3.2')  # path to Qt package

print('Done Pipeline config')