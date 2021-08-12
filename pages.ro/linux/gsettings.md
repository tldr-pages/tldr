# gsettings

> Interogare și modificați setările dconf cu validarea schemei.
> Mai multe informaţii: <https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/8/html/using_the_desktop_environment_in_rhel_8/configuring-gnome-at-low-level_using-the-desktop-environment-in-rhel-8#using-gsettings-command_configuring-gnome-at-low-level>

- Setați valoarea unei chei. Nu reușește dacă cheia nu există sau valoarea este în afara intervalului:

`gsettings set {{org.example.schema}} {{example-key}} {{value}}`

- Tipăriți valoarea unei chei sau valoarea implicită furnizată de schemă dacă cheia nu a fost setată în `dconf`:

`gsetings get {{org.example.schema}} {{example-key}}`

- Anulați o cheie, astfel încât valoarea implicită a schemei va fi utilizată:

`gsettings reset {{org.example.schema}} {{example-key}}`

- Afișează toate schemele, cheile și valorile (nerelocabile):

`gsettings list-recursively`

- Afișează toate tastele și valorile (implicit dacă nu sunt setate) dintr-o schemă:

`gsettings list-recursively {{org.example.schema}}`

- Afișează valorile permise de schemă pentru o cheie (util cu tastele enum):

`gsettings range {{org.example.schema}} {{example-key}}`

- Afișează descrierea care poate fi citită de om a unei chei:

`gsettings describe {{org.example.schema}} {{example-key}}`
