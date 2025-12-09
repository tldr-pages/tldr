# pip cache

> Inspect and manage pip's wheel cache.
> More information: <https://pip.pypa.io/en/stable/cli/pip_cache/>.

- Show the location of the pip cache directory:

`pip cache dir`

- List filenames of all packages currently stored in the cache:

`pip cache list`

- Remove all files from the pip cache:

`pip cache purge`

- Remove cached files matching a specific package name:

`pip cache remove {{package_name}}`
