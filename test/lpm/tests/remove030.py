self.description = "Remove a package in HoldPkg"

p1 = pmpkg("dummy")
self.addpkg2db("local", p1)

self.option["HoldPkg"] = ["dummy"]

self.args = "-R %s" % p1.name

self.addrule("LPM_RETCODE=1")
self.addrule("PKG_EXIST=dummy")
