pkgname=lpm
pkgver=1.0.0
pkgrel=2
pkgdesc="The Lingmo OS Package Manager"
arch=('any')
url="https://github.com/LingmoOS/lpm"
license=('GPL-2.0')
source=("git+https://github.com/LingmoOS/$pkgname")
validpgpkeys=("FA4D355E2BE1BEF4A15D924EF1A83B6031E04C70")
sha256sums=('SKIP')

package() {
  cd "${pkgname}"
  meson build
  ninja -C build
		ninja -C build install
}
