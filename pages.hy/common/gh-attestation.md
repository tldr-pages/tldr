# gh ատեստավորում

> Ներբեռնեք և ստուգեք արտեֆակտերի հավաստագրերը՝ դրանց ամբողջականությունն ու ծագումն ապահովելու համար:.
> Լրացուցիչ տեղեկություններ. <https://cli.github.com/manual/gh_attestation>:.

- Ներբեռնեք հավաստագրեր հատուկ պահեստի հետ կապված տեղական ֆայլի համար.:

`gh {{[at|attestation]}} download {{path/to/artifact.bin}} {{[-R|--repo]}} {{owner}}/{{repository}}`

- Ներբեռնեք հավաստագրեր կազմակերպության հետ կապված OCI կոնտեյների պատկերի համար.:

`gh {{[at|attestation]}} download oci://{{image_uri}} {{[-o|--owner]}} {{organization_name}}`

- Ստուգեք տեղական արտեֆակտը առցանց՝ կոնկրետ պահոցից ստացված վկայագրերի դեմ.:

`gh {{[at|attestation]}} verify {{path/to/artifact.bin}} {{[-R|--repo]}} {{owner}}/{{repository}}`

- Ստուգեք արտեֆակտը՝ պահանջելով, որ այն ստորագրված է հատուկ վերօգտագործվող աշխատանքային հոսքով՝ ուժեղացված անվտանգության համար.:

`gh {{[at|attestation]}} verify {{path/to/artifact.bin}} {{[-o|--owner]}} {{organization_name}} --signer-workflow {{owner}}/{{repository}}/{{path/to/workflow.yml}}`

- Ստուգեք արտեֆակտը և դուրս բերեք մանրամասն ստուգման արդյունքները որպես JSON՝ քաղաքականության շարժիչներում օգտագործելու համար.:

`gh {{[at|attestation]}} verify {{path/to/artifact.bin}} {{[-o|--owner]}} {{organization_name}} --format json`

- Կատարեք լիովին անցանց ստուգում՝ օգտագործելով ներբեռնված փաթեթը և սովորական վստահելի արմատային ֆայլը.:

`gh {{[at|attestation]}} verify {{path/to/artifact.bin}} {{[-b|--bundle]}} {{path/to/bundle.jsonl}} --custom-trusted-root {{path/to/trusted_root.jsonl}}`

- Պահպանեք հավաստագրերի ստորագրման վստահելի արմատը ֆայլում՝ անցանց ստուգման համար.:

`gh {{[at|attestation]}} trusted-root > {{path/to/trusted_root.jsonl}}`
