'''some module'''

import sys
import subprocess

for arg in sys.argv:
    print('arg:{arg}'.format(arg=arg))

project_name = sys.argv[1]

def build(project):
    '''angular deploy script, wrapped in python runner'''
    cmd = 'ng build --prod --output-path docs --base-href /{project}/'.format(project=project)
    subprocess.run(cmd)

build(project_name)

# progress bar:
# from tqdm import tqdm
# wrap any iterable in tqdm:
# for key in tqdm(range(26)):
