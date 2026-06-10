# <>

> Բացեք ֆայլի նկարագրիչ՝ կարդալու և գրելու համար:.
> Լրացուցիչ տեղեկություններ. <https://www.gnu.org/software/bash/manual/bash.html#Opening-File-Descriptors-for-Reading-and-Writing>:.

- Բացեք ֆայլ ֆայլի նկարագրիչում կարդալու և գրելու համար.:

`exec {{3}}<>{{path/to/file}}`

- Բացեք ֆայլի նկարագրիչը հեռավոր կապի համար.:

`exec {{3}}<>/dev/{{tcp}}/{{remote_host}}/{{port_number}}`

- Փակեք ֆայլի նկարագրիչը.:

`exec {{3}}<>-`
