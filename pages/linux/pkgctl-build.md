# pkgctl build

> Build packages inside a clean `chroot`.
> More information: <https://man.archlinux.org/man/pkgctl-build.1>.

- Automatically choose the right build script to build in a clean `chroot`:

`pkgctl build`

- Manually choose the right build script to build in a clean `chroot`:

`pkgctl build --arch {{architecture}} --repo {{repository}} --clean`
