#դալֆոքս

> Հզոր բաց կոդով XSS սկաներ, որը կենտրոնացած է ավտոմատացման վրա:.
> Լրացուցիչ տեղեկություններ. <https://dalfox.hahwul.com/reference/cli/>:.

- Սկանավորեք մեկ URL XSS խոցելիության համար.:

`dalfox url {{https://example.com}}`

- Սկանավորեք URL՝ օգտագործելով վերնագիր՝ նույնականացման համար.:

`dalfox url {{https://example.com}} {{[-H|--header]}} '{{X-My-Header: 123}}'`

- Սկանավորեք URL-ների ցանկը ֆայլից.:

`dalfox file {{path/to/file}}`

- Սկսեք Dalfox-ը որպես REST API սերվեր.:

`dalfox server --host {{0.0.0.0}} --port {{8080}}`
