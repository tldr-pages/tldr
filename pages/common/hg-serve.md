# hg serve

> Start a standalone Mercurial web server for browsing repositories.
> More information: <https://www.mercurial-scm.org/help/commands/serve>.

- Start a web server instance:

`hg serve`

- Start a web server instance on the specified port:

`hg serve {{[-p|--port]}} {{port}}`

- Start a web server instance on the specified listening address:

`hg serve {{[-a|--address]}} {{address}}`

- Start a web server instance with a specific identifier:

`hg serve {{[-n|--name]}} {{name}}`

- Start a web server instance using the specified theme (see the templates directory):

`hg serve --style {{style}}`

- Start a web server instance using the specified SSL certificate bundle:

`hg serve --certificate {{path/to/certificate}}`
