# rm

> Fjern filer eller mapper.
> Se også: `rmdir`, `trash`.
> Mer informasjon: <https://www.gnu.org/software/coreutils/manual/html_node/rm-invocation.html>.

- Fjern bestemte filer:

`rm {{sti/til/fil1 sti/til/fil2 ...}}`

- Fjern bestemte filer og ignorer dem som ikke finnes:

`rm {{[-f|--force]}} {{sti/til/fil1 sti/til/fil2 ...}}`

- Fjern bestemte filer interaktivt med spørsmål før hver fjerning:

`rm {{[-i|--interactive]}} {{sti/til/fil1 sti/til/fil2 ...}}`

- Fjern bestemte filer og skriv ut informasjon om hver fjerning:

`rm {{[-v|--verbose]}} {{sti/til/fil1 sti/til/fil2 ...}}`

- Fjern bestemte filer og mapper rekursivt:

`rm {{[-r|--recursive]}} {{sti/til/fil_eller_mappe1 sti/til/fil_eller_mappe2 ...}}`

- Fjern tomme mapper (dette regnes som den trygge metoden):

`rm {{[-d|--dir]}} {{sti/til/mappe}}`
