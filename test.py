import urllib
import re
from django.core.validators import URLValidator
from django.core.exceptions import ValidationError
import subprocess
from distutils.version import StrictVersion


def get_content(url):
    """
    get page html
    """
    return urllib.urlopen(url).read()


def use_bash(command, url):
    """
    bash command caller
    """
    bash_command = command + url
    process = subprocess.Popen(bash_command.split(), stdout=subprocess.PIPE)
    output = process.communicate()[0]
    return output


def test():
    version = None
    content = get_content('http://httpd.apache.org/download.cgi').split('<p')
    for elem in content:
        if 'Stable Release - Latest Version' in elem:
            version = re.findall('">(.+)</a',elem)[0]
            break

    return version

def php():
    version = []
    content = get_content('http://www.php.net/downloads.php').split('<h3')
    for elem in content:
        if 'Current Stable' in elem:
            try:
                version.append(re.findall('id="v(.+)"\s',elem)[0])
            except:
                pass
        elif 'Old Stable' in elem:
            try:
                version.append(re.findall('id="v(.+)"\s',elem)[0])
            except:
                pass
    print version



    return


def check_url(user_input):
    try:
        URLValidator(user_input)
        return user_input
    except ValidationError:
        print 'url is invalid'
        return None



def site_audit(url):
    '''
    perform site audit
    '''
    result = None
    if check_url(url):
        result = use_bash('whatweb ', url+' --colour never')
        result = parse_result(result)
        print result
    return result


def parse_result(unparsed):
    '''
    parse result of command execution
    '''
    http_server = 'Unknown'
    http_server_version = ''
    php_version = ''
    parsed = {}
    unparsed = unparsed.split(',')
    for elem in unparsed:
        # Parsing http server
        if 'HTTPServer' in elem:
            if 'Apache' in elem:
                http_server = 'apache'
            if 'nginx' in elem:
                http_server = 'nginx'
            if '/' in elem:
                http_server_version = elem.split('/')[1].split()[0]
            parsed.update({http_server:http_server_version})
        # Parsing PHP
        if 'PHP[' in elem:
            php_version = re.findall('\[(.+)\]',elem)[0]
            parsed.update({'php':php_version})

    return parsed


site_audit('k-m2.ru')


