# mvn արխետիպ

> Ստեղծեք նոր Maven նախագիծ նախապես սահմանված ձևանմուշից (արխետիպ):.
> Լրացուցիչ տեղեկություններ. <https://maven.apache.org/archetype/maven-archetype-plugin/usage.html>:.

- Ստեղծեք նոր նախագիծ ինտերակտիվ կերպով.:

`mvn archetype:generate`

- Ստեղծեք նախագիծ ոչ ինտերակտիվ կերպով՝ հատուկ արխետիպով և նախագծի պարամետրերով.:

`mvn archetype:generate --define archetypeGroupId={{group_id}} --define archetypeArtifactId={{artifact_id}} --define archetypeVersion={{version}} --define groupId={{project_group_id}} --define artifactId={{project_name}} --define interactiveMode=false`
