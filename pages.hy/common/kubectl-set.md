# kubectl հավաքածու

> Թարմացրեք առկա կիրառական ռեսուրսների դաշտերը:.
> Լրացուցիչ տեղեկություններ. <https://kubernetes.io/docs/reference/kubectl/generated/kubectl_set/>:.

- Թարմացրեք կոնտեյների պատկերը տեղակայման մեջ.:

`kubectl set image {{[deploy|deployment]}}/{{deployment_name}} {{container_name}}={{image}}`

- Թարմացրեք բոլոր բեռնարկղերի պատկերը տեղակայման մեջ.:

`kubectl set image {{[deploy|deployment]}}/{{deployment_name}} *={{image}}`

- Սահմանեք ռեսուրսների սահմանաչափերը (CPU և հիշողություն) տեղակայման վրա.:

`kubectl set resources {{[deploy|deployment]}}/{{deployment_name}} --limits cpu={{cpu_limit}},memory={{memory_limit}}`

- Տեղադրեք շրջակա միջավայրի փոփոխականը տեղակայման վրա.:

`kubectl set env {{[deploy|deployment]}}/{{deployment_name}} {{variable_name}}={{value}}`

- Հեռացնել միջավայրի փոփոխականը տեղակայումից.:

`kubectl set env {{[deploy|deployment]}}/{{deployment_name}} {{variable_name}}-`

- Ներմուծեք միջավայրի փոփոխականները գաղտնիքից կամ ConfigMap-ից.:

`kubectl set env --from {{secret|configmap}}/{{resource_name}} {{[deploy|deployment]}}/{{deployment_name}}`

- Թարմացրեք տեղակայման ծառայության հաշիվը.:

`kubectl set {{[sa|serviceaccount]}} {{[deploy|deployment]}}/{{deployment_name}} {{service_account_name}}`
