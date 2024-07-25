self.description = "Hook using multiple 'Exec's"

self.add_hook("hook",
        """
        [Trigger]
        Type = Package
        Operation = Install
        Target = foo

        [Action]
        When = PostTransaction
        Exec = /bin/date
        Exec = /bin/date
        """);

sp = pmpkg("foo")
self.addpkg2db("sync", sp)

self.args = "-S foo"

self.addrule("LPM_RETCODE=0")
self.addrule("LPM_OUTPUT=warning.*overwriting previous definition of Exec")
