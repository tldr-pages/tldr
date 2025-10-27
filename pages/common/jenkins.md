# jenkins cli 

> an open-source automation server that facilitates the automation of software development lifecycle.
> More information: <https://www.jenkins.io/doc/>.

- Connect to Jenkins CLI:

`java -jar jenkins-cli.jar -s http://{{jenkins-url}} -auth {{username}}:{{api_token}}`

- List Available Commands:

`java -jar jenkins-cli.jar -s http://{{jenkins-url}} help`

- Get Jenkins Version:

`java -jar jenkins-cli.jar -s http://{{jenkins-url}} version`

- Restart Jenkins:

`java -jar jenkins-cli.jar -s http://{{jenkins-url}} restart`

- Shutdown Jenkins:

`java -jar jenkins-cli.jar -s http://{{jenkins-url}} shutdown`
