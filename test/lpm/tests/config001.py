self.description = "Quick check for Include being parsed in [options]"

self.option['Include'] = ['/dev/null']

p = pmpkg("foobar")
p.files = ["bin/foobar"]
p.desc = "test description"
p.groups = ["foo"]
p.url = "http://www.lingmo.org"
p.license = "GPL2"
p.arch = "i686"

self.addpkg2db("local", p)

self.args = "-Qi %s" % p.name

self.addrule("LPM_RETCODE=0")
