# axel

> Descărcare accelerator.
> Suportă HTTP, HTTPS și FTP.
> Mai multe informaţii: <https://github.com/axel-download-accelerator/axel>

- Descărcați un URL într-un fișier:

`axel {{url}}`

- Descărcați și specificați numele fișierului:

`axel {{url}} -o {{filename}}`

- Descărcați cu mai multe conexiuni:

`axel -n {{connections_num}} {{url}}`

- Caută oglinzi:

`axel -S {{mirrors_num}} {{url}}`

- Limitați viteza de descărcare (octeți pe secundă):

`axel -s {{speed}} {{url}}`
