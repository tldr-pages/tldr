# wrk

> instrument de analiză comparativă HTTP.
> Mai multe informaţii: <https://github.com/wg/wrk>

- Rulați un punct de referință timp de `30` secunde, folosind fire `12` și menținând deschise conexiunile HTTP „400`:

`wrk -t{{12}} -c{{400}} -d{{30s}} "{{http://127.0.0.1:8080/index.html}}"`

- Rulați un punct de referință cu un antet personalizat:

`wrk -t{{2}} -c{{5}} -d{{5s}} -H "{{Host: example.com}}" "{{http://example.com/index.html}}"`

- Rulați un criteriu de referință cu o expirare a solicitării de `2` secunde:

`wrk -t{{2}} -c{{5}} -d{{5s}} --timeout {{2s}} "{{http://example.com/index.html}}"`
