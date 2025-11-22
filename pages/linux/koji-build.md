# koji build

> Build an RPM package.
> More information: <https://docs.pagure.org/koji>.

- Build a package from `src.rpm`:

`koji build {{target}} {{path/to/src.rpm}}`

- Build a package from a SCM (Source Code Management) URL:

`koji build {{target}} {{git+https://src.fedoraproject.org/rpms/vim.git#e847a50297a216229050bf4db3d06a139104e7cf}}`

- Perform a scratch build:

`koji build {{target}} {{path/to/src.rpm}} --scratch`

- Wait on the build, even if it's running in the background:

`koji build {{target}} {{path/to/src.rpm}} --wait`

- Don't wait on build:

`koji build {{target}} {{path/to/src.rpm}} --nowait`

- Display help:

`koji build {{[-h|--help]}}`
