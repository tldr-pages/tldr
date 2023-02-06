# swaks

> Swiss Army Knife SMTP, az SMTP tranzakció tesztelője. További információ: <https://github.com/jetmore/swaks/blob/develop/doc/base.pod>.

- Küldjön egy szabványos teszt e-mailt a `user@example.com` címre a `test-server.example.net` 25-ös portján:

`swaks --to {{user@example.com}} --server {{test-server.example.net}}`

- Kézbesítsen egy szabványos teszt e-mailt, amelyhez CRAM-MD5 hitelesítésre van szükség a `me@example.com` felhasználóként. Az e-mail testéhez egy "X-Test" fejléc kerül hozzáadásra:

`swaks --to {{user@example.com}} --from {{me@example.com}} --auth {{CRAM-MD5}} --auth-user {{me@example.com}} --header-X-Test "{{test_email}}"`

- Teszteljen egy víruskeresőt az EICAR használatával egy csatolmányban. Ne jelenítse meg az üzenet DATA részét:

`swaks -t {{user@example.com}} --attach - --server {{test-server.example.com}} --suppress-data {{path/to/eicar.txt}}`

- Teszteljen egy spamszkennert GTUBE használatával egy e-mail testében, a `example.com` MX rekordjain keresztül továbbítva:

`swaks --to {{user@example.com}} --body {{path/to/gtube_file}}`

- Kézbesítsen egy szabványos teszt e-mailt a `user@example.com` címre LMTP protokollt használva egy UNIX tartományi socket fájlon keresztül:

`swaks --to {{user@example.com}} --socket {{/var/lda.sock}} --protocol {{LMTP}}`
