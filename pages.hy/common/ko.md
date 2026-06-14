#կո

> Կառուցեք և տեղակայեք Go հավելվածները որպես բեռնարկղային պատկերներ Kubernetes-ում:.
> Լրացուցիչ տեղեկություններ. <https://ko.build/reference/ko/>:.

- Կառուցեք և հրապարակեք կոնտեյների պատկեր Go փաթեթի ներմուծման ճանապարհից.:

`ko build {{import_path}}`

- Կառուցեք և բեռնեք կոնտեյների պատկեր տեղական Docker daemon-ում.:

`ko build {{[-L|--local]}} {{import_path}}`

- Կիրառել Kubernetes-ի մանիֆեստները՝ Go-ի պատկերների հղումներով, որոնք լուծվել են բովանդակության մեջ.:

`ko apply {{[-f|--filename]}} {{path/to/manifest.yaml}}`

- Ստեղծեք Kubernetes ռեսուրսներ լուծված պատկերների հղումներով.:

`ko create {{[-f|--filename]}} {{path/to/manifest.yaml}}`

- Տպեք լուծված Kubernetes-ի դրսևորումները՝ առանց դրանք կիրառելու.:

`ko resolve {{[-f|--filename]}} {{path/to/manifest.yaml}}`

- Կառուցեք և գործարկեք Go փաթեթ Kubernetes-ում.:

`ko run {{import_path}}`

- Ջնջել Kubernetes ռեսուրսները, որոնք սահմանված են մանիֆեստում.:

`ko delete {{[-f|--filename]}} {{path/to/manifest.yaml}}`

- Մուտք գործեք կոնտեյների ռեեստր.:

`ko login {{registry.example.com}} {{[-u|--username]}} {{username}} {{[-p|--password]}} {{password}}`
