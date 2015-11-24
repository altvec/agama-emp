#!/usr/bin/env python2
from __future__ import print_function
from suds.client import Client

api = Client('http://ent:8080/ws/emp?WSDL')


def getProbesInGroup(group):
    return api.service.getProbesInGroup(group)


def getMetadataForProbes(group):
    return api.service.getMetadataForProbes(probes=probes,
                                            metadata_types=['stb_ip',
                                                            'lpi',
                                                            'latest_report'])

probes = getProbesInGroup("All")
# API can handle only 1000 probes at once, so we split probes into chunks
chunks = [probes[i:i+1000] for i in xrange(0, len(probes), 1000)]
f = open('output.txt', 'w')
for chunk in chunks:
    for probe in getMetadataForProbes(chunk):
        _id = probe["id"]
        _ip = probe["metadata"][0][1]
        lpi = probe["metadata"][1][1]
        print("%s %s %s" % (_id, _ip, lpi), file=f)
f.close()
