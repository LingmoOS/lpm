self.description = "Get URL on package from a sync db"

sp = pmpkg("dummy")
sp.files = ["bin/dummy",
            "usr/man/man1/dummy.1"]
self.addpkg2db("sync", sp)

self.args = "-Sp %s" % sp.name

self.addrule("LPM_RETCODE=0")
self.addrule("LPM_OUTPUT=%s" % sp.name)
self.addrule("LPM_OUTPUT=file://")
