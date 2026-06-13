# debchange

> Maintain the debian/changelog file of a Debian source package.
> More information: <https://manned.org/debchange>.

- Add a new version for a non-maintainer upload to the changelog:

`debchange {{[-n|--nmu]}}`

- Add a changelog entry to the current version:

`debchange {{[-a|--append]}}`

- Add a changelog entry to close the bug with specified ID:

`debchange --closes {{bug_id}}`
