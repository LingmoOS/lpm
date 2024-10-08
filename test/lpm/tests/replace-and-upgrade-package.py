self.description = 'Simultaneously replace and upgrade a package'

# replacement package
sp1 = pmpkg('foo1', '1-2')
sp1.replaces = ['foo=1-1']
sp1.conflicts = ['foo=1-1']
self.addpkg2db('sync', sp1)

# upgrade package
sp2 = pmpkg('foo', '2-1')
self.addpkg2db('sync', sp2)

# depend on upgraded package to pull it into transaction
sp3 = pmpkg('bar', '1-1')
sp3.depends = [ 'foo=2-1' ]
self.addpkg2db('sync', sp3)

lp = pmpkg('foo', '1-1')
self.addpkg2db('local', lp)

self.args = "-Su bar"

self.addrule('LPM_RETCODE=0')
self.addrule('PKG_VERSION=foo1|1-2')
self.addrule('PKG_VERSION=foo|2-1')
self.addrule('PKG_VERSION=bar|1-1')
self.addrule('!LPM_OUTPUT=error')
