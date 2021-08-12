# dvc fetch

> Descărcați fișiere și directoare DVC urmărite dintr-un depozit la distanță.
> Mai multe informaţii: <https://dvc.org/doc/command-reference/fetch>

- Obțineți cele mai recente modificări din depozitul implicit de la distanță din amonte (dacă este setat):

`dvc fetch`

- Preluare modificări de la un anumit depozit la distanță din amonte:

`dvc fetch --remote {{remote_name}}`

- Obține cele mai recente modificări pentru un anumit țint/s:

`dvc fetch {{target/s}}`

- Fetch modificări pentru toate ramurile și etichetele:

`dvc fetch --all-branches --all-tags`

- Fetch modificări pentru toate angajările:

`dvc fetch --all-commits`
