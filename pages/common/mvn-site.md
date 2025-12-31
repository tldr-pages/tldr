# mvn site

> Generate a project website based on the information in the `pom.xml` file.
> More information: <https://maven.apache.org/plugins/maven-site-plugin/usage.html>.

- Generate a project site using the site plugin:

`mvn site`

- Generate a site for a specific Maven project (multi-module build):

`mvn site {{[-pl|--projects]}} {{module_name}}`

- Clean previous site output before generating a new one:

`mvn clean site`

- Skip tests while generating the site:

`mvn site {{[-D|--define]}} skipTests`

- Generate and deploy the site to the remote server:

`mvn site-deploy`
