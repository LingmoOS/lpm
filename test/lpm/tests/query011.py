self.description = "Query info on a package (optdep install status [installed])"

optstr = "dep: for foobar"

pkg = pmpkg("dummy", "1.0-2")
pkg.optdepends = [optstr]
self.addpkg2db("local", pkg)

dep = pmpkg("dep")
self.addpkg2db("local", dep)

self.args = "-Qi %s" % pkg.name

self.addrule("LPM_RETCODE=0")
self.addrule("LPM_OUTPUT=^Optional Deps.*%s \[installed\]$" % optstr)
