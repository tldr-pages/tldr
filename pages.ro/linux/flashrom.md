# flashrom

> Citiți, scrieți, verificați și ștergeți chips-uri flash.
> Mai multe informaţii: <https://manned.org/flashrom>

- Sonde cip, asigurându-vă că cablajul este corect:

`flashrom --programmer {{programmer}}`

- Citiți blițul și salvați-l într-un fișier:

`flashrom -p {{programmer}} --read {{path/to/file}}`

- Scrieți un fișier în bliț:

`flashrom -p {{programmer}} --write {{path/to/file}}`

- Verificați blițul împotriva unui fișier:

`flashrom -p {{programmer}} --verify {{path/to/file}}`

- Sonda cip folosind RaspberryPi:

`flashrom -p {{linux_spi:dev=/dev/spidev0.0}}`
