# losetup

> Configurați și controlați dispozitivele cu buclă.

- Lista dispozitivelor de buclă cu informații detaliate:

`losetup -a`

- Atașați un fișier la un dispozitiv de buclă dat:

`sudo losetup /dev/{{loop}} /{{path/to/file}}`

- Atașați un fișier la un nou dispozitiv de buclă liberă și scanați dispozitivul pentru partiții:

`sudo losetup --show --partscan -f /{{path/to/file}}`

- Atașați un fișier la un dispozitiv buclă doar în citire:

`sudo losetup --read-only /dev/{{loop}} /{{path/to/file}}`

- Detaşaţi toate dispozitivele de buclă:

`sudo losetup -D`

- Detașați un dispozitiv de buclă dat:

`sudo losetup -d /dev/{{loop}}`
