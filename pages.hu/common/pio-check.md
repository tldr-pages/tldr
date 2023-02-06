# pio check

> Statikus elemzés elvégzése egy PlatformIO-projekten. További információ: <https://docs.platformio.org/en/latest/core/userguide/cmd_check.html>.

- Alapelemzési ellenőrzés elvégzése az aktuális projekten:

`pio check`

- Alapelemzési ellenőrzés végrehajtása egy adott projekten:

`pio check --project-dir {{project_dir}}`

- Egy adott környezet elemzési ellenőrzésének elvégzése:

`pio check --environment {{environment}}`

- Elemzési ellenőrzés végrehajtása és csak egy megadott hibasúlyossági típus jelentése:

`pio check --severity {{low|medium|high}}`

- Elemzési ellenőrzés végrehajtása és részletes információk megjelenítése a környezetek feldolgozásakor:

`pio check --verbose`
