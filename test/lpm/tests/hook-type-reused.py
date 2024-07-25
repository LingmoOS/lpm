self.description = "Hook using multiple 'Type's"

self.add_hook("hook",
        """
        [Trigger]
        Type = Package
        Type = Path
        Operation = Install
        Target = foo

        [Action]
        When = PostTransaction
        Exec = /bin/date
        """);

sp = pmpkg("foo")
self.addpkg2db("sync", sp)

self.args = "-S foo"

self.addrule("LPM_RETCODE=0")
self.addrule("LPM_OUTPUT=warning.*overwriting previous definition of Type")
