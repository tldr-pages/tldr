# kubetail

> Utilitate pentru a coada mai multe busteni Kubernetes pod în același timp.
> Mai multe informaţii: <https://github.com/johanhaleby/kubetail>

- Coada jurnalele de mai multe păstăi (al căror nume începe cu „my_app”) într-un du-te:

`kubetail {{my_app}}`

- Coada doar un container specific din mai multe păstăi:

`kubetail {{my_app}} -c {{my_container}}`

- Pentru a urmări mai multe containere din mai multe păstăi:

`kubetail {{my_app}} -c {{my_container_1}} -c {{my_container_2}}`

- Pentru a coada mai multe aplicații în același timp, separați-le prin virgulă:

`kubetail {{my_app_1}},{{my_app_2}}`
