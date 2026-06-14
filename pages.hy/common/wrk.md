#գործ

> HTTP չափորոշիչ գործիք:.
> Լրացուցիչ տեղեկություններ. <https://github.com/wg/wrk#basic-usage>:.

- Գործարկել հենանիշը `30` վայրկյանի ընթացքում՝ օգտագործելով `12` շղթաները և բաց պահելով `400` HTTP կապերը:

`wrk {{[-t|--threads]}} {{12}} {{[-c|--connections]}} {{400}} {{[-d|--duration]}} {{30s}} "{{http://127.0.0.1:8080/index.html}}"`

- Գործարկեք հենանիշ հատուկ վերնագրով.:

`wrk {{[-t|--threads]}} {{2}} {{[-c|--connections]}} {{5}} {{[-d|--duration]}} {{5s}} {{[-H|--header]}} "{{Host: example.com}}" "{{http://example.com/index.html}}"`

- Գործարկեք հենանիշ՝ `2` վայրկյանի հարցման ժամկետի ավարտով:

`wrk {{[-t|--threads]}} {{2}} {{[-c|--connections]}} {{5}} {{[-d|--duration]}} {{5s}} --timeout {{2s}} "{{http://example.com/index.html}}"`
