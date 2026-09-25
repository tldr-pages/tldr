# bg

> Hervat onderbroken jobs (bijvoorbeeld met `<Ctrl z>`) en laat ze op de achtergrond blijven draaien.
> Zie ook: `jobs`, `fg`, `disown`.
> Meer informatie: <https://www.gnu.org/software/bash/manual/bash.html#index-bg>.

- Hervat de meest recent onderbroken job en laat deze op de achtergrond draaien:

`bg`

- Hervat een specifieke job en laat deze op de achtergrond draaien (voer `jobs` uit om het jobnummer te vinden):

`bg %{{job_number}}`
