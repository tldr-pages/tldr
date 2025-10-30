# jenkins view

> An open-source automation server that facilitates the automation of software development lifecycle.
> More information: <https://www.jenkins.io/doc/>.

- List all views:

`java -jar jenkins-cli.jar -s {{jenkins_server_url}} list-views`

- Create a view:

`java -jar jenkins-cli.jar -s {{jenkins_server_url}} create-view {{view_name}}`

- Delete a view:

`java -jar jenkins-cli.jar -s {{jenkins_server_url}} delete-view {{view_name}}`

- Update a view:

`java -jar jenkins-cli.jar -s {{jenkins_server_url}} update-view {{view_name}} < {{path_to_file}}`

- Add job to view:

`java -jar jenkins-cli.jar -s {{jenkins_server_url}} add-job-to-view {{view_name}} {{job_name}}`

- Remove job from a view:

`java -jar jenkins-cli.jar -s {{jenkins_server_url}} remove-job-from-view {{view_name}} {{job_name}}`
