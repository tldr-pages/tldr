# mvn deploy

> Add an artifact to a remote repository.
> More information: <https://manned.org/mvn>.

- Copy the final artifact into the remote repository configured in the `settings.xml` file:

`mvn deploy`

- Copy an artifact, that is not built using Maven to the remote repository:

`mvn deploy:deploy-file {{[-D|--define]}} url={{URLOfTheRemoteRepository}} {{[-D|--define]}} repositoryId={{ServerIdFromSettingsXML}} {{[-D|--define]}} file={{FileToBeDeployed}}`
