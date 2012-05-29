#!/usr/bin/python

import os
import sys
from pysnmp.smi.builder import MibBuilder
from pysnmp.smi.view import MibViewController
from mibfind import mibcache, mibwalk

def main(args):
    mibdir = '/home/heillr10/jmibs'
    dbfile = '/home/heillr10/tmp/mibcache.db'
    cache = mibcache.MibCache(dbfile)
    entry = args[0]
    if not cache.checkmodule(entry):
        cache.saverows(mibwalk.walkmibs(mibdir))
    module = cache.checkmodule(entry)
    if not module:
        print "%s not found" % (entry)
        exit(1)
    print "%s::%s" % (module, entry)

if __name__ == "__main__":
    main(sys.argv[1:])
