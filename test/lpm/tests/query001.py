self.description = "Query a package"

p = pmpkg("foobar")
p.files = ["bin/foobar"]
self.addpkg2db("local", p)

self.args = "-Q %s" % p.name

self.addrule("LPM_RETCODE=0")
self.addrule("LPM_OUTPUT=^%s" % p.name)
