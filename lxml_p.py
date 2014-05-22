import os
import sys

from lxml import etree

def get_producturls(f):
    parser = etree.iterparse(f, tag='ProductUrl')

    for _, element in parser:
        print (element.text)
        element.clear()


def entry_point(argv):
    if len(argv) != 2:
        print ("Usage: %s <file>" % argv[0])
        return 1

    f = open(argv[1], 'rb')
    get_producturls(f)
    f.close()
    return 0


if __name__ == '__main__':
    entry_point(sys.argv)
