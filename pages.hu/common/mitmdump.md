# mitmdump

> A mitmproxy parancssori megfelelője. További információ: <https://docs.mitmproxy.org/stable/overview-tools/#mitmdump>.

- Indítson el egy proxyt, és mentse az összes kimenetet egy fájlba:

`mitmdump -w {{path/to/file}}`

- Egy elmentett forgalmi fájl szűrése csak a POST-kérelmekre:

`mitmdump -nr {{input_filename}} -w {{output_filename}} "{{~m post}}"`

- Egy elmentett forgalmi fájl újrajátszása:

`mitmdump -nc {{path/to/file}}`
