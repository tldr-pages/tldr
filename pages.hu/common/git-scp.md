# git scp

> Fájlok másolása az aktuális munkafából egy távoli tároló munkakönyvtárába. A `git-extras` része. Fájlok átvitelére a `rsync` -t használja. További információ: <https://github.com/tj/git-extras/blob/master/Commands.md#git-scp>.

- Előkészítetlen fájlok másolása egy adott távoli helyre:

`git scp {{remote_name}}`

- Elkészült és el nem készített fájlok másolása egy távoli tárolóba:

`git scp {{remote_name}} HEAD`

- A legutóbbi commitban módosított fájlok, valamint a staged és unstaged fájlok másolása egy távoli helyre:

`git scp {{remote_name}} HEAD~1`

- Konkrét fájlok másolása távoli helyre:

`git scp {{remote_name}} {{path/to/file1 path/to/file2 ...}}`

- Egy adott könyvtár másolása egy távoli helyre:

`git scp {{remote_name}} {{path/to/directory}}`
