# pacman --deptest

> Verificați fiecare dependență specificată și returnați o listă de dependențe care nu sunt îndeplinite în prezent în sistem.
> Mai multe informaţii: <https://man.archlinux.org/man/pacman.8>

- Imprimați numele pachetelor dependențelor care nu sunt instalate:

`pacman --deptest {{package_name1}} {{package_name2}}`

- Verificați dacă pachetul instalat satisface versiunea minimă dată:

`pacman --deptest "{{bash>=5}}"`

- Verificați dacă este instalată o versiune ulterioară a unui pachet:

`pacman --deptest "{{bash>5}}"`

- Ajutor pentru afișare:

`pacman --deptest --help`
