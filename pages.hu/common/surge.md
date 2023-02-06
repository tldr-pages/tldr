# surge

> Egyszerű parancssori webes publikálás. További információ: <https://surge.sh>.

- Új webhely feltöltése a surge.sh-be:

`surge {{path/to/my_project}}`

- Telepítse a webhelyet az egyéni tartományba (vegye figyelembe, hogy a DNS-bejegyzéseknek a surge.sh aldomainre kell mutatniuk):

`surge {{path/to/my_project}} {{my_custom_domain.com}}`

- Listázza ki a surge projektjeit:

`surge list`

- Projekt eltávolítása:

`surge teardown {{my_custom_domain.com}}`
