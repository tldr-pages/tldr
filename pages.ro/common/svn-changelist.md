# svn changelist

> Asociați un modificator cu un set de fișiere.
> Mai multe informaţii: <http://svnbook.red-bean.com/en/1.7/svn.advanced.changelists.html>

- Adăugați fișiere la un schimbător, creând schimbătorul dacă nu există:

`svn changelist {{changelist_name}} {{path/to/file1}} {{path/to/file2}}`

- Eliminați fișierele de la un schimbător:

`svn changelist --remove {{path/to/file1}} {{path/to/file2}}`

- Înlăturați întregul schimbător dintr-o dată:

`svn changelist --remove --recursive --changelist {{changelist_name}} .`

- Adăugați conținutul unei liste separate în spațiu de directoare la un schimbător:

`svn changelist --recursive {{changelist_name}} {{path/to/directory1}} {{path/to/directory2}}`

- Comite un schimbător:

`svn commit --changelist {{changelist_name}}`
