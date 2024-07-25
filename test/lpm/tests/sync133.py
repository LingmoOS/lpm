self.description = "Sysupgrade with a sync package replacing a local one in 'IgnorePkg'"

sp = pmpkg("pkg2")
sp.replaces = ["pkg1"]

self.addpkg2db("sync", sp)

lp = pmpkg("pkg1")

self.addpkg2db("local", lp)

self.option["IgnorePkg"] = ["pkg1"]

self.args = "-Su"

self.addrule("LPM_RETCODE=0")
self.addrule("PKG_EXIST=pkg1")
self.addrule("!PKG_EXIST=pkg2")
