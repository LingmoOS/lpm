self.description = "Query info on a package (new date)"

p = pmpkg("foobar")
p.files = ["bin/foobar"]
p.desc = "test description"
p.groups = ["foo"]
p.url = "http://www.lingmo.org"
p.license = "GPL2"
p.arch = "i686"
# test new style date
p.builddate = "1196640127"
p.packager = "Lingmo OS"

self.addpkg2db("local", p)

self.args = "-Qi %s" % p.name

self.addrule("LPM_RETCODE=0")
self.addrule("LPM_OUTPUT=^Name.*%s" % p.name)
self.addrule("LPM_OUTPUT=^Description.*%s" % p.desc)
self.addrule("LPM_OUTPUT=^Build Date.* 2007")
