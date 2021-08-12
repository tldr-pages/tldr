# ftp

> Instrumente pentru a interacționa cu un server prin intermediul Protocolului de transfer de fișiere.

- Conectează-te la un server FTP:

`ftp {{ftp.example.com}}`

- Comutați la modul de transfer binar (grafică, fișiere comprimate, etc):

`binary`

- Transferați mai multe fișiere fără a solicita confirmarea pe fiecare fișier:

`prompt off`

- Descărcați mai multe fișiere (expresie glob):

`mget {{*.png}}`

- Încărcați mai multe fișiere (expresie glob):

`mput {{*.zip}}`

- Ștergeți mai multe fișiere de pe serverul de la distanță:

`mdelete {{*.txt}}`

- Redenumiți un fișier de pe serverul de la distanță:

`rename {{original_filename}} {{new_filename}}`
