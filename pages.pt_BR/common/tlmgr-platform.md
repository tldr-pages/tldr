# tlmgr platform

> Gerencia plataformas de TeX Live.
> Mais informações: <https://www.tug.org/texlive/doc/tlmgr.html#platform>.

- Lista todas as plataformas disponíveis no repositório de pacotes:

`tlmgr {{[arch|platform]}} list`

- Adiciona os executáveis de uma plataforma específica:

`sudo tlmgr {{[arch|platform]}} add {{plataforma}}`

- Remove os executáveis de uma plataforma específica:

`sudo tlmgr {{[arch|platform]}} remove {{plataforma}}`

- Detecta automaticamente e troca para a plataforma atual:

`sudo tlmgr {{[arch|platform]}} set auto`

- Troca para uma plataforma específica:

`sudo tlmgr {{[arch|platform]}} set {{plataforma}}`
