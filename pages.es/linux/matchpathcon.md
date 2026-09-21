# matchpathcon

> Consulta la configuración del contexto de seguridad persistente de SELinux para una ruta.
> Vea también: `semanage fcontext`, `secon`, `chcon`, `restorecon`.
> Más información: <https://manned.org/matchpathcon.8>.

- Consulta la configuración del contexto de seguridad persistente de una ruta absoluta:

`matchpathcon /{{ruta/al/archivo}}`

- Restringe la consulta a la configuración de un tipo de archivo específico:

`matchpathcon -m {{file|dir|pipe|chr_file|blk_file|lnk_file|sock_file}} /{{ruta/al/archivo}}`

- [V]erifica que los contextos de seguridad persistentes y actuales de una ruta coincidan:

`matchpathcon -V /{{ruta/al/archivo}}`
