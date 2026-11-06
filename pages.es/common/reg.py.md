# reg.py

> Consulta, añade, elimina, guarda o realiza copias de seguridad de claves y valores del registro en un equipo Windows remoto a través de SMB/RPC.
> Forma parte del paquete Impacket.
> Más información: <https://github.com/fortra/impacket>.

- Consulta subclaves y valores en una ruta del registro:

`reg.py {{dominio}}/{{usuario}}:{{contraseña}}@{{destino}} query -keyName '{{HKLM\SOFTWARE\Microsoft\Windows}}'`

- Consulta todas las subclaves y valores de una ruta del registro de forma recursiva:

`reg.py {{dominio}}/{{usuario}}:{{contraseña}}@{{destino}} query -keyName '{{HKLM\SOFTWARE\Microsoft\Windows}}' -s`

- Añade una nueva clave o un nuevo valor del Registro (el tipo de valor predeterminado es `REG_SZ`):

`reg.py {{dominio}}/{{usuario}}:{{contraseña}}@{{destino}} add -keyName '{{HKLM\SOFTWARE\Microsoft\Windows}}' -v {{nombre_valor}} -vt {{REG_SZ|REG_NONE|REG_EXPAND_SZ|REG_BINARY|REG_DWORD|REG_DWORD_BIG_ENDIAN|REG_LINK|REG_MULTI_SZ|REG_QWORD}} -vd {{datos_valor}}`

- Eliminar una clave o un valor del Registro:

`reg.py {{dominio}}/{{usuario}}:{{contraseña}}@{{destino}} delete -keyName '{{HKLM\SOFTWARE\Example}}' -v {{nombre_valor}}`

- Guardar una clave del Registro (y sus subclaves) en un archivo del destino mediante una ruta UNC:

`reg.py {{dominio}}/{{usuario}}:{{contraseña}}@{{destino}} save -keyName '{{HKLM\SOFTWARE\Example}}' -o '\\{{destino}}\{{recurso compartido}}\{{archivo_de_salida.reg}}'`

- Realiza una copia de seguridad de los subárboles SAM, SYSTEM y SECURITY en un archivo del sistema de destino mediante una ruta UNC (requiere privilegios de SYSTEM):

`reg.py {{dominio}}/{{usuario}}:{{contraseña}}@{{destino}} backup -o '\\{{destino}}\{{compartir}}'`
