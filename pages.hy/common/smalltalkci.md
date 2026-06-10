# smalltalkci

> Smalltalk նախագծերի փորձարկման շրջանակ GitHub Actions-ի, Travis CI-ի, AppVeyor-ի, GitLab CI-ի և այլոց հետ:.
> Լրացուցիչ տեղեկություններ. <https://github.com/hpi-swa/smalltalkCI>:.

- Գործարկել թեստերը կազմաձևման ֆայլի համար.:

`smalltalkci {{path/to/.smalltalk.ston}}`

- Գործարկեք թեստեր `.smalltalk.ston` կոնֆիգուրացիայի համար ընթացիկ գրացուցակում.:

`smalltalkci`

- Վրիպազերծման թեստեր գլխային ռեժիմում (ցույց տալ VM պատուհանը).:

`smalltalkci --headful`

- Ներբեռնեք և պատրաստեք թեստերի համար հայտնի smalltalk պատկեր.:

`smalltalkci --smalltalk {{Squeak64-Trunk}}`

- Նշեք հատուկ Smalltalk պատկեր և VM:

`smalltalkci --image {{path/to/Smalltalk.image}} --vm {{path/to/vm}}`

- Մաքրել քեշերը և ջնջել կառուցումները.:

`smalltalkci --clean`
