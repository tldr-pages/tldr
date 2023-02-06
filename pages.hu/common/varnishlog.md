# varnishlog

> Varnish naplók megjelenítése. További információ: <https://varnish-cache.org/docs/trunk/reference/varnishlog.html>.

- Naplók megjelenítése valós időben:

`varnishlog`

- Csak egy adott tartományhoz érkező kérések megjelenítése:

`varnishlog -q 'ReqHeader eq "Host: {{example.com}}"'`

- Csak a POST kérések megjelenítése:

`varnishlog -q 'ReqMethod eq "{{POST}}"'`

- Csak egy adott elérési útvonalra irányuló kérések megjelenítése:

`varnishlog -q 'ReqURL eq "{{/path}}"'`

- Csak a reguláris kifejezésnek megfelelő elérési utakhoz érkező kérések megjelenítése:

`varnishlog -q 'ReqURL ~ "{{regex}}"'`
