# mvn archetype

> 미리 정의된 템플릿(archetype)으로부터 새로운 Maven 프로젝트를 생성하는 도구.
> 더 많은 정보: <https://maven.apache.org/archetype/maven-archetype-plugin/usage.html>.

- 대화형으로 새로운 프로젝트 생성:

`mvn archetype:generate`

- 특정 archetype과 프로젝트 파라미터를 지정해 비대화식으로 프로젝트 생성:

`mvn archetype:generate --define archetypeGroupId={{그룹_아이디}} --define archetypeArtifactId={{아티팩트_아이디}} --define archetypeVersion={{버전}} --define groupId={{프로젝트_그룹_아이디}} --define artifactId={{프로젝트_이름}} --define interactiveMode=false`
