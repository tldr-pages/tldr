# aws configure

> Az AWS CLI konfigurációjának kezelése. További információ: <https://docs.aws.amazon.com/cli/latest/reference/configure/>.

- Az AWS CLI interaktív konfigurálása (új konfiguráció létrehozása vagy az alapértelmezett frissítése):

`aws configure`

- Nevezett profil konfigurálása az AWS CLI számára interaktívan (új profil létrehozása vagy egy meglévő profil frissítése):

`aws configure --profile {{profile_name}}`

- Egy adott konfigurációs változó értékének megjelenítése:

`aws configure get {{name}}`

- Egy adott profilban lévő konfigurációs változó értékének megjelenítése:

`aws configure get {{name}} --profile {{profile_name}}`

- Egy adott konfigurációs változó értékének beállítása:

`aws configure set {{name}} {{value}}`

- Egy adott profilban lévő konfigurációs változó értékének beállítása:

`aws configure set {{name}} {{value}} --profile {{profile_name}}`

- A konfigurációs bejegyzések listázása:

`aws configure list`

- Egy adott profil konfigurációs bejegyzéseinek listázása:

`aws configure list --profile {{profile_name}}`
