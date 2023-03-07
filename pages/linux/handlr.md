# handlr

> Manage your default applications.
> More information: <https://github.com/chmln/handlr>.

- Open a URL in the default application:

`handlr open {{https://example.com}}`

- Open a PDF in the default PDF viewer:

`handlr open {{path/to/pdf}}`

- Set imv as the default handler for PNG images:

`handlr set {{.png}} {{imv.desktop}}`

- Set NeoVim as a wildcard handler for all text files:

`handlr set {{'text/*'}} {{nvim.desktop}}`

- Set the default handler based on mime-type:

`handlr set {{application/pdf}} {{evince.desktop}}`

- List all default apps:

`handlr list`

- Get the default handler for PNG images:

`handlr get {{.png}}`
