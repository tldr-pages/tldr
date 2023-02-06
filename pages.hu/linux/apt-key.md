# apt-key

> Kulcskezelő segédprogram az APT csomagkezelőhöz Debian és Ubuntu alatt. Megjegyzés: a `apt-key` már elavult (kivéve a `apt-key del` használatát a karbantartó szkriptekben). További információ: <https://manpages.debian.org/latest/apt/apt-key.8.html>.

- Megbízható kulcsok listája:

`apt-key list`

- Kulcs hozzáadása a megbízható kulcstárhoz:

`apt-key add {{public_key_file.asc}}`

- Kulcs törlése a megbízható kulcstárból:

`apt-key del {{key_id}}`

- Távoli kulcs hozzáadása a megbízható kulcstárhoz:

`wget -qO - {{https://host.tld/filename.key}} | apt-key add -`

- Kulcs hozzáadása a kulcskiszolgálóról csak a kulcs azonosítójával:

`apt-key adv --keyserver {{pgp.mit.edu}} --recv {{KEYID}}`
