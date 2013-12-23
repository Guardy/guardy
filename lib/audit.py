from software.models import Program
import subprocess
import re
import urllib


def use_bash(command, url):
    """
    bash command caller
    """
    bash_command = command + url
    process = subprocess.Popen(bash_command.split(), stdout=subprocess.PIPE)
    output = process.communicate()[0]
    return output


def get_content(url):
    """
    get page html
    """
    return urllib.urlopen(url).read()


def refresh_nginx(program):
    """
    getting nginx object with current version
    """
    version = None
    content = get_content(program.url).split('<center>')
    for elem in content:
        if 'Stable' in elem:
            for i in elem.split('<a'):
                if 'download' in i:
                    version = re.findall('>nginx-(.+)<', i)[0]
                    break
    if version:
        program.version = version


def refresh_apache(program):
    """
    getting apache object with current version
    """
    content = get_content(program.url)


def refresh_products():
    programs = Program.objects.all()
    for prog in programs:
        try:
            if prog.name == 'nginx':
                prog.refresh(refresh_nginx)
            elif prog.name == 'apache':
                prog.refresh(refresh_apache)
        except Exception, expt:
            pass


def audit(url):
    #output = use_bash('whatweb -a 3 ', url + ' --color=never').split(',')
    #print output
    #for line in output:
    #     if 'nginx[' in line:
	 #    cur_ver = re.findall('nginx\[(.+)\]',line)[0]
	 #    print cur_ver
	 #    print nginx_latest_version
    #         if StrictVersion(cur_ver) < StrictVersion(nginx_latest_version):
	 #        print 'Warning nginx is outdated!'

    refresh_products()
    print 'hip-hip'

    return 0


audit('k-m2.ru')

