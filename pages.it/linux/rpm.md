# rpm

> RPM Package Manager.
> Per comandi equivalenti in altri gestori di pacchetti, vedi <https://wiki.archlinux.org/title/Pacman/Rosetta>.
> Maggiori informazioni: <https://rpm-software-management.github.io/rpm/man/rpm.8>.

- Mostra la versione del pacchetto httpd:

`rpm {{[-q|--query]}} httpd`

- Elenca le versioni di tutti i pacchetti corrispondenti:

`rpm {{[-qa|--query --all]}} '{{mariadb*}}'`

- Installa forzatamente un pacchetto indipendentemente dalle versioni attualmente installate:

`rpm {{[-U|--upgrade]}} {{path/to/package.rpm}} --force`

- Identifica il proprietario di un file e mostra la versione del pacchetto:

`rpm {{[-qf|--query --file]}} {{/etc/postfix/main.cf}}`

- Elenca i file posseduti da un pacchetto:

`rpm {{[-ql|--query --list]}} {{kernel}}`

- Mostra gli scriptlet da un file RPM:

`rpm {{[-qp|--query --package]}} --scripts {{package.rpm}}`

- Mostra file modificati, mancanti e/o installati in modo errato dei pacchetti corrispondenti:

`rpm {{[-Va|--verify --all]}} '{{php-*}}'`

- Mostra il changelog di un pacchetto specifico:

`rpm {{[-q|--query]}} --changelog {{package}}`
