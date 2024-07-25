self.description = "Get info on package from a sync db"

sp = pmpkg("dummy")
sp.files = ["bin/dummy",
            "usr/man/man1/dummy.1"]
sp.desc = "test description"
sp.groups = ["foo"]
sp.url = "http://www.lingmo.org"
sp.license = "GPL2"
sp.arch = "i686"
sp.packager = "Lingmo OS"
sp.md5sum = "00000000000000000000000000000000"

self.addpkg2db("sync", sp)

self.args = "-Si %s" % sp.name

self.addrule("LPM_RETCODE=0")
self.addrule("LPM_OUTPUT=^Name.*%s" % sp.name)
self.addrule("LPM_OUTPUT=^Description.*%s" % sp.desc)
