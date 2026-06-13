# tail

> Via den sista delen av en fil.
> Se även: `head`.
> Mer information: <https://www.gnu.org/software/coreutils/manual/html_node/tail-invocation.html>.

- Visa de sista 10 raderna av en fil:

`tail {{sökväg/till/fil}}`

- Visa de 10 sista raderna av flera olika filer:

`tail {{sökväg/till/fil1 sökväg/till/fil2 ...}}`

- Visa de sista 5 raderna av en fil:

`tail {{[-5|--lines 5]}} {{sökväg/till/fil}}`

- Visa de sista `antal` raderna av en fil:

`tail {{[-n|--lines]}} +{{antal}} {{sökväg/till/fil}}`

- Visa de sista `antal` bytes av en fil:

`tail {{[-c|--bytes]}} {{antal}} {{sökväg/till/fil}}`

- Visa de sista raderna av en fil och fortsätt läsa till `<Ctrl c>`:

`tail {{[-f|--follow]}} {{sökväg/till/fil}}`

- Fortsätt läsa filen till `<Ctrl c>`, även om filen blir oåtkomlig:

`tail {{[-F|--retry --follow]}} {{sökväg/till/fil}}`

- Visa de sista `antal` raderna i en fil och updatera varje `sekunder` sekunder:

`tail {{[-n|--lines]}} {{antal}} {{[-s|--sleep-interval]}} {{sekunder}} {{[-f|--follow]}} {{sökväg/till/fil}}`
