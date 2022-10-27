# aws backup

> Unified backup service designed to protect Amazon Web Services services and their associated data.
> More information: <https://docs.aws.amazon.com/cli/latest/reference/backup/index.html>.

- Returns BackupPlan details for the specified BackupPlanId:

`aws backup get-backup-plan --backup-plan-id {{id}}`

- Creates a backup plan using a backup plan name and backup rules:

`aws backup create-backup-plan --backup-plan {{plan}}`

- Deletes a backup plan:

`aws backup delete-backup-plan --backup-plan-id {{id}}`

- Returns a list of all active backup plans for an authenticated account:

`aws backup list-backup-plans`

- Returns details about your report jobs:

`aws backup list-report-jobs`


