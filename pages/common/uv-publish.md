# uv publish

> Upload distributions to an index.
> More information: <https://docs.astral.sh/uv/reference/cli/#uv-publish>.

- Publish packages from `dist/` directory (default behavior):

`uv publish`

- Publish to a specific repository URL:

`uv publish --publish-url {{https://upload.pypi.org/legacy/}}`

- Publish using a specific username and password:

`uv publish {{[-u|--username]}} {{username}} {{[-p|--password]}} {{password}}`

- Publish using an API token:

`uv publish {{[-t|--token]}} {{your_api_token}}`

- Publish specific distribution files:

`uv publish {{path/to/dist/*.whl}} {{path/to/dist/*.tar.gz}}`

- Publish to TestPyPI for testing:

`uv publish --publish-url https://test.pypi.org/legacy/`
