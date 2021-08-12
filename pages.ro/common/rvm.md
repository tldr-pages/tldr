# rvm

> Un instrument pentru instalarea, gestionarea și lucrul cu mai multe medii rubinice.
> Mai multe informaţii: <https://rvm.io>

- Instalați una sau mai multe versiuni separate de spațiu de Ruby:

`rvm install {{version(s)}}`

- Afișează o listă de versiuni instalate:

`rvm list`

- Utilizați o versiune specifică a Ruby:

`rvm use {{version}}`

- Setați versiunea implicită Ruby:

`rvm --default use {{version}}`

- Upgrade o versiune de Ruby la o nouă versiune:

`rvm upgrade {{current_version}} {{new_version}}`

- Dezinstalați o versiune de Ruby și să păstreze sursele sale:

`rvm uninstall {{version}}`

- Eliminați o versiune a Ruby și a surselor sale:

`rvm remove {{version}}`

- Afișați dependențe specifice pentru sistemul dvs. de operare:

`rvm requirements`
