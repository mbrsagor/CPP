import os
import dbm
import pickle

# Current working dictionary
cwd = os.getcwd()
print(cwd)

html = os.path.abspath('index.html')
print(html)

# True False
path = os.path.isdir('/Users/macair/PycharmProjects/pyLearn/think_python/Iteration')
print(path)
new_path = os.path.isdir('/Users/macair/PycharmProjects/pyLearn/think_python/Iteration/new_path')
print(new_path)

check_dir = os.listdir(cwd)
print(check_dir)

db = dbm.open('captions', 'c')
print(db)

t = [1, 2, 3]
t1 = pickle.dumps(t)
print(t1)

file_name = 'book.txt'
cmd = 'md5sum ' + file_name
fp = os.popen(cmd)
res = fp.read()
stat = fp.close()
print(res)
print(stat)
