self.description = "Ensure we choose provider already in target list"

sp1 = pmpkg("pkg1")
sp1.depends = ["dep"]
self.addpkg2db("sync", sp1)

sp2 = pmpkg("pkg2")
sp2.provides = ["dep"]
self.addpkg2db("sync", sp2)

sp3 = pmpkg("pkg3")
sp3.conflicts = ["pkg2"]
sp3.provides = ["dep"]
self.addpkg2db("sync", sp3)

self.args = "-S pkg1 pkg2"

self.addrule("LPM_RETCODE=0")
self.addrule("PKG_EXIST=pkg1")
self.addrule("PKG_EXIST=pkg2")
self.addrule("!PKG_EXIST=pkg3")
