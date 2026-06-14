# aws արագատեսություն

> Ստեղծեք, ջնջեք, ցուցակագրեք, որոնեք և թարմացրեք AWS QuickSight սուբյեկտները:.
> Լրացուցիչ տեղեկություններ. <https://docs.aws.amazon.com/cli/latest/reference/quicksight/>:.

- Ցուցակ տվյալների հավաքածուներ.:

`aws quicksight list-data-sets --aws-account-id {{aws_account_id}}`

- Ցանկ օգտագործողներին.:

`aws quicksight list-users --aws-account-id {{aws_account_id}} --namespace default`

- Ցանկ խմբեր.:

`aws quicksight list-groups --aws-account-id {{aws_account_id}} --namespace default`

- Ցուցակ վահանակներ.:

`aws quicksight list-dashboards --aws-account-id {{aws_account_id}}`

- Ցուցադրել տվյալների բազայի մասին մանրամասն տեղեկատվություն.:

`aws quicksight describe-data-set --aws-account-id {{aws_account_id}} --data-set-id {{data_set_id}}`

- Ցուցադրել, թե ով ունի տվյալների բազայի հասանելիություն և ինչպիսի գործողություններ կարող են կատարել տվյալ տվյալների վրա.:

`aws quicksight describe-data-set-permissions --aws-account-id {{aws_account_id}} --data-set-id {{data_set_id}}`
