# aws կրկնօրինակում

> Միասնական պահեստային ծառայություն, որը նախատեսված է պաշտպանելու Amazon Web Services ծառայությունները և դրանց հետ կապված տվյալները:.
> Լրացուցիչ տեղեկություններ. <https://docs.aws.amazon.com/cli/latest/reference/backup/>:.

- Վերադարձեք BackupPlan-ի մանրամասները կոնկրետ BackupPlanId-ի համար.:

`aws backup get-backup-plan --backup-plan-id {{id}}`

- Ստեղծեք պահեստային պլան՝ օգտագործելով հատուկ պահեստային պլանի անվանումը և պահուստավորման կանոնները.:

`aws backup create-backup-plan --backup-plan {{plan}}`

- Ջնջել հատուկ պահուստային պլան.:

`aws backup delete-backup-plan --backup-plan-id {{id}}`

- Թվարկեք բոլոր ակտիվ պահուստային պլանները ընթացիկ հաշվի համար.:

`aws backup list-backup-plans`

- Ցուցադրել մանրամասներ ձեր զեկույցի աշխատանքների մասին.:

`aws backup list-report-jobs`
