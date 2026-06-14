#ընդմիջում

> Կտրվեք `for`, `while`, `until` կամ `select` հանգույցից:.
> Լրացուցիչ տեղեկություններ. <https://www.gnu.org/software/bash/manual/bash.html#index-break>:.

- Դուրս գալ մեկ օղակից.:

`while :; do break; done`

- Դուրս գալ բնադրված օղակներից.:

`while :; do while :; do break 2; done; done`
