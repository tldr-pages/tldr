# mv

> Flytt eller gi nytt navn til filer og mapper.
> Mer informasjon: <https://www.gnu.org/software/coreutils/manual/html_node/mv-invocation.html>.

- Gi nytt navn til en fil eller mappe når målet ikke er en eksisterende mappe:

`mv {{sti/til/kilde}} {{sti/til/mål}}`

- Flytt en fil eller mappe inn i en eksisterende mappe:

`mv {{sti/til/kilde}} {{sti/til/eksisterende_mappe}}`

- Flytt flere filer inn i en eksisterende mappe, og behold filnavnene uendret:

`mv {{sti/til/kilde1 sti/til/kilde2 ...}} {{sti/til/eksisterende_mappe}}`

- Ikke spør om bekreftelse før eksisterende filer overskrives:

`mv {{[-f|--force]}} {{sti/til/kilde}} {{sti/til/mål}}`

- Spør om bekreftelse interaktivt før eksisterende filer overskrives, uavhengig av filrettigheter:

`mv {{[-i|--interactive]}} {{sti/til/kilde}} {{sti/til/mål}}`

- Ikke overskriv eksisterende filer på målet:

`mv {{[-n|--no-clobber]}} {{sti/til/kilde}} {{sti/til/mål}}`

- Flytt filer i detaljert modus, og vis filer etter at de er flyttet:

`mv {{[-v|--verbose]}} {{sti/til/kilde}} {{sti/til/mål}}`

- Angi målmappe slik at du kan bruke eksterne verktøy for å samle filer som skal flyttes:

`{{find /var/log -type f -name '*.log' -print0}} | {{xargs -0}} mv {{[-t|--target-directory]}} {{sti/til/målmappe}}`
