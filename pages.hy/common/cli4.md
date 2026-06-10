# cli4

> Python հրամանի տող ինտերֆեյս Cloudflare API-ի համար:.
> Լրացուցիչ տեղեկություններ. <https://github.com/cloudflare/python-cloudflare>:.

- Ցուցադրել հաշվի տվյալները.:

`cli4 {{/user}}`

- Նշեք բոլոր գոտիները.:

`cli4 {{/zones}}`

- Ցուցակեք DNS գրառումները որոշակի գոտու համար.:

`cli4 {{/zones/:example.com/dns_records}}`

- Ստեղծեք նոր DNS գրառում.:

`cli4 --post {{name=example.com}} {{type=A}} {{content=192.0.2.1}} {{/zones/:example.com/dns_records}}`

- Թարմացրեք առկա DNS գրառումը.:

`cli4 --put {{name=sub.example.com}} {{type=A}} {{content=192.0.2.2}} {{/zones/:example.com/dns_records/:record_id}}`

- Ջնջել DNS գրառումը.:

`cli4 --delete {{/zones/:example.com/dns_records/:record_id}}`

- Մաքրել ամբողջ քեշը մի գոտու համար.:

`cli4 --post {{purge_everything=true}} {{/zones/:example.com/purge_cache}}`
