# particle

> Un instrument de linie de comandă pentru interacțiunea cu dispozitivele cu particule.
> Mai multe informaţii: <https://docs.particle.io/tutorials/developer-tools/cli>

- Conectați-vă sau creați un cont pentru particula CLI:

`particle setup`

- Afișează o listă de dispozitive:

`particle list`

- Creați un nou proiect de particule interactiv:

`particle project create`

- Compilarea unui proiect de particule:

`particle compile {{device_type}} {{path/to/source_code.ino}}`

- Actualizați un dispozitiv pentru a utiliza o anumită aplicație de la distanță:

`particle flash {{device_name}} {{path/to/program.bin}}`

- Actualizați un dispozitiv pentru a utiliza cel mai recent firmware prin serie:

`particle flash --serial {{path/to/firmware.bin}}`

- Execută o funcție pe un dispozitiv:

`particle call {{device_name}} {{function_name}} {{function_arguments}}`
