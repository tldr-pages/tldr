# phar

> Crearea, actualizarea sau extragerea arhivelor PHP (PHAR).

- Adăugați fișiere sau directoare separate de spațiu într-un fișier Phar:

`phar add -f {{path/to/phar_file}} {{files_or_directories}}`

- Afișează conținutul unui fișier Phar:

`phar list -f {{path/to/phar_file}}`

- Ștergeți fișierul sau directorul specificat dintr-un fișier Phar:

`phar delete -f {{path/to/phar_file}} -e {{file_or_directory}}`

- Afișează informații complete de utilizare și algoritmi de hashing/compresie disponibile:

`phar help`

- Comprimare sau decompresie fișiere și directoare într-un fișier Phar:

`phar compress -f {{path/to/phar_file}} -c {{algorithm}}`

- Obțineți informații despre un fișier Phar:

`phar info -f {{path/to/phar_file}}`

- Semnează un fișier Phar cu un algoritm hash specific:

`phar sign -f {{path/to/phar_file}} -h {{algorithm}}`

- Semnează un fișier Phar cu o cheie privată OpenSSL:

`phar sign -f {{path/to/phar_file}} -h openssl -y {{path/to/private_key}}`
