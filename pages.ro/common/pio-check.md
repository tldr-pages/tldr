# pio check

> Efectuați o verificare de analiză statică pe un proiect PlatForMio.
> Mai multe informaţii: <https://docs.platformio.org/en/latest/core/userguide/cmd_check.html>

- Efectuați o analiză de bază a proiectului curent:

`pio check`

- Efectuați o analiză de bază a unui anumit proiect:

`pio check --project-dir {{project_dir}}`

- Efectuați o verificare de analiză pentru un anumit mediu:

`pio check --environment {{environment}}`

- Efectuați o verificare de analiză și raportați numai un anumit tip de severitate a defectelor:

`pio check --severity {{low|medium|high}}`

- Efectuați o verificare de analiză și afișați informații detaliate atunci când procesați medii:

`pio check --verbose`
