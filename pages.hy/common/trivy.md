# մանրուք

> Սկանավորող՝ կոնտեյների պատկերների, ֆայլային համակարգերի և Git պահոցների խոցելիության, ինչպես նաև կազմաձևման խնդիրների համար:.
> Լրացուցիչ տեղեկություններ. <https://trivy.dev/docs/latest/guide/references/configuration/cli/trivy/>:.

- Սկանավորեք Docker պատկերը խոցելիության և բացահայտված գաղտնիքների համար.:

`trivy image {{image:tag}}`

- Սկանավորեք Docker պատկերը՝ զտելով ելքը ըստ խստության.:

`trivy image {{[-s|--severity]}} {{HIGH,CRITICAL}} {{alpine:3.15}}`

- Սկանավորեք Docker պատկերը՝ անտեսելով չֆիքսված/չկարկատված խոցելիությունը.:

`trivy image --ignore-unfixed {{alpine:3.15}}`

- Սկանավորեք ֆայլային համակարգը խոցելիության և սխալ կազմաձևումների համար.:

`trivy fs --scanners {{vuln,misconfig}} {{path/to/project_directory}}`

- Սկանավորեք IaC (Terraform, CloudFormation, ARM, Helm և Dockerfile) գրացուցակը սխալ կազմաձևումների համար.:

`trivy config {{path/to/iac_directory}}`

- Սկանավորեք տեղական կամ հեռավոր Git պահոցը խոցելիության համար.:

`trivy repo {{path/to/local_repository_directory|remote_repository_url}}`

- Սկանավորեք Git պահոցը մինչև կոնկրետ commit hash:

`trivy repo --commit {{commit_hash}} {{repository}}`

- Ստեղծեք արդյունք SARIF ձևանմուշով.:

`trivy image {{[-f|--format]}} {{template}} {{[-t|--template]}} "{{@sarif.tpl}}" {{[-o|--output]}} {{path/to/report.sarif}} {{image:tag}}`
