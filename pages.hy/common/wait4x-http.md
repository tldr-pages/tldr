# սպասել4x http

> Սպասեք, մինչև HTTP(S) վերջնակետը հասանելի դառնա ճկուն վավերացման տարբերակներով:.
> Լրացուցիչ տեղեկություններ. <https://github.com/wait4x/wait4x>:.

- Սպասեք, մինչև HTTP վերջնակետը պատասխանի որոշակի կարգավիճակի կոդով.:

`wait4x http {{https://example.com/health}} --expect-status-code {{200}}`

- Սպասեք, որ պատասխան մարմինը համապատասխանի `regex` օրինակին.:

`wait4x http {{https://api.example.com/status}} --expect-body-regex '{{\"status\":\s*\"healthy\"}}'`

- Սպասեք կոնկրետ JSON դաշտի գոյությանը, օգտագործելով GJSON ուղու շարահյուսությունը.:

`wait4x http {{https://api.example.com/status}} --expect-body-json "{{services.database.status}}"`

- Սպասեք պատասխանի մաքսային հարցումների վերնագրերով.:

`wait4x http {{https://api.example.com}} --request-header "{{Authorization: Bearer token123}}"`

- Սպասեք, որ կոնկրետ պատասխանի վերնագիր համապատասխանի արժեքին.:

`wait4x http {{https://api.example.com}} --expect-header "{{Content-Type=application/json}}"`

- Սպասեք՝ օգտագործելով TLS հաճախորդի վկայականը.:

`wait4x http {{https://example.com}} --cert-file {{path/to/cert.pem}} --key-file {{path/to/key.pem}}`

- Սպասեք հատուկ ժամանակի ավարտով և շրջված ստուգմամբ (սպասեք մինչև վերջնակետը իջնի).:

`wait4x http {{https://example.com/health}} --expect-status-code {{200}} --invert-check --timeout {{60s}}`
