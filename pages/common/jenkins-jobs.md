# jenkins job

> An open-source automation server that facilitates the automation of software development lifecycle.
> More information: <https://www.jenkins.io/doc/>.

- Create a new job:

`java -jar jenkins-cli.jar -s http://{{jenkins-url}} create-job {{job_name}} < {{path_to_file}}`

- Build a job:

`java -jar jenkins-cli.jar -s http://{{jenkins-url}} build {{job_name}}`

- Delete a job:

`java -jar jenkins-cli.jar -s http://{{jenkins-url}} delete-job {{job_name}}`

- Get job configurations:

`java -jar jenkins-cli.jar -s http://{{jenkins-url}} get-job {{job_name}} > {{path_to_file}}`
