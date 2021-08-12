# makensis

> Compilator cross-platform pentru instalatori NSIS.
> Acesta compilează un script NSIS într-un executabil de instalare Windows.
> Mai multe informaţii: <https://nsis.sourceforge.io/Docs/Chapter3.html>

- Compilarea unui script NSIS:

`makensis {{path/to/file.nsi}}`

- Compilați un script NSIS în mod strict (tratați avertismentele ca erori):

`makensis -WX {{path/to/file.nsi}}`

- Print ajutor pentru o anumită comandă:

`makensis -CMDHELP {{command}}`
