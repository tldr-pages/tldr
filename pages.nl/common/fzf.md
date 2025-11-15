# fzf

> Fuzzy finder.
> Vergelijkbaar met `sk`.
> Meer informatie: <https://github.com/junegunn/fzf#usage>.

- Start `fzf` op alle bestanden in de opgegeven map:

`find {{pad/naar/map}} -type f | fzf`

- Start `fzf` voor actieve processen:

`ps aux | fzf`

- Selecteer meerdere bestanden met `<Shift Tab>` en schrijf naar een bestand:

`find {{pad/naar/map}} -type f | fzf {{[-m|--multi]}} > {{pad/naar/bestand}}`

- Start `fzf` met een bepaalde query:

`fzf {{[-q|--query]}} "{{query}}"`

- Start `fzf` op items die beginnen met `core` en eindigen met `go`, `rb` of `py`:

`fzf {{[-q|--query]}} "^core go$ | rb$ | py$"`

- Start `fzf` op items die niet overeenkomen met `pyc`, maar wel `travis` bevatten:

`fzf {{[-q|--query]}} '!pyc travis'`
