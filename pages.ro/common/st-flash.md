# st-flash

> Fișiere binare Flash pentru microcontrolere ARM STM32 Cortex.
> Mai multe informaţii: <https://github.com/texane/stlink>

- Citiți 4096 octeți de pe dispozitiv începând de la 0x8000000:

`st-flash read {{firmware}}.bin {{0x8000000}} {{4096}}`

- Scrieți firmware-ul pe dispozitiv începând de la 0x8000000:

`st-flash write {{firmware}}.bin {{0x8000000}}`

- Ștergeți firmware-ul de pe dispozitiv:

`st-flash erase`
