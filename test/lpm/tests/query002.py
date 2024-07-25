self.description = "Query info on a package"

p = pmpkg("foobar")
p.files = ["bin/foobar"]
p.desc = "test description"
p.groups = ["foo"]
p.url = "http://www.lingmo.org"
p.license = "GPL2"
p.arch = "i686"
p.packager = "Lingmo OS"

self.addpkg2db("local", p)

self.args = "-Qi %s" % p.name

self.addrule("LPM_RETCODE=0")
self.addrule("LPM_OUTPUT=^Name.*%s" % p.name)
self.addrule("LPM_OUTPUT=^Description.*%s" % p.desc)
