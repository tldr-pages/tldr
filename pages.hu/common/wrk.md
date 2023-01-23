# wrk

> HTTP benchmarking eszköz. További információ: <https://github.com/wg/wrk>.

- Futtasson egy benchmarkot `30` másodpercig, a `12` szálak használatával és a `400` HTTP-kapcsolatok nyitva tartásával:

`wrk -t{{12}} -c{{400}} -d{{30s}} "{{http://127.0.0.1:8080/index.html}}"`

- Futtasson benchmarkot egyéni fejléccel:

`wrk -t{{2}} -c{{5}} -d{{5s}} -H "{{Host: example.com}}" "{{http://example.com/index.html}}"`

- Futtasson benchmarkot `2` másodperces kérési időkorlátozással:

`wrk -t{{2}} -c{{5}} -d{{5s}} --timeout {{2s}} "{{http://example.com/index.html}}"`
