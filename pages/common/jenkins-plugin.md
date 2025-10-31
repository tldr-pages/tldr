# jenkins plugin

> An open-source automation server that facilitates the automation of software development lifecycle.
> More information: <https://www.jenkins.io/doc/>.

- List all plugins:

`java -jar jenkins-cli.jar -s {{jenkins_server_url}} list-plugins`

- Install a plugin:

`java -jar jenkins-cli.jar -s {{jenkins_server_url}} install-plugin {{plugin_name}}`

- Update a plugin:

`java -jar jenkins-cli.jar -s {{jenkins_server_url}} install-plugin {{plugin_name}} --deploy`

- Update all plugin:

`java -jar jenkins-cli.jar -s {{jenkins_server_url}} install-plugin all`

- Uninstall a plugin:

`java -jar jenkins-cli.jar -s {{jenkins_server_url}} uninstall-plugin {{plugin_name}}`
