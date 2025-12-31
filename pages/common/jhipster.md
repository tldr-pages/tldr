# jhipster

> Web application generator using either monolithic or microservices architecture.
> More information: <https://www.jhipster.tech/creating-an-app/#command-line-options>.

- Generate a simple full-stack project (monolithic or microservices):

`jhipster`

- Generate a simple frontend project:

`jhipster --skip-server`

- Generate a simple backend project:

`jhipster --skip-client`

- Apply latest JHipster updates to the project:

`jhipster upgrade`

- Add a new entity to a generated project:

`jhipster entity {{entity_name}}`

- Import a JDL file to configure your application (see: <https://start.jhipster.tech/jdl-studio/>):

`jhipster import-jdl {{file1.jh file2.jh ...}}`

- Generate a CI/CD pipeline for your application:

`jhipster ci-cd`

- Generate a Kubernetes configuration for your application:

`jhipster kubernetes`
