# acme.sh --dns

> Használjon DNS-01 kihívást a TLS-tanúsítvány kiállításához. További információ: <https://github.com/acmesh-official/acme.sh/wiki>.

- Állítson ki tanúsítványt automatikus DNS API mód használatával:

`acme.sh --issue --dns {{gnd_gd}} --domain {{example.com}}`

- Állítson ki egy (csillaggal jelölt) joker-tanúsítványt automatikus DNS API mód használatával:

`acme.sh --issue --dns {{dns_namesilo}} --domain {{example.com}} --domain {{*.example.com}}`

- Tanúsítvány kiállítása DNS alias mód használatával:

`acme.sh --issue --dns {{dns_cf}} --domain {{example.com}} --challenge-alias {{alias-for-example-validation.com}}`

- Tanúsítvány kiállítása az automatikus Cloudflare / Google DNS-lekérdezés letiltása mellett a DNS-rekord hozzáadása után egy másodpercben megadott egyéni várakozási idő megadásával:

`acme.sh --issue --dns {{dns_namecheap}} --domain {{example.com}} --dnssleep {{300}}`

- Tanúsítvány kiállítása manuális DNS módban:

`acme.sh --issue --dns --domain {{example.com}} --yes-I-know-dns-manual-mode-enough-go-ahead-please`
