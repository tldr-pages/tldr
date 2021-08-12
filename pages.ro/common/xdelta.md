# xdelta

> Utilitar de codificare Delta.
> Deseori se utilizează pentru aplicarea de patch-uri la fișierele binare.
> Mai multe informaţii: <http://xdelta.org>

- Aplicaţi un plasture:

`xdelta -d -s {{path/to/input_file}} {{path/to/delta_file.xdelta}} {{path/to/output_file}}`

- Creează un patch:

`xdelta -e -s {{path/to/old_file}} {{path/to/new_file}} {{path/to/output_file.xdelta}}`
