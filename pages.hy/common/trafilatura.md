#տրաֆիլատուրա

> Վեբ գրելու և սողալու համար Python գործիք, որը վեբ էջերից հանում է հիմնական տեքստը, մետատվյալները և մեկնաբանությունները:.
> Նախատեսված է տեքստային կորպուսներ ստեղծելու և կառուցվածքային բովանդակություն հանելու համար:.
> Լրացուցիչ տեղեկություններ. <https://trafilatura.readthedocs.io/en/latest/usage-cli.html#further-information>:.

- Տեքստ հանեք URL-ից.:

`trafilatura {{[-u|--URL]}} {{url}}`

- Քաղեք տեքստը և պահեք ֆայլում.:

`trafilatura {{[-u|--URL]}} {{url}} {{[-o|--output-dir]}} {{path/to/output.txt}}`

- Քաղեք տեքստը JSON ձևաչափով.:

`trafilatura {{[-u|--URL]}} {{url}} --json`

- Քաղեք տեքստը ֆայլում թվարկված բազմաթիվ URL-ներից.:

`trafilatura {{[-i|--input-file]}} {{path/to/url_list.txt}}`

- Քայլեք կայք՝ օգտագործելով իր կայքի քարտեզը՝:

`trafilatura --sitemap {{url_to_sitemap.xml}}`

- Քաղեք տեքստը՝ պահպանելով HTML ձևաչափումը.:

`trafilatura {{[-u|--URL]}} {{url}} --formatting`

- Քաղեք տեքստը, ներառյալ մեկնաբանությունները.:

`trafilatura {{[-u|--URL]}} {{url}} --with-comments`

- Ցուցադրել օգնությունը.:

`trafilatura {{[-h|--help]}}`
