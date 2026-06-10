# acme.sh

> Shell սկրիպտը, որն իրականացնում է ACME հաճախորդի արձանագրությունը, այլընտրանք `certbot`-ին:.
> Տես նաև՝ `acme.sh dns`:.
> Լրացուցիչ տեղեկություններ. <https://github.com/acmesh-official/acme.sh#2-just-issue-a-cert>:.

- Թողարկեք վկայագիր՝ օգտագործելով webroot ռեժիմը.:

`acme.sh --issue {{[-d|--domain]}} {{example.com}} {{[-w|--webroot]}} /{{path/to/webroot}}`

- Թողարկեք վկայագիր բազմաթիվ տիրույթների համար՝ օգտագործելով ինքնուրույն ռեժիմ՝ օգտագործելով 80 նավահանգիստը.:

`acme.sh --issue --standalone {{[-d|--domain]}} {{example.com}} {{[-d|--domain]}} {{www.example.com}}`

- Թողարկեք վկայագիր՝ օգտագործելով ինքնուրույն TLS ռեժիմը, օգտագործելով պորտը 443:

`acme.sh --issue --alpn {{[-d|--domain]}} {{example.com}}`

- Թողարկեք վկայագիր՝ օգտագործելով աշխատանքային `nginx` կոնֆիգուրացիա՝:

`acme.sh --issue --nginx {{[-d|--domain]}} {{example.com}}`

- Թողարկեք վկայագիր՝ օգտագործելով աշխատանքային Apache կոնֆիգուրացիա.:

`acme.sh --issue --apache {{[-d|--domain]}} {{example.com}}`

- Տրամադրել wildcard (\*) վկայագիր՝ օգտագործելով ավտոմատ DNS API ռեժիմը.:

`acme.sh --issue --dns {{dns_cf}} {{[-d|--domain]}} {{*.example.com}}`

- Տեղադրեք վկայագրի ֆայլերը նշված վայրերում (օգտակար վկայագրի ավտոմատ նորացման համար).:

`acme.sh {{[-i|--install-cert]}} {{[-d|--domain]}} {{example.com}} --key-file /{{path/to/example.com.key}} --fullchain-file /{{path/to/example.com.cer}} --reloadcmd "{{systemctl force-reload nginx}}"`
