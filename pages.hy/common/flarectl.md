# flarectl

> Պաշտոնական CLI Cloudflare-ի համար:.
> Լրացուցիչ տեղեկություններ. <https://github.com/cloudflare/cloudflare-go/blob/v0/cmd/flarectl/README.md>:.

- Արգելափակել կոնկրետ IP.:

`flarectl firewall rules create --zone="{{example.com}}" --value="{{8.8.8.8}}" --mode="{{block}}" --notes="{{Block bad actor}}"`

- Ավելացնել DNS գրառում.:

`flarectl dns create --zone="{{example.com}}" --name="{{app}}" --type="{{CNAME}}" --content="{{myapp.herokuapp.com}}" --proxy`

- Թվարկեք Cloudflare IPv4/IPv6 բոլոր տիրույթները.:

`flarectl ips --ip-type {{ipv4|ipv6|all}}`

- Ստեղծեք շատ նոր Cloudflare գոտիներ ինքնաբերաբար `domains.txt`-ից անուններով.:

`for domain in $(cat {{domains.txt}}); do flarectl zone info --zone=$domain; done`

- Թվարկեք firewall-ի բոլոր կանոնները.:

`flarectl firewall rules list`
