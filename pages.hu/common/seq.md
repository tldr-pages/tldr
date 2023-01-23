# seq

> Egy számsorozat kimenete a `stdout` címre. További információ: <https://www.gnu.org/software/coreutils/seq>.

- Sorozat 1-től 10-ig:

`seq 10`

- Minden 3. szám 5-től 20-ig:

`seq 5 3 20`

- A kimenetet újsor helyett szóközzel válassza el:

`seq -s " " 5 3 20`

- Formázza a kimenet szélességét legalább 4 számjegyre, szükség szerint nullákkal kitöltve:

`seq -f "%04g" 5 3 20`
