# tlmgr platform

> Administra las plataformas TeX Live.
> Más información: <https://www.tug.org/texlive/doc/tlmgr.html#platform>.

- Lista todas las plataformas disponibles en el repositorio de paquetes:

`tlmgr {{[arch|platform]}} list`

- Añade los ejecutables para una plataforma específica:

`sudo tlmgr {{[arch|platform]}} add {{plataforma}}`

- Elimina los ejecutables para una plataforma específica:

`sudo tlmgr {{[arch|platform]}} remove {{plataforma}}`

- Auto detecta y cambia a la plataforma actual:

`sudo tlmgr {{[arch|platform]}} set auto`

- Cambia a una plataforma específica:

`sudo tlmgr {{[arch|platform]}} set {{plataforma}}`
