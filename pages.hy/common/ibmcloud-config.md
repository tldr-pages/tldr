# ibmcloud կոնֆիգուրացիա

> Փոփոխեք կամ կարդացեք արժեքները IBM Cloud CLI-ի կազմաձևում:.
> Լրացուցիչ տեղեկություններ. <https://cloud.ibm.com/docs/cli?topic=cli-ibmcloud_cli#ibmcloud_config>:.

- Սահմանեք HTTP հարցման ժամանակի վերջը 30 վայրկյան.:

`ibmcloud config --http-timeout 30`

- Միացնել հետքի ելքը HTTP հարցումների համար.:

`ibmcloud config --trace true`

- Հետևեք HTTP հարցումներին որոշակի ֆայլի.:

`ibmcloud config --trace {{path/to/trace_file}}`

- Անջատել գունային ելքը.:

`ibmcloud config --color false`

- Տեղադրեք տեղանքը որոշակի լեզվով.:

`ibmcloud config --locale {{zh_Hans}}`

- Միացնել SSO-ի մեկանգամյա ծածկագրի ավտոմատ ընդունումը.:

`ibmcloud config --sso-otp auto`
