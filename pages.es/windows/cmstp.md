# cmstp

> Administra perfiles de servicio de conexión.
> Más información: <https://learn.microsoft.com/windows-server/administration/windows-commands/cmstp>.

- Instala un perfil específico:

`cmstp "{{ruta\al\archivo_de_perfil}}"`

- Instala sin crear un acceso directo en el escritorio:

`cmstp /ns "{{ruta\al\archivo_de_perfil}}"`

- Instala sin verificar dependencias:

`cmstp /nf "{{ruta\al\archivo_de_perfil}}"`

- Instala solo para el usuario actual:

`cmstp /su "{{ruta\al\archivo_de_perfil}}"`

- Instala para todos los usuarios (requiere privilegios de administrador):

`cmstp /au "{{ruta\al\archivo_de_perfil}}"`

- Instala silenciosamente sin ningún aviso:

`cmstp /s "{{ruta\al\archivo_de_perfil}}"`

- Desinstala un perfil específico:

`cmstp /u "{{ruta\al\archivo_de_perfil}}"`

- Desinstala silenciosamente sin un aviso de confirmación:

`cmstp /u /s "{{ruta\al\archivo_de_perfil}}"`
