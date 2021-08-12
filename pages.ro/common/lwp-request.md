# lwp-request

> Simplu client HTTP linie de comandă.
> Construit cu libwww-perl.
> Mai multe informaţii: <https://metacpan.org/pod/lwp-request>

- Faceți o cerere simplă de obținere:

`lwp-request -m GET {{http://example.com/some/path}}`

- Încărcați un fișier cu o cerere POST:

`lwp-request -m POST {{http://example.com/some/path}} < {{path/to/file}}`

- Faceți o cerere cu un agent utilizator personalizat:

`lwp-request -H 'User-Agent: {{user_agent}} -m {{METHOD}} {{http://example.com/some/path}}`

- Faceți o solicitare cu autentificare HTTP:

`lwp-request -C {{username}}:{{password}} -m {{METHOD}} {{http://example.com/some/path}}`

- Efectuați o cerere și imprimați anteturi cerere:

`lwp-request -U -m {{METHOD}} {{http://example.com/some/path}}`

- Efectuați o solicitare și imprimați anteturi de răspuns și lanț de stare:

`lwp-request -E -m {{METHOD}} {{http://example.com/some/path}}`
