# csv2tsv

> Փոխարկեք CSV (ստորակետով բաժանված) տեքստը TSV (ներդիրներով առանձնացված) ձևաչափի:.
> Լրացուցիչ տեղեկություններ. <https://github.com/eBay/tsv-utils/blob/master/README.md#csv2tsv>:.

- Փոխարկել CSV-ից TSV.:

`csv2tsv {{path/to/input_csv1 path/to/input_csv2 ...}} > {{path/to/output_tsv}}`

- Փոխարկեք դաշտի սահմանազատիչն առանձնացված CSV-ին TSV.:

`csv2tsv -c'{{field_delimiter}}' {{path/to/input_csv}}`

- Ստորակետով անջատված CSV-ն փոխարկեք TSV-ի.:

`csv2tsv -c';' {{path/to/input_csv}}`
