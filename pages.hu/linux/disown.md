# disown

> Engedélyezi, hogy az alfolyamatok azon a héjon túl is éljenek, amelyhez kapcsolódnak. Lásd még a `jobs` parancsot. További információ: <https://www.gnu.org/software/bash/manual/bash.html#index-disown>.

- Az aktuális munka letiltása:

`disown`

- Egy adott munka letiltása:

`disown %{{job_number}}`

- Az összes munka letiltása:

`disown -a`

- Megtartja a munkát (nem tagadja meg), de megjelöli, hogy a shell kilépésekor a jövőben ne kapjon SIGHUP-ot:

`disown -h %{{job_number}}`
