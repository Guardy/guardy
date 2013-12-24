import re
import urllib

def refresh_nginx(program):
    """
    getting nginx object with current version
    """
    version = None
    content = urllib.urlopen(program.url).read().split('<center>')
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
    version = None
    content = urllib.urlopen(program.url).read().split('<p')
    for elem in content:
        if 'Stable Release - Latest Version' in elem:
            version = re.findall('">(.+)</a', elem)[0]
            break
    if version:
        program.version = version