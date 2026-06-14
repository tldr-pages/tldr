#շարունակել

> Անցեք `for`, `while`, `until` կամ `select` հանգույցի հաջորդ կրկնությանը:.
> Լրացուցիչ տեղեկություններ. <https://www.gnu.org/software/bash/manual/bash.html#index-continue>:.

- Անցեք հաջորդ կրկնությանը.:

`while :; do continue; {{echo "This will never be reached"}}; done`

- Անցեք հաջորդ կրկնությանը` ներկառուցված օղակի ներսից.:

`for i in {{{1..3}}}; do {{echo $i}}; while :; do continue 2; done; done`
