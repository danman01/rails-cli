#!/usr/bin/env python
import subprocess
PROJECT_NAME = 'rails-cli'

def build:
'''angular deploy script, wrapped in python runner'''
  cmd = "ng build --prod --output-path docs --base-href /${PROJECT_NAME}/"
  subprocess.run(cmd)

build()
