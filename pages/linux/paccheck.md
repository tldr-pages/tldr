# paccheck

> Check installed packages on an Arch-based system to verify dependencies, integrity, and consistency.
> More information: <https://github.com/andrewgregory/pacutils/blob/master/doc/paccheck.pod>.

- List and check all installed packages:

`paccheck`

- Check the specified packages:

`paccheck {{package1 package2 ...}}`

- Only display messages if a problem is found:

`paccheck --quiet`

- Check that all package dependencies are satisfied:

`paccheck --depends`

- Display help:

`paccheck --help`

- Display version:

`paccheck --version`
