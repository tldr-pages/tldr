# nologin

> Alternative Shell, die verhindert, dass sich ein Benutzer einloggt.

- Die Login-Shell eines Benutzers auf `nologin` setzen, um zu verhindern, dass der Benutzer sich anmeldet:

`chsh -s {{user}} nologin`

- Nachricht für Benutzer mit Login-Shell `nologin` anpassen:

`echo "{{declined_login_message}}" > /etc/nologin.txt`
