# scrcpy

> Afișați și controlați dispozitivul Android pe un desktop.
> Mai multe informaţii: <https://github.com/Genymobile/scrcpy>

- Afișează o oglindă a unui dispozitiv conectat:

`scrcpy`

- Afișează o oglindă a unui anumit dispozitiv pe baza ID-ului sau a adresei IP (găsește sub comanda `dispozitive adb”):

`scrcpy --serial {{0123456789abcdef|192.168.0.1:5555}}`

- Porniți afișarea în modul ecran complet:

`scrcpy --fullscreen`

- Rotiți ecranul de afișare. Fiecare valoare incrementală adaugă o rotație de 90 de grade în sens invers acelor de ceasornic:

`scrcpy --rotation {{0|1|2|3}}`

- Arată atingeri pe dispozitivul fizic:

`scrcpy --show-touches`

- Ecran de înregistrare:

`scrcpy --record {{path/to/file.mp4}}`

- Setați directorul țintă pentru împingerea fișierelor la dispozitiv prin drag and drop (non-APK):

`scrcpy --push-target {{path/to/directory}}`
