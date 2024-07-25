self.description = "refresh databases with Optional siglevel"
self.require_capability("curl")

p1 = pmpkg('pkg1', '1.0-1')
self.addpkg2db('sync', p1)

self.db['sync'].option['SigLevel'] = ["Optional"]

self.args = '-Syy'

self.addrule("LPM_RETCODE=0")
