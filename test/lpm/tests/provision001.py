self.description = "-S provision"

sp = pmpkg("pkg1")
sp.provides = ["provision=1.0-1"]
self.addpkg2db("sync", sp)

self.args = "-S provision"

self.addrule("LPM_RETCODE=0")
self.addrule("PKG_EXIST=pkg1")
