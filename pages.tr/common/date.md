# date

> Sistem tarihini görüntüleyin veya ayarlayın.
> Daha fazla bilgi: <https://www.gnu.org/software/coreutils/date>.

- Varsayılan yerel biçimi kullanarak geçerli tarihi görüntüleyin:

`date +"%c"`

- Geçerli tarihi UTC ve ISO 8601 formatında görüntüleyin:

`date -u +"%Y-%m-%dT%H:%M:%S%Z"`

- Geçerli tarihi bir Unix zaman damgası olarak görüntüleyin (Unix zamanından bu yana geçen saniyeler):

`date +%s`

- Varsayılan biçimi kullanarak belirli bir tarihi (Unix zaman damgası olarak) görüntüleyin:

`date -d @1473305798`

- Belirli bir tarihi Unix zaman damgası biçimine dönüştürün:

`date -d "{{2018-09-01 00:00}}" +%s --utc`

- RFC-3339 biçimini kullanarak geçerli tarihi görüntüleyin (`YYYY-AA-GG ss:dd:ss ZD`):

`date --rfc-3339=s`
