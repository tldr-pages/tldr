# acme.sh --dns

> Օգտագործեք DNS-01 մարտահրավեր՝ TLS վկայական տալու համար:.
> Լրացուցիչ տեղեկություններ. <https://github.com/acmesh-official/acme.sh/wiki>:.

- Վկայական տրամադրեք՝ օգտագործելով ավտոմատ DNS API ռեժիմը.:

`acme.sh --issue --dns {{dns_gd}} --domain {{example.com}}`

- Տրամադրել wildcard վկայագիր (նշվում է աստղանիշով)՝ օգտագործելով ավտոմատ DNS API ռեժիմը.:

`acme.sh --issue --dns {{dns_namesilo}} --domain {{example.com}} --domain {{*.example.com}}`

- Թողարկեք վկայագիր՝ օգտագործելով DNS alias ռեժիմը.:

`acme.sh --issue --dns {{dns_cf}} --domain {{example.com}} --challenge-alias {{alias-for-example-validation.com}}`

- Թողարկեք վկայագիր՝ անջատելով ավտոմատ Cloudflare/Google DNS հարցումը DNS գրառումն ավելացնելուց հետո՝ նշելով հատուկ սպասման ժամանակը վայրկյաններով.:

`acme.sh --issue --dns {{dns_namecheap}} --domain {{example.com}} --dnssleep {{300}}`

- Տրամադրել վկայագիր՝ օգտագործելով ձեռքով DNS ռեժիմ.:

`acme.sh --issue --dns --domain {{example.com}} --yes-I-know-dns-manual-mode-enough-go-ahead-please`
