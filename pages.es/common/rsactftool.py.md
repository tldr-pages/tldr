# RsaCtfTool.py

> Herramienta de ataque RSA para desafíos CTF - recupera claves privadas a partir de claves públicas débiles y/o descifra datos.
> Más información: <https://github.com/RsaCtfTool/RsaCtfTool>.

- Recupera una clave privada de un archivo de clave pública:

`RsaCtfTool.py --publickey {{ruta/a/clave.pub}} --private`

- Descifra un fichero utilizando una clave pública:

`RsaCtfTool.py --publickey {{ruta/a/clave.pub}} --decryptfile {{ruta/a/archivo_cifrado}}`

- Descifra una cadena de texto cifrado específica:

`RsaCtfTool.py --publickey {{ruta/a/clave.pub}} --decrypt "{{texto_cifrado}}"`

- Vuelca los componentes de una clave RSA (por ejemplo, módulo, exponente) desde un archivo de claves:

`RsaCtfTool.py --dumpkey --key {{ruta/a/clave.pub}}`

- Ejecuta un ataque específico (por ejemplo, factorización de Fermat) para recuperar la clave privada:

`RsaCtfTool.py --publickey {{ruta/a/clave.pub}} --private --attack fermat`

- Genera una clave pública a partir del módulo (n) y el exponente (e):

`RsaCtfTool.py --createpub -n {{módulo}} -e {{exponente}}`

- Intenta todos los ataques disponibles para recuperar la clave privada:

`RsaCtfTool.py --publickey {{ruta/a/clave.pub}} --private --attack all`
