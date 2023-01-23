# lwp-request

> Egyszerű parancssori HTTP kliens. libwww-perl segítségével készült. További információ: <https://metacpan.org/pod/lwp-request>.

- Egyszerű GET kérés:

`lwp-request -m GET {{http://example.com/some/path}}`

- Fájl feltöltése POST kéréssel:

`lwp-request -m POST {{http://example.com/some/path}} < {{path/to/file}}`

- Kérés készítése egyéni felhasználói ügynökkel:

`lwp-request -H 'User-Agent: {{user_agent}} -m {{METHOD}} {{http://example.com/some/path}}`

- HTTP-hitelesítéssel történő kérés:

`lwp-request -C {{username}}:{{password}} -m {{METHOD}} {{http://example.com/some/path}}`

- Kérés készítése és a kérés fejlécének kinyomtatása:

`lwp-request -U -m {{METHOD}} {{http://example.com/some/path}}`

- Kérés készítése és válaszcímek és státuszlánc nyomtatása:

`lwp-request -E -m {{METHOD}} {{http://example.com/some/path}}`
