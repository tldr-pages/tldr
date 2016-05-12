# odps tunnel

> Data tunnel in ODPS (Open Data Processing Service).

- Download table to local file:

`tunnel download {{table_name}} {{file}};`

- Upload local file to a table parition:

`tunnel upload {{file}} {{table_name}}/{{partition_spec};`

- Upload table with specifying field and record delimiters:

`tunnel upload {{file}} {{table_name}} -fd {{field_delim}} -rd {{record_delim}};`

- Upload table using multi-threads:

`tunnel upload {{file}} {{table_name}} -threads {{num}};`
