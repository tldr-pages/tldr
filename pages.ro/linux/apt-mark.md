# apt-mark

> Utilitar pentru a schimba starea pachetelor instalate.
> Mai multe informaţii: <https://manpages.debian.org/latest/apt/apt-mark.8.html>

- Marcați un pachet ca instalat automat:

`sudo apt-mark auto {{package_name}}`

- Țineți un pachet la versiunea sa curentă și împiedicați actualizările acestuia:

`sudo apt-mark hold {{package_name}}`

- Permiteți unui pachet să fie actualizat din nou:

`sudo apt-mark unhold {{package_name}}`

- Arată pachetele instalate manual:

`apt-mark showmanual`

- Afișează pachetele deținute care nu sunt actualizate:

`apt-mark showhold`
