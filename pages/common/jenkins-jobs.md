# jenkins job

> An open-source automation server that facilitates the automation of software development lifecycle.
> More information: <https://www.jenkins.io/doc/>.

- List all jobs:

`java -jar jenkins-cli.jar -s {{jenkins_server_url}} list-jobs`

- Create a new job:

`java -jar jenkins-cli.jar -s {{jenkins_server_url}} create-job {{job_name}} < {{path_to_file}}`

- Build a job:

`java -jar jenkins-cli.jar -s {{jenkins_server_url}} build {{job_name}}`

- Delete a job:

`java -jar jenkins-cli.jar -s {{jenkins_server_url}} delete-job {{job_name}}`

- Get job configurations:

`java -jar jenkins-cli.jar -s {{jenkins_server_url}} get-job {{job_name}} > {{path_to_file}}`

- Copy job:

`java -jar jenkins-cli.jar -s {{jenkins_server_url}} copy-job {{source_job}} {{distination_job}}`

- Rename a job:

`java -jar jenkins-cli.jar -s {{jenkins_server_url}} rename-job {{old_job_name}} {{new_job_name}}`
