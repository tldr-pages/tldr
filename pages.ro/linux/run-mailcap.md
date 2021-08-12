# run-mailcap

> Rulați programe MailCap.
> Rulați vizualizarea mailcap, vedeți, editați, compuneți, tipăriți - executați programe prin intrări în fișierul mailcap (sau oricare dintre aliasurile sale) va utiliza acțiunea dată pentru a procesa fiecare tip/fișier MIME.

- Acțiuni/programe individuale pe run-mailcap pot fi invocate cu semnalizatorul de acțiune:

`run-mailcap --action=ACTION [--option[=value]]`

- În limbaj simplu:

`run-mailcap --action=ACTION {{filename}}`

- Activați informații suplimentare:

`run-mailcap --action=ACTION --debug {{filename}}`

- Ignorați orice directivă „copiousoutput” și ieșire înainte la ieșire standard:

`run-mailcap --action=ACTION --nopager {{filename}}`

- Afișați comanda găsită fără a o executa efectiv:

`run-mailcap --action=ACTION --norun {{filename}}`
