# jenkins-cli

> Բաց կոդով ավտոմատացման սերվեր, որը հեշտացնում է ծրագրային ապահովման մշակման կյանքի ցիկլի ավտոմատացումը:.
> Լրացուցիչ տեղեկություններ. <https://www.jenkins.io/doc/>:.

- Միացեք jenkins CLI-ին.:

`java -jar jenkins-cli.jar -s {{jenkins_server_url}} -auth {{username}}:{{api_token}}`

- Վերագործարկեք jenkins-ը.:

`java -jar jenkins-cli.jar -s {{jenkins_server_url}} restart`

- Անջատում jenkins:

`java -jar jenkins-cli.jar -s {{jenkins_server_url}} shutdown`

- Ցուցադրել օգնությունը.:

`java -jar jenkins-cli.jar -s {{jenkins_server_url}} help`

- Ցուցադրման տարբերակը:

`java -jar jenkins-cli.jar -s {{jenkins_server_url}} version`
