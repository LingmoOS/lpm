self.description = "Sysupgrade with a force and ignore on same package"

lp = pmpkg("dummy", "1.0-1")

self.addpkg2db("local", lp)

sp = pmpkg("dummy", "1:1.0-2")
self.addpkg2db("sync", sp)

self.args = "-Su --ignore %s" % lp.name

self.addrule("LPM_RETCODE=0")
self.addrule("PKG_VERSION=dummy|1.0-1")
