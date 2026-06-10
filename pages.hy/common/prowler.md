# արշավորդ

> Կատարեք անվտանգության լավագույն փորձի գնահատումներ, աուդիտներ և համապատասխանության ստուգումներ AWS-ում, Azure-ում, Google Cloud-ում և Kubernetes-ում:.
> Տես նաև՝ `prowler-aws`, `prowler-azure`, `prowler-gcp`, `prowler-kubernetes`, `prowler-m365`, `prowler-github`:.
> Լրացուցիչ տեղեկություններ. <https://docs.prowler.com/user-guide/cli/tutorials/misc>:.

- Գործարկել AWS, Azure, GCP, Kubernetes - որպես մատակարար - աուդիտ լռելյայն ստուգումներով.:

`prowler {{provider}}`

- Ցույց տալ բոլոր հասանելի ստուգումները կոնկրետ մատակարարի համար.:

`prowler {{provider}} {{[-l|--list-checks]}}`

- Ցույց տալ բոլոր հասանելի ծառայությունները կոնկրետ մատակարարի համար.:

`prowler {{provider}} --list-services`

- Ստեղծեք ելք բազմաթիվ ձևաչափերով, ներառյալ JSON-ASFF AWS Security Hub-ի համար.:

`prowler {{provider}} --output-modes {{csv,json-asff,html,...}}`

- Կատարել բանավոր ռեժիմով.:

`prowler {{provider}} --verbose`

- Զտեք բացահայտումները ըստ կարգավիճակի.:

`prowler {{provider}} --status {{PASS,FAIL,MANUAL}}`

- Ցուցադրել օգնությունը.:

`prowler --help`

- Ցուցադրման տարբերակը:

`prowler {{[-v|--version]}}`
