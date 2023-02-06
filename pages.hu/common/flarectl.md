# flarectl

> A Cloudflare hivatalos CLI-je. További információ: <https://github.com/cloudflare/cloudflare-go/blob/master/cmd/flarectl/README.md>.

- Egy adott IP blokkolása:

`flarectl firewall rules create --zone="{{example.com}}" --value="{{8.8.8.8}}" --mode="{{block}}" --notes="{{Block bad actor}}"`

- DNS-bejegyzés hozzáadása:

`flarectl dns create --zone="{{example.com}}" --name="{{app}}" --type="{{CNAME}}" --content="{{myapp.herokuapp.com}}" --proxy`

- Az összes Cloudflare IPv4/IPv6 tartomány listázása:

`flarectl ips --ip-type {{ipv4|ipv6|all}}`

- Számos új Cloudflare zóna automatikus létrehozása a `domains.txt` oldalon található nevekkel:

`for domain in $(cat {{domains.txt}}); do flarectl zone info --zone=$domain; done`

- Az összes tűzfalszabály listázása:

`flarectl firewall rules list`
