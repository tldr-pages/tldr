# jenkins plugin

> An open-source automation server that facilitates the automation of software development lifecycle.
> More information: <https://www.jenkins.io/doc/>.

- List all plugins:

`java -jar jenkins-cli.jar -s http://{{jenkins-url}} list-plugins`

- Install a plugin:

`java -jar jenkins-cli.jar -s http://{{jenkins-url}} install-plugin {{plugin_name}}`

- Update a plugin:

`java -jar jenkins-cli.jar -s http://{{jenkins-url}} install-plugin {{plugin_name}} --deploy`

- Update all plugin:

`java -jar jenkins-cli.jar -s http://{{jenkins-url}} install-plugin all`

- Uninstall a plugin:

`java -jar jenkins-cli.jar -s http://{{jenkins-url}} uninstall-plugin {{plugin_name}}`
