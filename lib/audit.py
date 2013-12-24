from software.models import Program
import subprocess


def use_bash(command, url):
    """
    bash command caller
    """
    bash_command = command + url
    process = subprocess.Popen(bash_command.split(), stdout=subprocess.PIPE)
    output = process.communicate()[0]
    return output


def audit():
    """
    debug
    """
    all_programs = Program.objects.all()
    for prog in all_programs:
        try:
            prog.refresh()
        except Exception, expt:
            print(expt)
            pass

    print 'hip-hip'

audit()