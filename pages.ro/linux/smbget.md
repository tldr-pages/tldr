# smbget

> `wget`-like utilitar pentru descărcarea fișierelor de pe serverele SMB.
> Mai multe informaţii: <https://www.samba.org/samba/docs/current/man-html/smbget.1.html>

- Descărcați un fișier de pe un server:

`smbget {{smb://server/share/file}}`

- Descărcați o partajare sau un director recursiv:

`smbget --recursive {{smb://server/share}}`

- Conectați-vă cu un nume de utilizator și o parolă:

`smbget {{smb://server/share/file}} --user {{username%password}}`

- Necesită transferuri criptate:

`smbget {{smb://server/share/file}} --encrypt`
