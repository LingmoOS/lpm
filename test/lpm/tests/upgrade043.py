self.description = "Backup file relocation (reverse order)"

lp1 = pmpkg("bash")
lp1.files = ["etc/profile*"]
lp1.backup = ["etc/profile"]
self.addpkg2db("local", lp1)

p1 = pmpkg("bash", "1.0-2")
p1.depends = [ "filesystem" ]
self.addpkg(p1)

lp2 = pmpkg("filesystem")
self.addpkg2db("local", lp2)

p2 = pmpkg("filesystem", "1.0-2")
p2.files = ["etc/profile**"]
p2.backup = ["etc/profile"]
self.addpkg(p2)

self.args = "-U %s" % " ".join([p.filename() for p in (p1, p2)])

self.filesystem = ["etc/profile"]

self.addrule("LPM_RETCODE=0")
self.addrule("PKG_VERSION=bash|1.0-2")
self.addrule("PKG_VERSION=filesystem|1.0-2")
self.addrule("!FILE_PACSAVE=etc/profile")
self.addrule("FILE_PACNEW=etc/profile")
self.addrule("FILE_EXIST=etc/profile")
