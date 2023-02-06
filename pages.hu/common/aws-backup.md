# aws backup

> Az Amazon Web Services szolgáltatásainak és a hozzájuk tartozó adatoknak a védelmére tervezett egységes biztonsági mentési szolgáltatás. További információ: <https://docs.aws.amazon.com/cli/latest/reference/backup/index.html>.

- Visszaadja a BackupPlan adatait egy adott BackupPlanId-hez:

`aws backup get-backup-plan --backup-plan-id {{id}}`

- Biztonsági mentési terv létrehozása egy adott mentési terv neve és a mentési szabályok felhasználásával:

`aws backup create-backup-plan --backup-plan {{plan}}`

- Egy adott biztonsági mentési terv törlése:

`aws backup delete-backup-plan --backup-plan-id {{id}}`

- Az aktuális fiók összes aktív biztonsági mentési tervének listájának visszaadása:

`aws backup list-backup-plans`

- A jelentési feladatok részleteinek megjelenítése:

`aws backup list-report-jobs`
