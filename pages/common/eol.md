> CLI to show end-of-life dates (EoLs) for a number of products.
> More information: <https://github.com/hugovk/norwegianblue>.

- List all available products:

`eol`

- Get EOLs of a given product:

`eol {{product}}`

- Open product webpage on EOL:

`eol {{product}} -w`

- Get EOLs of multiple products all at once:

`eol {{product1 product2 ...}}`

- Get EOLs of a product in a specific format:

`eol {{product}} -f {{html|json|md|markdown|pretty|rst|csv|tsv|yaml}}`

- Get EOLs of multiple products as a single markdown file:

`eol {{product1 product2 ...}} -f markdown > eol_report.md`

- Display help:

`eol --help`
