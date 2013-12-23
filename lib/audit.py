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


class Product(object):
    """
    base product object
    """
    name = None
    url = None
    page = None
    version = None

    def __init__(self, name, url):
        self.name = name
        self.url = url
        self.page = get_content(url)


def get_nginx():
    """
    getting nginx object with current version
    """
    product = Product(name='nginx', url='nginx.org/en/download.html')
    content = product.page.split('<center>')
    for elem in content:
        if 'Stable' in elem:
            for i in elem.split('<a'):
                if 'download' in i:
                    product.version = re.findall('>nginx-(.+)<', i)[0]
                    break
    return product


def get_apache():
    """
    getting apache object with current version
    """
    product = Product(name='apache', url='httpd.apache.org/download.cgi')
    return  product


def get_products():
    nginx = get_nginx()
    apache = get_apache()
    return {
        nginx.name: nginx,
        apache.name: apache
    }


def audit(url):
    output = use_bash('whatweb -a 3 ', url + ' --color=never').split(',')
    print output
    #for line in output:
    #     if 'nginx[' in line:
	 #    cur_ver = re.findall('nginx\[(.+)\]',line)[0]
	 #    print cur_ver
	 #    print nginx_latest_version
    #         if StrictVersion(cur_ver) < StrictVersion(nginx_latest_version):
	 #        print 'Warning nginx is outdated!'

    products = get_products()
    print products

    return 0


audit('k-m2.ru')

