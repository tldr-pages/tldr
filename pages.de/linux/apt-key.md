# apt-key

> Schlüssel-Management-Tool für den APT-Paket-Manager auf Debian und Ubuntu.
> Notiz: `apt-key` ist veraltet (außer für `apt-key del` in Maintainerskripten).
> Weitere Informationen: <https://manpages.debian.org/latest/apt/apt-key.8.html>.

- Liste alle vertrauten Schlüssel auf:

`apt-key list`

- Füge einen Schlüssel hinzu:

`apt-key add {{public_key_file.asc}}`

- Lösche einen Schlüssel:

`apt-key del {{key_id}}`

- Füge einen Remote-Schlüssel hinzu:

`wget -qO - {{https://host.tld/filename.key}} | apt-key add -`

- Füge einen Schlüssel von einem Schlüsselserver hinzu nur mit der Schlüssel-ID:

`apt-key adv --keyserver {{pgp.mit.edu}} --recv {{KEYID}}`
