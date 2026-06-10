# aws ամպ9

> Կառավարեք Cloud9 - գործիքների հավաքածու՝ ամպում ծրագրակազմը կոդավորելու, ստեղծելու, գործարկելու, փորձարկելու, կարգաբերելու և թողարկելու համար:.
> Լրացուցիչ տեղեկություններ. <https://docs.aws.amazon.com/cli/latest/reference/cloud9/>:.

- Թվարկեք Cloud9-ի զարգացման միջավայրի բոլոր նույնացուցիչները.:

`aws cloud9 list-environments`

- Ստեղծեք Cloud9-ի զարգացման միջավայր.:

`aws cloud9 create-environment-ec2 --name {{name}} --instance-type {{instance_type}}`

- Ցուցադրել տեղեկատվություն Cloud9-ի մշակման միջավայրերի մասին.:

`aws cloud9 describe-environments --environment-ids {{environment_ids}}`

- Ավելացրեք միջավայրի անդամ Cloud9-ի զարգացման միջավայրում.:

`aws cloud9 create-environment-membership --environment-id {{environment_id}} --user-arn {{user_arn}} --permissions {{permissions}}`

- Ցուցադրել կարգավիճակի մասին տեղեկատվություն Cloud9-ի զարգացման միջավայրի համար.:

`aws cloud9 describe-environment-status --environment-id {{environment_id}}`

- Ջնջել Cloud9 միջավայրը.:

`aws cloud9 delete-environment --environment-id {{environment_id}}`

- Ջնջել շրջակա միջավայրի անդամը զարգացման միջավայրից.:

`aws cloud9 delete-environment-membership --environment-id {{environment_id}} --user-arn {{user_arn}}`
