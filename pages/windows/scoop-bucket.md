# scoop bucket

> A bucket is an application repository.
> Some buckets are already known to scoop, so you don't have to provide an url.
> More information: <https://github.com/lukesampson/scoop/wiki/Buckets>.

- List all buckets currently in use:

`scoop bucket list`

- List all known buckets:

`scoop bucket known`

- Add a known bucket by its name:

`scoop bucket add {{name}}`

- Add an unknown bucket by its name and Git repository url:

`scoop bucket add {{name}} {{repository}}`

- Remove a bucket by its name:

`scoop bucket rm {{name}}`
