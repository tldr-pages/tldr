# eol

> Show end-of-life dates (EoLs) for a number of products.
> More information: <https://github.com/hugovk/norwegianblue#example-command-line-use>.

- List all available products:

`eol`

- Get EoLs of one or more products:

`eol {{product1 product2 ...}}`

- Open the product webpage:

`eol {{product}} {{[-w|--web]}}`

- Get EoLs of a one or more products in a specific format:

`eol {{product1 product2 ...}} --{{html|json|md|markdown|pretty|rst|csv|tsv|yaml}}`

- Get EoLs of one or more products as a single markdown file:

`eol {{product1 product2 ...}} --{{markdown}} > {{eol_report.md}}`

- Display help:

`eol {{[-h|--help]}}`
