self.description = "dir->file change during package upgrade (filesystem directory conflict)"

lp1 = pmpkg("pkg1")
lp1.files = ["dir/"]
self.addpkg2db("local", lp1)

self.filesystem = ["dir/conflict/"]

p = pmpkg("pkg1", "1.0-2")
p.files = ["dir"]
self.addpkg2db("sync", p)

self.args = "-S pkg1"

self.addrule("LPM_RETCODE=1")
self.addrule("PKG_VERSION=pkg1|1.0-1")
self.addrule("DIR_EXIST=dir/conflict/")
