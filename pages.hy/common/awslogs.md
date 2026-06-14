# awslogs

> Հարցման խմբեր, հոսքեր և իրադարձություններ Amazon CloudWatch-ի տեղեկամատյաններից:.
> Լրացուցիչ տեղեկություններ. <https://github.com/jorgebastida/awslogs#options>:.

- Ցուցակ մատյան խմբեր.:

`awslogs groups`

- Նշեք առկա հոսքերը նշված խմբի համար.:

`awslogs streams {{/var/log/syslog}}`

- Ստացեք տեղեկամատյաններ նշված խմբի ցանկացած հոսքերի համար 1-ից 2 ժամ առաջ.:

`awslogs get {{/var/log/syslog}} {{[-s|--start]}} '{{2h ago}}' {{[-e|--end]}} '{{1h ago}}'`

- Ստացեք տեղեկամատյաններ, որոնք համապատասխանում են CloudWatch Logs Filter-ի հատուկ օրինակին.:

`awslogs get {{/aws/lambda/my_lambda_group}} --filter-pattern '{{ERROR}}'`

- Դիտեք տեղեկամատյանները նշված խմբի ցանկացած հոսքերի համար.:

`awslogs get {{/var/log/syslog}} ALL --watch`
