# pip index

> Inspect information available from package indexes.
> More information: <https://pip.pypa.io/en/stable/cli/pip_index/>.

- List all available versions of a package:

`pip index versions {{package}}`

- List versions from a specific index (`--index-url`):

`pip index versions {{package}} --index-url {{https://test.pypi.org/simple/}}`

- Include pre-release versions (`--pre`):

`pip index versions {{package}} --pre`

- Include an additional index (`--extra-index-url`):

`pip index versions {{package}} --extra-index-url {{https://example.com/simple/}}`

- Output versions in JSON format (`--format json`):

`pip index versions {{package}} --format json`

- List versions for a specific platform (`--platform`):

`pip index versions {{package}} --platform {{linux_x86_64}}`
