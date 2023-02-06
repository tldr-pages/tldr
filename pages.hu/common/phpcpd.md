# phpcpd

> Másolás és beillesztés detektor PHP kódhoz. További információ: <https://github.com/sebastianbergmann/phpcpd>.

- Egy adott fájl vagy könyvtár duplikált kódjának elemzése:

`phpcpd {{path/to/file_or_directory}}`

- Elemzés a változónevek fuzzy megfeleltetésével:

`phpcpd --fuzzy {{path/to/file_or_directory}}`

- Adja meg az azonos sorok minimális számát (alapértelmezett érték 5):

`phpcpd --min-lines {{number_of_lines}} {{path/to/file_or_directory}}`

- Az azonos tokenek minimális számának megadása (alapértelmezett érték 70):

`phpcpd --min-tokens {{number_of_tokens}} {{path/to/file_or_directory}}`

- Egy könyvtár kizárása az elemzésből (a forráshoz viszonyítva kell lennie):

`phpcpd --exclude {{path/to/excluded_directory}} {{path/to/file_or_directory}}`

- Az eredmények PHP-CPD XML-fájlba történő kimenete:

`phpcpd --log-pmd {{path/to/log_file}} {{path/to/file_or_directory}}`
