# mogrify

> Efectuați operații pe mai multe imagini, cum ar fi redimensionarea, decuparea, răsturnarea și adăugarea de efecte.
> Modificările se aplică direct la fișierul original.
> Mai multe informaţii: <https://imagemagick.org/script/mogrify.php>

- Redimensionați toate imaginile JPEG din director la 50% din dimensiunea inițială:

`mogrify -resize {{50%}} {{*.jpg}}`

- Redimensionați toate imaginile începând cu „DSC” la 800x600:

`mogrify -resize {{800x600}} {{DSC*}}`

- Conversia tuturor imaginilor PNG din director la JPEG:

`mogrify -format {{jpg}} {{*.png}}`

- Înjumătăți saturația tuturor fișierelor de imagine din directorul curent:

`mogrify -modulate {{100,50}} {{*}}`

- Dublați luminozitatea tuturor fișierelor de imagine din directorul curent:

`mogrify -modulate {{200}} {{*}}`
