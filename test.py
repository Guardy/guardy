import urllib
import re


def get_content(url):
    """
    get page html
    """
    return urllib.urlopen(url).read()


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


php()