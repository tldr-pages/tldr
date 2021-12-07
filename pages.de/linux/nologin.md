# nologin

> Alternative Shell, die verhindert, dass sich ein Benutzer einloggt.

- Setze die Login-Shell eines Benutzers auf `nologin`, um zu verhindern, dass der Benutzer sich anmeldet:

`chsh -s {{user}} nologin`

- Passe die Nachricht für Benutzer mit Login-Shell `nologin` an:

`echo "{{nachricht}}" > /etc/nologin.txt`
