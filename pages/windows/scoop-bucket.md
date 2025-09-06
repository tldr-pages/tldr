# scoop bucket

> Manage buckets: Git repositories containing files which describe how scoop installs applications.
> If Scoop doesn't know where the bucket is located its repository location must be specified.
> More information: <https://github.com/lukesampson/scoop/wiki/Buckets>.

- List all buckets currently in use:

`scoop bucket list`

- List all known buckets:

`scoop bucket known`

- Add a known bucket by its name:

`scoop bucket add {{name}}`

- Add an unknown bucket by its name and Git repository URL:

`scoop bucket add {{name}} {{https://example.com/repository.git}}`

- Remove a bucket by its name:

`scoop bucket rm {{name}}`
