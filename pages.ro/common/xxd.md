# xxd

> Creați o reprezentare hexazecimală (hexdump) dintr-un fișier binar sau invers.

- Generați un hexdump dintr-un fișier binar și afișați ieșirea:

`xxd {{input_file}}`

- Generați un hexdump dintr-un fișier binar și salvați-l ca fișier text:

`xxd {{input_file}} {{output_file}}`

- Afișați o ieșire mai compactă, înlocuind zerouri consecutive (dacă există) cu o stea:

`xxd -a {{input_file}}`

- Afișează ieșirea cu 10 coloane de câte un octet (octet) fiecare:

`xxd -c {{10}} {{input_file}}`

- Afișează ieșire numai până la o lungime de 32 octeți:

`xxd -l {{32}} {{input_file}}`

- Afișează ieșirea în modul simplu, fără goluri între coloane:

`xxd -p {{input_file}}`

- Reveniți un hexdump text simplu înapoi în binar și salvați-l ca fișier binar:

`xxd -r -p {{input_file}} {{output_file}}`
