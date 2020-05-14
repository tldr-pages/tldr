# jhipster

> Generates a monolithic or microservices project after prompting user.
> More information: <https://www.jhipster.tech/>.

- Generate a simple full-stack project (monolithic or microservices):

`jhipster`

- Generate a simple frontend project (with OPTION = --skip-server) or a simple backend project (with OPTION = --skip-client):

`jhipster [OPTION]`

- Upgrade a generated project with the last JHipster updates:

`jhipster upgrade`

- Add a new entity to a generated project:

`jhipster entity {{entity_name}}`

- Import a JDL file to configure your application (entities...) - See: https://start.jhipster.tech/jdl-studio/:

`jhipster import-jdl {{first_file.jh}} {{second_file.jh}}... {{n_file.jh}}`

- Generate a CI/CD pipeline for your application:

`jhipster ci-cd`

- Generate a docker-compose.yml file for your application(s):

`jhipster docker-compose`

- Generate a Kubernetes configuration for your applications:

`jhipster kubernetes`
