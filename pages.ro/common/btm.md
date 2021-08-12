# btm

> O alternativă la `top'.
> Scopul este de a fi ușor, cross-platform și mai grafic decât `top`.
> Mai multe informaţii: <https://github.com/ClementTsang/bottom>

- Afișați aspectul implicit (CPU, memorie, temperaturi, disc, rețea și procese):

`btm`

- Activați modul de bază, eliminarea diagramelor și a datelor de condensare (similar cu `top`):

`btm --basic`

- Utilizați puncte mari în loc de cele mici în diagrame:

`btm --dot_marker`

- Arată, de asemenea, încărcarea bateriei și starea de sănătate:

`btm --battery`

- Reîmprospătați la fiecare 250 milisecunde și afișați ultimele 30 de secunde în diagrame:

`btm --rate 250 --default_time_value 30000`
