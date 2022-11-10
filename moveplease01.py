#!/usr/bin/env python3
import shutil
import os
os.chdir('/home/student/mycode/') # move in this dir
shutil.move('raynor.obj', 'ceph_storage/') # move raynor.obj into ceph_storage
xname = input('What is the new name for kerrigan.obj? ') # Takes new name 
shutil.move('ceph_storage/kerrigan.obj', 'ceph_storage/' + xname)

