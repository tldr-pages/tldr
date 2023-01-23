# afplay

> Parancssoros audiólejátszó. További információ: <https://ss64.com/osx/afplay.html>.

- Hangfájl lejátszása (a lejátszás végéig vár):

`afplay {{path/to/file}}`

- Hangfájl lejátszása 2x-es sebességgel (lejátszási sebesség):

`afplay --rate {{2}} {{path/to/file}}`

- Hangfájl lejátszása fél sebességgel:

`afplay --rate {{0.5}} {{path/to/file}}`

- A hangfájl első N másodpercének lejátszása:

`afplay --time {{seconds}} {{path/to/file}}`
