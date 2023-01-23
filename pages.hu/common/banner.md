# banner

> A megadott argumentumot nagy ASCII-képként nyomtatja ki. További információ: <https://manned.org/banner>.

- A szöveges üzenet nyomtatása nagyméretű bannerként (az idézőjelek opcionálisak):

`banner "{{Hello World}}"`

- A szöveges üzenet 50 karakter széles bannerként történő nyomtatása:

`banner -w {{50}} "{{Hello World}}"`

- Szöveg beolvasása a `stdin` oldalról:

`banner`
