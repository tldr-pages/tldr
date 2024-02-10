# pbmupc

> Generate a PBM image of a Universal Product Code (UPC).
> More information: <https://netpbm.sourceforge.net/doc/pbmupc.html>.

- Generate a UPC image for the specified product type, manufacturer code, and product code:

`pbmupc {{product_type}} {{manufacturer_code}} {{product_code}} > {{path/to/output.pbm}}`

- Use an alternative style that does not display the checksum:

`pbmupc -s2 {{product_type}} {{manufacturer_code}} {{product_code}} > {{path/to/output.pbm}}`
