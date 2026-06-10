# aws խմբաքանակ

> Գործարկեք խմբաքանակի հաշվարկման ծանրաբեռնվածությունը AWS Batch ծառայության միջոցով:.
> Լրացուցիչ տեղեկություններ. <https://docs.aws.amazon.com/cli/latest/reference/batch/>:.

- Ցուցակեք գործող խմբաքանակի աշխատանքները.:

`aws batch list-jobs --job-queue {{queue_name}}`

- Ստեղծեք հաշվողական միջավայր.:

`aws batch create-compute-environment --compute-environment-name {{compute_environment_name}} --type {{type}}`

- Ստեղծեք խմբաքանակի աշխատանքի հերթ.:

`aws batch create-job-queue --job-queue-name {{queue_name}} --priority {{priority}} --compute-environment-order {{compute_environment}}`

- Ներկայացրեք աշխատանք.:

`aws batch submit-job --job-name {{job_name}} --job-queue {{job_queue}} --job-definition {{job_definition}}`

- Նկարագրեք խմբաքանակի աշխատանքների ցանկը.:

`aws batch describe-jobs --jobs {{jobs}}`

- Չեղարկել աշխատանքը.:

`aws batch cancel-job --job-id {{job_id}} --reason {{reason}}`
