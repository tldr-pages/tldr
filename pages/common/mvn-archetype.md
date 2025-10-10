# mvn archetype

> Generate a new Maven project from a predefined template (archetype).  
> More information: <https://maven.apache.org/archetype/maven-archetype-plugin/usage.html>.

- Generate a new project interactively:

`mvn archetype:generate`

- Generate a project using specific archetype and parameters:

`mvn archetype:generate -DarchetypeGroupId={{group_id}} -DarchetypeArtifactId={{artifact_id}} -DarchetypeVersion={{version}} -DgroupId={{project_group_id}} -DartifactId={{project_name}} -DinteractiveMode=false`
