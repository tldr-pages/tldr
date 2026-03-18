# aws ssm

> Securely interact with and manage AWS resources. Interactive sessions require the Session Manager plugin installed.
> More information: <https://docs.aws.amazon.com/cli/latest/reference/ssm/>.

- Run commands on instances:

`aws ssm send-command --instance-ids "{{instance_id}}" "{{second_instance_id}}" --document-name "AWS-RunShellScript" --parameters 'commands=["{{command}}"]'`

- Check command invocations on an instance:

`aws ssm list-command-invocations --instance-id "{{instance_id}}"`

- Check command output:

`aws ssm list-command-invocations --command-id "{{command_id}}" --details`

- Start a session with an instance:

`aws ssm start-session --target "{{instance_id}}"`

- Port forward to a remote host:

`aws ssm start-session --target "{{instance_id}}" --document-name "AWS-StartPortForwardingSessionToRemoteHost" --parameters '{"portNumber":["{{remote_port}}"],"localPortNumber":["{{local_port}}"]}'`
