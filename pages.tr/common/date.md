# date

> Sistem tarihini görüntüleyin veya ayarlayın.
> Daha fazla bilgi için: <https://www.gnu.org/software/coreutils/manual/html_node/date-invocation.html>.

- Varsayılan yerel biçimi kullanarak geçerli tarihi görüntüleyin:

`date +%c`

- Geçerli tarihi UTC ve ISO 8601 formatında görüntüleyin:

`date {{[-u|--utc]}} +%Y-%m-%dT%H:%M:%SZ`

- Geçerli tarihi bir Unix zaman damgası olarak görüntüleyin (Unix zamanından bu yana geçen saniyeler):

`date +%s`

- Unix zaman damgası olarak belirtilen bir tarihi varsayılan biçime dönüştürün:

`date {{[-d|--date]}} @{{1473305798}}`

- Belirli bir tarihi Unix zaman damgası biçimine dönüştürün:

`date {{[-d|--date]}} "{{2018-09-01 00:00}}" +%s {{[-u|--utc]}}`

- Geçerli tarihi RFC-3339 biçiminde (`YYYY-AA-GG ss:dd:sn+ZD`) görüntüleyin ve duyarlılığını belirtin:

`date --rfc-3339 {{date|seconds|ns}}`

- Geçerli tarihi `AAGGssddYYYY.sn` biçimini kullanarak ayarlayın (`YYYY` ve `.sn` isteğe bağlıdır):

`sudo date {{093023592021.59}}`

- Geçerli ISO hafta numarasını görüntüleyin:

`date +%V`
