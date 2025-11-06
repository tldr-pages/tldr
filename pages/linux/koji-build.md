# koji build

> Build an RPM package.
> More information: <https://docs.pagure.org/koji>.

- Build a package from `src.rpm`:

`koji build {{target}} {{path/to/src.rpm}}`

- Build a package from a SCM (Source Code Management) URL:

`koji build {{target}} {{git+https://src.fedoraproject.org/rpms/vim.git#e847a50297a216229050bf4db3d06a139104e7cf}}`

- Perform a scratch build:

`koji build --scratch {{target}} {{path/to/src.rpm}}`

- Wait on the build, even if it's running in the background:

`koji build --wait {{target}} {{path/to/src.rpm}}`

- Don't wait on build:

`koji build --nowait {{target}} {{path/to/src.rpm}}`

- Display help:

`koji build --help`
