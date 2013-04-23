import urllib2
import settings

org_urlopen = urllib2.urlopen
def monkey(url, data=None, timeout=None):
    if timeout is None:
        timeout = settings.TIMEOUT
    return org_urlopen(url, data, timeout)
urllib2.urlopen = monkey
