# pm2

> Folyamatkezelő a Node.js számára. Naplókezelésre, folyamatok felügyeletére és konfigurálására szolgál. További információ: <https://pm2.keymetrics.io>.

- Indítson el egy folyamatot egy olyan névvel, amelyet későbbi műveletekhez használhat:

`pm2 start {{app.js}} --name {{application_name}}`

- Folyamatok listázása:

`pm2 list`

- Az összes folyamat figyelése:

`pm2 monit`

- Egy folyamat leállítása:

`pm2 stop {{application_name}}`

- Egy folyamat újraindítása:

`pm2 restart {{application_name}}`

- Az összes folyamat kiürítése a későbbi újraélesztésükhöz:

`pm2 save`

- Korábban kiürített folyamatok újraélesztése:

`pm2 resurrect`
