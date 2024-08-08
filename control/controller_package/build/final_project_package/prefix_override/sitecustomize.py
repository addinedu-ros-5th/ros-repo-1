import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/aa/dev_ws/AIE_Final-main/control/controller_package/install/final_project_package'
