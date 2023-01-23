# puppet agent

> Az ügyfélkonfiguráció lekérése a Puppet-kiszolgálóról és alkalmazása a helyi állomáson. További információ: <https://puppet.com/docs/puppet/7/man/agent.html>.

- Regisztrál egy csomópontot egy Puppet-kiszolgálón, és alkalmazza a kapott katalógust:

`puppet agent --test --server {{puppetserver_fqdn}} --serverport {{port}} --waitforcert {{poll_time}}`

- Az ügynök futtatása a háttérben (a `puppet.conf` oldalon található beállításokat használja):

`puppet agent`

- Az ügynök egyszeri futtatása előtérben, majd kilépés:

`puppet agent --test`

- Az ügynök futtatása száraz üzemmódban:

`puppet agent --test --noop`

- Minden kiértékelt erőforrás naplózása (még akkor is, ha semmi sem változik):

`puppet agent --test --evaltrace`

- Az ügynök letiltása:

`puppet agent --disable "{{message}}"`

- Az ügynök engedélyezése:

`puppet agent --enable`
