import os
import subprocess
import re
from distutils.version import StrictVersion
import pycurl
from StringIO import StringIO
##################### FOR Proof Of Concept ONLY#####################

# f = open('/tmp/nginx_ver','r')
# text = f.read()
# text = text.split('<center>')
# f.close()
# version = ''
#
# for elem in text:
#     if 'Stable' in elem:
#         for i in elem.split('<a'):
#             if 'download' in i:
#                 version = re.findall('>nginx-(.+)<',i)[0]
#         break
# nginx_latest_version = version

##################################

### Snachala privodim vvedenii na saite url k nujnomy vidy



### Funkciya vizova bash comand
def use_bash(command,url):
    bashCommand = command + url
    input = bashCommand
    process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
    output = process.communicate()[0]
    return (output)


def check_version(product_name):
    c = pycurl.Curl()
    url = ''
    version = 'fuck'
    output = StringIO()
    c.setopt(c.WRITEFUNCTION, output.write)
    if product_name == 'nginx':
        url = 'nginx.org/en/download.html'
        c.setopt(c.URL,url)
        c.perform()
        c.close()
        content = output.getvalue()
        content = content.split('<center>')
        for elem in content:
            if 'Stable' in elem:
                for i in elem.split('<a'):
                    if 'download' in i:
                        version = re.findall('>nginx-(.+)<',i)[0]
                        break
    elif product_name == 'apache':
        url = 'httpd.apache.org/download.cgi'
        c.setopt(c.URL,url)
        c.perform()
        c.close()
        content = output.getvalue()
        content = content.split('<h1')

        print content[1]

    print version
    return version


def audit(url):
    output = use_bash('whatweb -a 3 ', url + ' --color=never').split(',')
    print output
    # for line in output:
    #     if 'nginx[' in line:
	 #    cur_ver = re.findall('nginx\[(.+)\]',line)[0]
	 #    print cur_ver
	 #    print nginx_latest_version
    #         if StrictVersion(cur_ver) < StrictVersion(nginx_latest_version):
	 #        print 'Warning nginx is outdated!'
		#
    for elem in output:


    return


audit('k-m2.ru')

