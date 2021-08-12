# ngrep

> Filtrați pachetele de trafic în rețea utilizând expresii regulate.
> Mai multe informaţii: <https://github.com/jpr5/ngrep>

- Capturarea traficului tuturor interfețelor:

`ngrep -d any`

- Capturarea traficului unei interfețe specifice:

`ngrep -d {{eth0}}`

- Capturează portul de trecere a traficului 22 de interfață eth0:

`ngrep -d {{eth0}} port {{22}}`

- Capturarea traficului de la sau la o gazdă:

`ngrep host {{www.example.com}}`

- Filtrează cuvântul cheie 'User-Agent: 'de interfață eth0:

`ngrep -d {{eth0}} '{{User-Agent:}}'`
