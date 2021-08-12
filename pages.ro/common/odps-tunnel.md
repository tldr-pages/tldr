# odps tunnel

> Tunel de date în ODPS (Serviciul de procesare a datelor deschise).
> A se vedea, de asemenea, `odps`.
> Mai multe informaţii: <https://www.alibabacloud.com/help/doc-detail/27971.htm>

- Descărcați tabelul în fișierul local:

`tunnel download {{table_name}} {{file}};`

- Încărcați fișierul local într-o partiție de tabel:

`tunnel upload {{file}} {{table_name}}/{{partition_spec}};`

- Încărcați tabelul specificând câmpurile și înregistrările delimitatoare:

`tunnel upload {{file}} {{table_name}} -fd {{field_delim}} -rd {{record_delim}};`

- Încărcați tabelul folosind mai multe fire:

`tunnel upload {{file}} {{table_name}} -threads {{num}};`
