#cython

> Կոմպիլյատոր, որը փոխակերպում է `.pyx` ֆայլերը C կամ C++ սկզբնաղբյուր ֆայլերի:.
> Լրացուցիչ տեղեկություններ. <https://docs.cython.org/en/latest/>:.

- Կազմել C կոդի մեջ.:

`cython {{path/to/file}}`

- Կազմել C++ կոդի մեջ.:

`cython --cplus {{path/to/file}}`

- Նշեք ելքային ֆայլ.:

`cython {{[-o|--output-file]}} {{path/to/output_file}} {{path/to/file}}`

- Ցուցադրման տարբերակը:

`cython {{[-V|--version]}}`
