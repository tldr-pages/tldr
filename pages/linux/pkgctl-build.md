# pkgctl build

> Build packages inside a clean `chroot`.
> More information: <https://man.archlinux.org/man/pkgctl-build.1>.

- Automatically choose the right build script to build packages in a clean `chroot`:

`pkgctl build`

- Manually build packages in a clean `chroot`:

`pkgctl build --arch {{architecture}} --repo {{repository}} --clean`
