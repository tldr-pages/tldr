# kubeseal

> Հաճախորդի կողմից նախատեսված գործիք՝ Kubernetes-ի գաղտնիքները կոդավորելու համար՝ օգտագործելով Bitnami Sealed Secrets կարգավորիչը:.
> Ստեղծում է SealedSecret ռեսուրսներ, որոնք կարող են ապահով կերպով պահվել տարբերակի վերահսկման մեջ:.
> Պահանջում է կլաստերում աշխատող կարգավորիչ (օրինակ՝ տեղադրված `kubectl apply --filename controller.yaml`-ի միջոցով):.
> Լրացուցիչ տեղեկություններ. <https://github.com/bitnami-labs/sealed-secrets>:.

- Գաղտնագրեք Kubernetes գաղտնիքը YAML ֆայլից SealedSecret-ի մեջ (լռելյայն JSON ելք).:

`kubeseal < {{secret.yaml}} > {{sealedsecret.json}}`

- Գաղտնագրեք գաղտնիքը, այն թողարկեք YAML կամ JSON ձևաչափով, օգտագործելով API-ի նույնականացման կրող նշան.:

`kubeseal < {{secret.yaml}} {{[-o|--format]}} {{yaml|json}} --token {{my-bearer-token}} > {{sealedsecret.yaml}}`

- Գաղտնիքը կնքեք՝ օգտագործելով կնքված գաղտնիքների վերահսկիչի հատուկ վերահսկիչի անվան տարածք և անվանում.:

`kubeseal < {{secret.yaml}} --controller-namespace {{controller-namespace}} --controller-name {{controller-name}} > {{sealedsecret.yaml}}`

- Գաղտնագրեք չմշակված գաղտնի արժեքը նշված անունով և ծավալով ֆայլից.:

`kubeseal --raw --from-file {{path/to/secret.txt}} --name {{my-secret}} --scope {{strict|namespace-wide|cluster-wide}} > {{sealedsecret.yaml}}`

- Ստացեք վերահսկիչի հանրային վկայականը անցանց կնքման համար հիմնական վավերագրով.:

`kubeseal --fetch-cert --username {{username}} --password {{password}} > {{cert.pem}}`

- Գաղտնի փակեք անցանց՝ օգտագործելով բերված վկայականը.:

`kubeseal < {{secret.yaml}} --cert {{cert.pem}} > {{sealedsecret.yaml}}`

- Միավորել գաղտնիքը գոյություն ունեցող SealedSecret ֆայլի մեջ.:

`kubeseal < {{secret.yaml}} --merge-into {{sealedsecret.yaml}}`

- Վավերացրե՛ք SealedSecret-ը՝ առանց այն կիրառելու.:

`kubeseal < {{sealedsecret.yaml}} --validate`
