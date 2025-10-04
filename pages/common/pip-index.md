# pip index

> Inspect information available from package indexes.
> Useful for finding available package versions without installing.
> More information: <https://pip.pypa.io/en/stable/cli/pip_index/>.

- List all available versions of a package:

`pip index versions {{package}}`

- List versions from a specific index:

`pip index versions {{package}} --index-url {{https://test.pypi.org/simple/}}`

- List versions including pre-releases:

`pip index versions {{package}} --pre`

- List versions from an additional index:

`pip index versions {{package}} --extra-index-url {{https://example.com/simple/}}`

- List versions in JSON format:

`pip index versions {{package}} --format json`

- List versions for a specific platform:

`pip index versions {{package}} --platform {{linux_x86_64}}`
