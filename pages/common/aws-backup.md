# aws backup

> Unified backup service designed to protect Amazon Web Services services and their associated data.
> More information: <https://docs.aws.amazon.com/cli/latest/reference/backup/index.html>.

- Return BackupPlan details for a specific BackupPlanId:

`aws backup get-backup-plan --backup-plan-id {{id}}`

- Create a backup plan using a specific backup plan name and backup rules:

`aws backup create-backup-plan --backup-plan {{plan}}`

- Delete a specific backup plan:

`aws backup delete-backup-plan --backup-plan-id {{id}}`

- List all active backup plans for the current account:

`aws backup list-backup-plans`

- Display details about your report jobs:

`aws backup list-report-jobs`
