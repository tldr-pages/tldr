# aws ec2

> Կառավարեք AWS EC2 օրինակները և ծավալները:.
> AWS EC2-ն ապահովում է ապահով և չափափոխելի հաշվողական հզորություն AWS ամպում` հավելվածների ավելի արագ զարգացման և տեղակայման համար:.
> Լրացուցիչ տեղեկություններ. <https://docs.aws.amazon.com/cli/latest/reference/ec2/>:.

- Ցուցադրել տեղեկատվություն կոնկրետ օրինակի մասին.:

`aws ec2 describe-instances --instance-ids {{instance_id}}`

- Ցուցադրել տեղեկատվություն բոլոր դեպքերի մասին.:

`aws ec2 describe-instances`

- Ցուցադրել տեղեկատվություն բոլոր EC2 ծավալների մասին.:

`aws ec2 describe-volumes`

- Ջնջել EC2 ծավալը.:

`aws ec2 delete-volume --volume-id {{volume_id}}`

- Ստեղծեք նկար EC2 ծավալից.:

`aws ec2 create-snapshot --volume-id {{volume_id}}`

- Ցուցակ հասանելի AMI-ները (Amazon Machine Images).:

`aws ec2 describe-images`

- Ցուցադրել բոլոր հասանելի EC2 հրամանների ցանկը.:

`aws ec2 help`

- Ցուցադրել օգնություն հատուկ EC2 ենթահրամանի համար.:

`aws ec2 {{subcommand}} help`
