import os
import re

IDMATCH = re.compile(r'[a-z](?:-?[a-zA-Z0-9])*')

def objects(source):
    module = ''
    for line in source:
        match = IDMATCH.match(line)
        if match:
            yield module, match.group()
        else:
            if 'DEFINITION' in line:
                module = line[:line.find('DEFINITION')].strip()


def walkmibs(mibdir):
    for root, dirs, files in os.walk(mibdir):
        for filename in files:
            mibfile = open(os.path.join(root, filename))
            for module, oid in objects(mibfile):
                yield module, oid
