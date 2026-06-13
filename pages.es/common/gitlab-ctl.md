# gitlab-ctl

> Gestiona el ómnibus de GitLab.
> Más información: <https://docs.gitlab.com/omnibus/maintenance/>.

- Muestra el estado de cada servicio:

`sudo gitlab-ctl status`

- Muestra el estado de un servicio específico:

`sudo gitlab-ctl status {{nginx}}`

- Reinicia todos los servicios:

`sudo gitlab-ctl restart`

- Reinicia un servicio específico:

`sudo gitlab-ctl restart {{nginx}}`

- Muestra los registros de cada servicio y sigue leyendo hasta que se pulse `<Ctrl c>`:

`sudo gitlab-ctl tail`

- Muestra los registros de un servicio específico:

`sudo gitlab-ctl tail {{nginx}}`

- Envia la señal SIGKILL a un servicio específico:

`sudo gitlab-ctl kill {{nginx}}`

- Reconfigura la aplicación:

`sudo gitlab-ctl reconfigure`
