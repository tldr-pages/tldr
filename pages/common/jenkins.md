# jenkins cli

> An open-source automation server that facilitates the automation of software development lifecycle.
> More information: <https://www.jenkins.io/doc/>.

- Connect to jenkins CLI:

`java -jar jenkins-cli.jar -s http://{{jenkins-url}} -auth {{username}}:{{api_token}}`

- List Available Commands:

`java -jar jenkins-cli.jar -s http://{{jenkins-url}} help`

- Get Version:

`java -jar jenkins-cli.jar -s http://{{jenkins-url}} version`

- Restart jenkins:

`java -jar jenkins-cli.jar -s http://{{jenkins-url}} restart`

- Shutdown jenkins:

`java -jar jenkins-cli.jar -s http://{{jenkins-url}} shutdown`
