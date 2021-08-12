# xvfb-run

> Executați o comandă într-un mediu virtual de server X.
> Mai multe informaţii: <https://www.x.org/wiki/>

- Rulați comanda specificată într-un server virtual X:

`xvfb-run {{command}}`

- Încercați să obțineți un număr de server gratuit, dacă valoarea implicită (99) nu este disponibilă:

`xvfb-run --auto-servernum {{command}}`

- Treceți argumente la serverul Xvfb:

`xvfb-run --server-args "{{-screen 0 1024x768x24}}" {{command}}`
