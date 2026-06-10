# xh

> Ընկերական և արագ գործիք HTTP հարցումներ ուղարկելու համար:.
> Նշում. `xh`, գրված է ժանգով, ծառայում է որպես `http`-ի արդյունավետ փոխարինում:.
> Տես նաև՝ `http`, `curl`:.
> Լրացուցիչ տեղեկություններ. <https://github.com/ducaale/xh#usage>:.

- Ուղարկեք GET հարցում (ցույց է տալիս պատասխանի վերնագրերը և բովանդակությունը).:

`xh {{https://postman-echo.com/get}}`

- Ուղարկեք POST հարցում JSON մարմնով (բանալին-արժեք զույգերը ավելացվում են վերին մակարդակի JSON օբյեկտին, օրինակ՝ `{"name": "john", "age": 25}`):

`xh post {{https://postman-echo.com/post}} {{name=john}} {{age=25}}`

- Ուղարկեք GET հարցում հարցման պարամետրերով (օրինակ՝ <https://postman-echo.com/response-headers?foo1=bar1&foo2=bar2>):

`xh get {{https://postman-echo.com/response-headers}} {{foo1==bar1}} {{foo2==bar2}}`

- Ուղարկեք GET հարցում հատուկ վերնագրով.:

`xh get {{https://postman-echo.com}} {{header-name:header-value}}`

- Կատարեք GET հարցում և պահեք պատասխանի մարմինը ֆայլում.:

`xh {{[-d|--download]}} {{https://example.com}} {{[-o|--output]}} {{path/to/file}}`

- Ստեղծեք հարցում, բայց մի ուղարկեք այն (նման է չոր վազքի).:

`xh --offline {{get|delete|...}} {{https://example.com}}`

- Ցույց տալ համարժեք `curl` հրամանը (սա որևէ հարցում չի ուղարկի).:

`xh --{{curl|curl-long}} {{--follow --verbose get https://example.com user-agent:curl}}`
