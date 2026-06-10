# sc_tracediff

> Ցուցադրել հետագծային ուղիները, որտեղ ուղին փոխվել է:.
> Լրացուցիչ տեղեկություններ. <https://www.caida.org/catalog/software/scamper/>:.

- Ցույց տալ հետագծերի տարբերությունը երկու `.warts` ֆայլերում.:

`sc_tracediff {{path/to/file1.warts}} {{path/to/file2.warts}}`

- Ցույց տալ հետագծերի միջև տարբերությունը երկու `.warts` ֆայլերում, ներառյալ նրանք, որոնք չեն փոխվել.:

`sc_tracediff -a {{path/to/file1.warts}} {{path/to/file2.warts}}`

- Ցույց տվեք հետագծերի միջև տարբերությունը երկու `.warts` ֆայլերում և փորձեք ցուցադրել DNS անունները և ոչ թե IP հասցեները, եթե հնարավոր է.:

`sc_tracediff -n {{path/to/file1.warts}} {{path/to/file2.warts}}`
