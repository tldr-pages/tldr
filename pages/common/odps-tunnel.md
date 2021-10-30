# odps tunnel

> Data tunnel in ODPS (Open Data Processing Service).
> See also `odps`.
> More information: <https://www.alibabacloud.com/help/doc-detail/27971.htm>.

- Download table to local file:

`tunnel download {{table_name}} {{file}};`

- Upload local file to a table partition:

`tunnel upload {{file}} {{table_name}}/{{partition_spec}};`

- Upload table specifying field and record delimiters:

`tunnel upload {{file}} {{table_name}} -fd {{field_delim}} -rd {{record_delim}};`

- Upload table using multiple threads:

`tunnel upload {{file}} {{table_name}} -threads {{num}};`
