# uuencode

> Codificați fișierele binare în ASCII pentru transport prin medii care acceptă doar codificarea ASCII simplă.
> Mai multe informaţii: <https://manned.org/uuencode>

- Codificați un fișier și imprimați rezultatul la stdout:

`uuencode {{path/to/input_file}} {{output_file_name_after_decoding}}`

- Codificați un fișier și scrieți rezultatul într-un fișier:

`uuencode -o {{path/to/output_file}} {{path/to/input_file}} {{output_file_name_after_decoding}}`

- Codificați un fișier utilizând Base64 în loc de codificarea implicită uuuencode și scrieți rezultatul într-un fișier:

`uuencode -m -o {{path/to/output_file}} {{path/to/input_file}} {{output_file_name_after_decoding}}`
