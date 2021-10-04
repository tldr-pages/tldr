# puppet agent

> Ruft die Client-Konfiguration vom Puppetserver ab und setzt diese auf dem System um.
> Weitere Informationen: <https://puppet.com/docs/puppet/7/man/agent.html>.

- Registriere die Node beim Puppetserver und setze den empfangenen Katalog um:

`puppet agent --test --server {{puppetserver_fqdn}} --serverport {{port}} --waitforcert {{poll_zeit}}`

- Führe den Agenten im Hintergrund aus (nutzt die Einstellungen von `/opt/puppetlabs/puppet/puppet.conf`):

`puppet agent`

- Führe den Agenten einmal im Vordergrund aus und beende:

`puppet agent --test`

- Führe den Agenten im Dry-Modus aus:

`puppet agent --test --noop`

- Protokolliere jede ausgewertete Ressource (selbst wenn sich nichts geändert hat):

`puppet agent --test --evaltrace`
