# phpspec

> Un instrument de dezvoltare bazată pe comportament pentru PHP.
> Mai multe informaţii: <https://phpspec.net>

- Creați o specificație pentru o clasă:

`phpspec describe {{class_name}}`

- Rulați toate specificațiile din directorul „spec”:

`phpspec run`

- Rulați o singură specificație:

`phpspec run {{path/to/class_specification_file}}`

- Rulați specificații utilizând un fișier de configurare specific:

`phpspec run -c {{path/to/configuration_file}}`

- Executați specificații folosind un fișier bootstrap specific:

`phpspec run -b {{path/to/bootstrap_file}}`

- Dezactivați generarea de coduri:

`phpspec run --no-code-generation`

- Activați valorile returnate false:

`phpspec run --fake`
