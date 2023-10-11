# eol

> Show end-of-life dates (EoLs) for a number of products.
> More information: <https://github.com/hugovk/norwegianblue>.

- List all available products:

`eol`

- Get EoLs of one or more products:

`eol {{product1 product2 ...}}`

- Open the product webpage:

`eol {{product}} --web`

- Get EoLs of a one or more products in a specific format:

`eol {{product1 product2 ...}} --format {{html|json|md|markdown|pretty|rst|csv|tsv|yaml}}`

- Get EoLs of one or more products as a single markdown file:

`eol {{product1 product2 ...}} --format {{markdown}} > {{eol_report.md}}`

- Display help:

`eol --help`
