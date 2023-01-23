# supervisorctl

> A Supervisor egy kliens/szerver rendszer, amely lehetővé teszi a felhasználóinak, hogy számos folyamatot irányítsanak UNIX-szerű operációs rendszereken. A Supervisorctl a supervisor parancssori kliens része, amely egy shell-szerű felületet biztosít. További információ [: http://supervisord.org](http://supervisord.org).

- Egy folyamat indítása/leállítása/újraindítása:

`supervisorctl {{start|stop|restart}} {{process_name}}`

- Egy csoport összes folyamatának indítása/leállítása/újraindítása:

`supervisorctl {{start|stop|restart}} {{group_name}}:*`

- A folyamat utolsó 100 **bájtjának** megjelenítése `stderr`:

`supervisorctl tail -100 {{process_name}} stderr`

- Egy folyamat `stdout` folyamatos megjelenítése:

`supervisorctl tail -f {{process_name}} stdout`

- A folyamat konfigurációs fájl újratöltése a folyamatok hozzáadásához/eltávolításához szükség szerint:

`supervisorctl update`
