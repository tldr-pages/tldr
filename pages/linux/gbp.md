# gbp

> A system to integrate the Debian package build system with Git.
> More information: <http://honk.sigxcpu.org/projects/git-buildpackage/manual-html/gbp.html>.

- Convert an existing Debian package to gbp:

`gbp import-dsc {{software_0.1-2.dsc}}`

- Build a package using the default builder (`debuild`):

`gbp buildpackage -jauto -us -uc`

- Build a package in a `pbuilder` environment for Debian Bullseye:

`DIST={{bullseye}} ARCH={{amd64}} gbp buildpackage -jauto -us -uc --git-builder={{git-pbuilder}}`

- Specify that this is a source-only upload in the `.changes` file (see https://wiki.debian.org/SourceOnlyUpload):

`gbp buildpackage -jauto -us -uc --changes-options={{-S}}`

- Import a new upstream release:

`gbp import-orig --pristine-tar {{software-0.1.tar.gz}}`
