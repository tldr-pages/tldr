# ar

> Crea, modifica y extrae de archivos Unix. Típicamente utilizado para bibliotecas estáticas (`.a`) y paquetes Debian (`.deb`).
> Vea también: `tar`, `ranlib`.
> Más información: <https://manned.org/ar>.

- E[x]trae todos los miembros de un archivo:

`ar x {{ruta/al/archivo.a}}`

- Lis[t]a los contenidos de un archivo:

`ar t {{ruta/al/archivo.ar}}`

- [r]eemplaza o añade archivos a un archivo:

`ar r {{ruta/al/archivo.deb}} {{ruta/a/binario-debian ruta/a/control.tar.gz ruta/a/datos.tar.xz ...}}`

- In[s]erta un índice de archivo objeto (equivalente a usar `ranlib`):

`ar s {{ruta/al/archivo.a}}`

- Crea un archivo con archivos específicos incluyendo un índice de archivo objeto:

`ar rs {{ruta/al/archivo.a}} {{ruta/al/archivo1.o ruta/al/archivo2.o ...}}`
