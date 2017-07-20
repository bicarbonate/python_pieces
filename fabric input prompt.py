from fabric.operations import *

env.user = fabric.operations.prompt("What is your username?")
env.password = fabric.operations.prompt("What is your password?")
env.host = fabric.operations.prompt("What is your hostname?")