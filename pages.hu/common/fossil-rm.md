# fossil rm

> Fájlok vagy könyvtárak eltávolítása a Fossil verziókezelőből. Lásd még: `fossil forget`. További információ: <https://fossil-scm.org/home/help/rm>.

- Fájl vagy könyvtár eltávolítása a Fossil verziókezelőből:

`fossil rm {{path/to/file_or_directory}}`

- Egy fájl vagy könyvtár eltávolítása a Fossil verziókezelőből, és egyben törlése a lemezről:

`fossil rm --hard {{path/to/file_or_directory}}`

- Az összes korábban eltávolított és még nem véglegesített fájl újbóli hozzáadása a Fossil verziókezelőhöz:

`fossil rm --reset`
