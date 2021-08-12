# locust

> Instrument de testare a încărcăturii pentru a determina numărul de utilizatori simultani pe care un sistem îl poate gestiona.
> Mai multe informaţii: <https://locust.io>

- Încărcare-test „example.com” cu interfață web folosind locustfile.py:

`locust --host={{http://example.com}}`

- Utilizați un fișier de test diferit:

`locust --locustfile={{test_file.py}} --host={{http://example.com}}`

- Rulați testul fără interfață web, reproducând 1 utilizator o secundă până când există 100 de utilizatori:

`locust --no-web --clients={{100}} --hatch-rate={{1}} --host={{http://example.com}}`

- Porniți lăcusta în modul master:

`locust --master --host={{http://example.com}}`

- Conectați sclavul lăcuste la maestru:

`locust --slave --host={{http://example.com}}`

- Conectați sclavul lăcuste pentru a stăpâni pe o mașină diferită:

`locust --slave --master-host={{master_hostname}} --host={{http://example.com}}`
