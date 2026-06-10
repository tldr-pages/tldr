#քվարկուս

> Ստեղծեք Quarkus նախագծեր, կառավարեք ընդարձակումները և կատարեք հիմնական կառուցման և զարգացման առաջադրանքներ:.
> Լրացուցիչ տեղեկություններ. <https://quarkus.io/guides/cli-tooling>:.

- Ստեղծեք նոր հավելվածի նախագիծ նոր գրացուցակում.:

`quarkus create app {{project_name}}`

- Գործարկեք ընթացիկ նախագիծը կենդանի կոդավորման ռեժիմով.:

`quarkus dev`

- Գործարկել հավելվածը.:

`quarkus run`

- Գործարկեք ընթացիկ նախագիծը շարունակական փորձարկման ռեժիմով.:

`quarkus test`

- Ավելացրեք մեկ կամ մի քանի ընդարձակումներ ընթացիկ նախագծին.:

`quarkus extension add {{extension_name1 extension_name2 ...}}`

- Կառուցեք կոնտեյների պատկեր Docker-ի միջոցով.:

`quarkus image build docker`

- Տեղադրեք հավելվածը Kubernetes-ում.:

`quarkus deploy kubernetes`

- Թարմացնել նախագիծը.:

`quarkus update`
