# մատուցողուհի-սպասարկում

> Մաքուր Python WSGI HTTP սերվեր:.
> Լրացուցիչ տեղեկություններ. <https://docs.pylonsproject.org/projects/waitress/en/latest/runner.html>:.

- Գործարկել Python վեբ հավելվածը.:

`waitress-serve {{import.path:wsgi_func}}`

- Լսեք 8080 նավահանգստում localhost-ում.:

`waitress-serve --listen={{localhost}}:{{8080}} {{import.path:wsgi_func}}`

- Սկսեք մատուցողուհին Unix վարդակից.:

`waitress-serve --unix-socket={{path/to/socket}} {{import.path:wsgi_func}}`

- Օգտագործեք 4 թեմա՝ հարցումները մշակելու համար.:

`waitress-serve --threads={{4}} {{import.path:wsgifunc}}`

- Կանչեք գործարանային մեթոդ, որը վերադարձնում է WSGI օբյեկտ.:

`waitress-serve --call {{import.path.wsgi_factory}}`

- Օգտագործեք HTTPS URL սխեման.:

`waitress-serve --url-scheme={{https}} {{import.path:wsgi_func}}`
