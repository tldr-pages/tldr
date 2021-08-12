# if

> Shell simplă condiționată.
> A se vedea, de asemenea,: „test”, „[`.

- Executați două comenzi diferite bazate pe o condiție:

`if {{command}}; then {{echo "true"}}; else {{echo "false"}}; fi`

- Verificați dacă o variabilă este definită:

`if [[ -n "{{$VARIABLE}}" ]]; then {{echo "defined"}}; else {{echo "not defined"}}; fi`

- Verificați dacă există un fișier:

`if [[ -f "{{path/to/file}}" ]]; then {{echo "true"}}; else {{echo "false"}}; fi`

- Verificați dacă există un director:

`if [[ -d "{{path/to/directory}}" ]]; then {{echo "true"}}; else {{echo "false"}}; fi`

- Verificați dacă există un fișier sau un director:

`if [[ -e "{{path/to/file_or_directory}}" ]]; then {{echo "true"}}; else {{echo "false"}}; fi`

- Lista tuturor condițiilor posibile („test „este un alias pentru „['; ambele sunt utilizate în mod obișnuit cu „dacă”):

`man [`
