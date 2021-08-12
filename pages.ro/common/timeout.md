# timeout

> Rulați o comandă cu o limită de timp.
> Mai multe informaţii: <https://www.gnu.org/software/coreutils/timeout>

- Rulați `sleep 10` și terminați-l, în cazul în care rulează pentru mai mult de 3 secunde:

`timeout {{3s}} {{sleep 10}}`

- Specificați semnalul care urmează să fie trimis la comandă după expirarea termenului. (În mod implicit, TERMEN este trimis):

`timeout --signal {{INT}} {{5s}} {{sleep 10}}`
