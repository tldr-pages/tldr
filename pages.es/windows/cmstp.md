# cmstp

> Administra perfiles de servicio de conexión.
> Más información: <https://learn.microsoft.com/windows-server/administration/windows-commands/cmstp>.

- Instalar un perfil específico:

`cmstp "{{ruta\al\archivo_de_perfil}}"`

- Instalar sin crear un acceso directo en el escritorio:

`cmstp /ns "{{ruta\al\archivo_de_perfil}}"`

- Instalar sin verificar dependencias:

`cmstp /nf "{{ruta\al\archivo_de_perfil}}"`

- Instalar solo para el usuario actual:

`cmstp /su "{{ruta\al\archivo_de_perfil}}"`

- Instalar para todos los usuarios (requiere privilegios de administrador):

`cmstp /au "{{ruta\al\archivo_de_perfil}}"`

- Instalar silenciosamente sin ningún aviso:

`cmstp /s "{{ruta\al\archivo_de_perfil}}"`

- Desinstalar un perfil específico:

`cmstp /u "{{ruta\al\archivo_de_perfil}}"`

- Desinstalar silenciosamente sin un aviso de confirmación:

`cmstp /u /s "{{ruta\al\archivo_de_perfil}}"`
