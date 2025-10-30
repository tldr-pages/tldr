# jenkins node

> An open-source automation server that facilitates the automation of software development lifecycle.
> More information: <https://www.jenkins.io/doc/>.

- List all nodes:

`java -jar jenkins-cli.jar -s {{jenkins_server_url}} list-nodes`

- Create a node:

`java -jar jenkins-cli.jar -s {{jenkins_server_url}} create-node {{node_name}}`

- Delete a node:

`java -jar jenkins-cli.jar -s {{jenkins_server_url}} delete-node {{node_name}}`

- Enable a node:

`java -jar jenkins-cli.jar -s {{jenkins_server_url}} enable-node {{node_name}}`

- Disable a node:

`java -jar jenkins-cli.jar -s {{jenkins_server_url}} disable-node {{node_name}}`

- Connect to a node:

`java -jar jenkins-cli.jar -s {{jenkins_server_url}} connect-node {{node_name}}`
