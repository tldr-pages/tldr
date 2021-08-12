# rar

> Arhivatorul RAR. Suportă arhive multi-volum care pot fi opțional auto-extragere.

- Arhiva 1 sau mai multe fișiere:

`rar a {{path/to/archive_name.rar}} {{path/to/file1}} {{path/to/file2}} {{path/to/file3}}`

- Arhivează un director:

`rar a {{path/to/archive_name.rar}} {{path/to/directory}}`

- Împărțiți arhiva în părți de dimensiuni egale (50M):

`rar a -v{{50M}} -R {{path/to/archive_name.rar}} {{path/to/file_or_directory}}`

- Parola protejează arhiva rezultată:

`rar a -p{{password}} {{path/to/archive_name.rar}} {{path/to/file_or_directory}}`

- Criptați datele de fișier și anteturile cu parolă:

`rar a -hp{{password}} {{path/to/archive_name.rar}} {{path/to/file_or_directory}}`

- Utilizaţi un nivel specific de compresie (0-5):

`rar a -m{{compression_level}} {{path/to/archive_name.rar}} {{path/to/file_or_directory}}`
