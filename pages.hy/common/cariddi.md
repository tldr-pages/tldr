#կարիդդի

> Զննեք URL-ները և սկանավորեք վերջնակետերը, գաղտնիքները, api ստեղները, ֆայլերի ընդլայնումները, նշանները և ավելին տիրույթների ցանկից:.
> Լրացուցիչ տեղեկություններ. <https://github.com/edoardottt/cariddi/wiki>:.

- Որոնեք գաղտնիքներ՝ օգտագործելով հատուկ `regex`ներ և JSON-ում ելքային արդյունքներ.:

`cat {{path/to/urls.txt}} | cariddi -s -sf {{path/to/custom_secrets.txt}} -json`

- Որոնեք հյութալի վերջնակետեր բարձր միաժամանակությամբ և ժամանակի ընդմիջումով պարզ ելքային արդյունքներով.:

`cat {{path/to/urls.txt}} | cariddi -e -c {{250}} -t {{15}} -plain`

- Որոնեք վրիպազերծման ռեժիմով և պահեք HTTP պատասխաններն ու արդյունքները `txt` ֆայլում՝:

`cat {{path/to/urls.txt}} | cariddi -debug -sr -ot {{path/to/debug_output.txt}}`

- Կատարեք ինտենսիվ զննում վստահված անձի և պատահական օգտագործողի գործակալի հետ և արդյունքները թողարկեք `html` ֆայլում՝:

`cat {{path/to/urls.txt}} | cariddi -intensive -proxy {{http://127.0.0.1:8080}} -rua -oh {{path/to/intensive_crawl.html}}`

- Որոնեք սխալներ և օգտակար տեղեկատվություն հատուկ ուշացումով և օգտագործեք `.cariddi_cache` պանակը որպես քեշ:

`cat {{path/to/urls.txt}} | cariddi -err -info -d {{3}} -cache`

- Ցույց տալ օգտագործման օրինակներ.:

`cariddi -examples`
