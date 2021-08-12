# aws-vault

> Un seif pentru stocarea și accesarea securizată a acreditărilor AWS în medii de dezvoltare.
> Mai multe informaţii: <https://github.com/99designs/aws-vault>

- Adăugați acreditări la keystore securizat:

`aws-vault add {{profile}}`

- Executați o comandă cu acreditările AWS în mediu:

`aws-vault exec {{profile}} -- {{aws s3 ls}}`

- Deschideți o fereastră de browser și conectați-vă la consola AWS:

`aws-vault login {{profile}}`

- Lista profilurilor, împreună cu acreditările și sesiunile lor:

`aws-vault list`

- Rotiți acreditările AWS:

`aws-vault rotate {{profile}}`

- Eliminați acreditările din magazinul de chei securizate:

`aws-vault remove {{profile}}`
