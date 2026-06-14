# lwp-խնդրանք

> Պարզ HTTP հաճախորդ:.
> Կառուցված է libwww-perl-ով:.
> Լրացուցիչ տեղեկություններ. <https://metacpan.org/pod/lwp-request>:.

- Կատարեք պարզ GET հարցում.:

`lwp-request -m GET {{http://example.com/some/path}}`

- Վերբեռնեք ֆայլ POST հարցումով.:

`lwp-request < {{path/to/file}} -m POST {{http://example.com/some/path}}`

- Հարցում կատարեք մաքսային օգտվողի գործակալի հետ.:

`lwp-request -H 'User-Agent: {{user_agent}} -m {{METHOD}} {{http://example.com/some/path}}`

- Հարցում կատարեք HTTP նույնականացման միջոցով.:

`lwp-request -C {{username}}:{{password}} -m {{METHOD}} {{http://example.com/some/path}}`

- Կատարեք հարցում և տպեք հարցումների վերնագրերը.:

`lwp-request -U -m {{METHOD}} {{http://example.com/some/path}}`

- Կատարեք հարցում և տպեք պատասխանի վերնագրերը և կարգավիճակի շղթան.:

`lwp-request -E -m {{METHOD}} {{http://example.com/some/path}}`
