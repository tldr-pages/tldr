# nologin

> Alternative Shell, die verhindert, dass sich ein Benutzer einloggt.
> Weitere Informationen: <https://manned.org/nologin.8>.

- Setze die Login-Shell eines Benutzers auf `nologin`, um zu verhindern, dass der Benutzer sich anmeldet:

`chsh {{[-s|--shell]}} {{user}} nologin`

- Passe die Nachricht für Benutzer mit Login-Shell `nologin` an:

`echo "{{nachricht}}" > /etc/nologin.txt`
