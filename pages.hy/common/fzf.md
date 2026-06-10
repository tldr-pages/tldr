# fzf

> Մշուշոտ որոնիչ:.
> Նման `sk`-ին:.
> Լրացուցիչ տեղեկություններ. <https://github.com/junegunn/fzf#usage>:.

- Սկսեք `fzf`-ը նշված գրացուցակի բոլոր ֆայլերի վրա.:

`find {{path/to/directory}} -type f | fzf`

- Գործընթացների գործարկման համար գործարկեք `fzf`.:

`ps aux | fzf`

- Ընտրեք մի քանի ֆայլ `<Shift Tab>`-ով և գրեք ֆայլում՝:

`find {{path/to/directory}} -type f | fzf {{[-m|--multi]}} > {{path/to/file}}`

- Սկսեք `fzf`-ը նշված հարցումով.:

`fzf {{[-q|--query]}} "{{query}}"`

- Սկսեք `fzf` այն գրառումներում, որոնք սկսվում են `core`-ով և ավարտվում `go`, `rb` կամ `py`-ով:

`fzf {{[-q|--query]}} "^core go$ | rb$ | py$"`

- Սկսեք `fzf` գրառումները, որոնք չեն համապատասխանում `pyc`-ին և պարունակում են `travis`:

`fzf {{[-q|--query]}} '!pyc travis'`
