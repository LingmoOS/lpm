pkgname=lpm
pkgver=1.0.0
pkgrel=1
pkgdesc="The Lingmo OS Package Manager"
arch=('x86_64')
url="https://github.com/LingmoOS/lpm"
license=('GPL-2.0-or-later')
# depends=('bash' 'glibc' 'libarchive' 'curl' 'gpgme' 'pacman-mirrorlist'
#         'gettext' 'gawk' 'coreutils' 'gnupg' 'grep')
# makedepends=('meson' 'asciidoc' 'doxygen')
# checkdepends=('python' 'fakechroot')
# optdepends=('perl-locale-gettext: translation support in makepkg-template')
provides=('libalpm.so')
backup=(etc/lpm.conf
        etc/makepkg.conf)
options=('strip')
validpgpkeys=('AC17B9A7557CB5B0EBFFDA80FA3A5CC90C59CA75')
source=("git+https://github.com/LingmoOS/lpm")
sha256sums=('SKIP')

build() {
  cd "$pkgname"
  meson --prefix=/usr \
        --buildtype=plain \
        -Ddoc=enabled \
        -Ddoxygen=enabled \
        -Dscriptlet-shell=/usr/bin/bash \
        -Dldconfig=/usr/bin/ldconfig \
        build

  meson compile -C build
}

# check() {
#   cd "$pkgname"

#   meson test -C build
# }

package() {
  cd "$pkgname"

  DESTDIR="$pkgdir" meson install -C build

  # install Arch specific stuff
  install -dm755 "$pkgdir/etc"
  install -m644 "$srcdir/pacman.conf" "$pkgdir/etc"
  install -m644 "$srcdir/lpm.conf" "$pkgdir/etc"

  local wantsdir="$pkgdir/usr/lib/systemd/system/sockets.target.wants"
  install -dm755 "$wantsdir"

  local unit
  for unit in dirmngr gpg-agent gpg-agent-{browser,extra,ssh} keyboxd; do
    ln -s "../${unit}@.socket" "$wantsdir/${unit}@etc-pacman.d-gnupg.socket"
  done
}

# vim: set ts=2 sw=2 et:
