# debchange

> Tool for maintenance of the debian/changelog file in a Debian source package.
> More information: <https://manpages.debian.org/debchange>.

- Add a new version for a non-maintainer upload to the changelog:

`debchange --nmu`

- Add a changelog entry to the current version:

`debchange --append`

- Add a changelog entry to close the bug with specified ID:

`debchange --closes {{bug_id}}`
