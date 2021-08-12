# nginx

> server web Nginx.
> Mai multe informaţii: <https://nginx.org/en/>

- Porniți serverul cu fișierul de configurare implicit:

`nginx`

- Porniți serverul cu un fișier de configurare personalizat:

`nginx -c {{config_file}}`

- Porniți serverul cu un prefix pentru toate căile relative din fișierul de configurare:

`nginx -c {{config_file}} -p {{prefix/for/relative/paths}}`

- Testați configurația fără a afecta serverul de funcționare:

`nginx -t`

- Reîncărcați configurația prin trimiterea unui semnal fără întreruperi:

`nginx -s reload`
