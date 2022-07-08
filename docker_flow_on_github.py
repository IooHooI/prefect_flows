#--------------------------------------------------------------
# Imports
#--------------------------------------------------------------
 
# basic imports
import time

from prefect import Flow, Parameter, task

from prefect.storage.git import Git

from prefect.run_configs import DockerRun

# specific task class imports
from prefect.tasks.shell import ShellTask
 
 
#--------------------------------------------------------------
# Define custom task functions
#--------------------------------------------------------------
 
@task
def plus_one(x):
    """A task that adds 1 to a number"""
    time.sleep(30)
    
    print("FAIUBVAFIEVBAFRBEIUVYARBEIUVRABTSRVAIBSRVIASVUA")

    return x + 1
 
@task
def build_command(name):
    time.sleep(30)

    print("ABDHFCAJHBBFDSJVHAGSVFAHJGSVJAFSGVFAJHSFVAGHJSFHKVAFSKUVA")

    return 'echo "HELLO, {}!"'.format(name)
 
#--------------------------------------------------------------
# Instantiate task classes
#--------------------------------------------------------------
 
run_in_bash = ShellTask(name='run a command in bash')
 
#--------------------------------------------------------------
# Open a Flow context and use the functional API (if possible)
#--------------------------------------------------------------
 
with Flow('Best Practices (Docker, GitHub)') as flow:
    flow.run_config = DockerRun()
    
    flow.storage = Git(
            repo="IooHooI/prefect_flows",
            flow_path="docker_flow_on_github.py",
            repo_host="github.com",
            branch_name="main"
    )
    
    # store the result of each task call, even if you don't use the result again
    two = plus_one(1)
 
    # for clarity, call each task on its own line
    name = Parameter('name')
    cmd = build_command(name=name)
    shell_result = run_in_bash(command=cmd)
 
    # use the imperative API where appropriate
    shell_result.set_upstream(two)
