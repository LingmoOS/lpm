self.description = "package name with invalid characters cannot be installed"

sp = pmpkg("-foo")
self.addpkg2db("sync", sp)

self.args = "-S -- %s" % sp.name

self.addrule("!LPM_RETCODE=0")
self.addrule("!PKG_EXIST=-foo")
