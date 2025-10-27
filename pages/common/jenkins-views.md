# jenkins view

> An open-source automation server that facilitates the automation of software development lifecycle.
> More information: <https://www.jenkins.io/doc/>.

- List all views:

`java -jar jenkins-cli.jar -s http://{{jenkins-url}} list-views`

- Create a view:

`java -jar jenkins-cli.jar -s http://{{jenkins-url}} create-view {{view_name}}`

- Delele a view:

`java -jar jenkins-cli.jar -s http://{{jenkins-url}} delete-view {{view_name}}`

- Update a view:

`java -jar jenkins-cli.jar -s http://{{jenkins-url}} update-view {{view_name}} < {{path_to_file}}`

- Add job to view:

`java -jar jenkins-cli.jar -s http://{{jenkins-url}} add-job-to-view {{view_name}} {{job_name}}`

- Remove job from a view:

`java -jar jenkins-cli.jar -s http://{{jenkins-url}} remove-job-from-view {{view_name}} {{job_name}}`
