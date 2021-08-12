# lftp

> Program sofisticat de transfer de fișiere.
> Mai multe informaţii: <https://lftp.yar.ru/lftp-man.html>

- Conectează-te la un server FTP:

`lftp {{ftp.example.com}}`

- Descărcați mai multe fișiere (expresie glob):

`mget {{path/to/*.png}}`

- Încărcați mai multe fișiere (expresie glob):

`mput {{path/to/*.zip}}`

- Ștergeți mai multe fișiere de pe serverul de la distanță:

`mrm {{path/to/*.txt}}`

- Redenumiți un fișier de pe serverul de la distanță:

`mv {{original_filename}} {{new_filename}}`

- Descărcați sau actualizați un întreg director:

`mirror {{path/to/remote_dir}} {{path/to/local_output_dir}}`

- Încărcați sau actualizați un întreg director:

`mirror -R {{path/to/local_dir}} {{path/to/remote_output_dir}}`
