# aws ssm

> Ապահով փոխգործակցեք և կառավարեք AWS ռեսուրսները:.
> Նշում. ինտերակտիվ նիստերի համար պահանջվում է Session Manager հավելվածի տեղադրում:.
> Լրացուցիչ տեղեկություններ. <https://docs.aws.amazon.com/cli/latest/reference/ssm/>:.

- Գործարկել հրամանները օրինակների վրա.:

`aws ssm send-command --instance-ids {{instance_id1 instance_id2 ...}} --document-name "AWS-RunShellScript" --parameters 'commands=["{{command}}"]'`

- Ստուգեք հրամանի կանչերը մի օրինակի վրա.:

`aws ssm list-command-invocations --instance-id "{{instance_id}}"`

- Ստուգեք հրամանի ելքը հատուկ հրամանի կանչի համար.:

`aws ssm list-command-invocations --command-id "{{command_id}}" --details`

- Սկսեք ինտերակտիվ նստաշրջան մի օրինակով.:

`aws ssm start-session --target "{{instance_id}}"`

- Սկսեք նավահանգիստների վերահասցեավորում դեպի հեռավոր հոսթ.:

`aws ssm start-session --target "{{instance_id}}" --document-name "AWS-StartPortForwardingSessionToRemoteHost" --parameters '{"portNumber":["{{remote_port}}"],"localPortNumber":["{{local_port}}"]}'`
