self.description = "Make sure ldconfig runs on an upgrade operation"

p = pmpkg("dummy")
self.addpkg(p)

self.args = "-U %s" % p.filename()

self.addrule("LPM_RETCODE=0")
self.addrule("FILE_EXIST=etc/ld.so.cache")
