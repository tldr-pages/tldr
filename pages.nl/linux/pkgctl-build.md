# pkgctl build

> Bouw pakketten in een schone `chroot`.
> Meer informatie: <https://man.archlinux.org/man/pkgctl-build.1>.

- Kies automatisch het juiste build script om pakketten in een schone `chroot` te bouwen:

`pkgctl build`

- Bouw pakketten handmatig in een schone `chroot`:

`pkgctl build --arch {{architecture}} --repo {{repository}} --clean`
