# aurpublish

> Publish Arch User Repository packages.
> More information: <https://github.com/eli-schwartz/aurpublish>.

- Verify `PKGBUILD` integrity, generate `.SRCINFO`, create a commit message template, and publish the package to the AUR:

`aurpublish {{package_name}}`

- Add githooks to the current repository:

`aurpublish setup`
