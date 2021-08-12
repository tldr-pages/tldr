# spectre-meltdown-checker

> Instrument de detectare a atenuării Spectre și Meltdown.
> Mai multe informaţii: <https://manned.org/spectre-meltdown-checker.1>

- Verificați kernel-ul care rulează în prezent pentru Spectre sau Meltdown:

`sudo spectre-meltdown-checker`

- Verificați kernel-ul care rulează în prezent și afișați o explicație a acțiunilor de întreprins pentru a atenua o vulnerabilitate:

`sudo spectre-meltdown-checker --explain`

- Verificați pentru variante specifice (valori implicite pentru toate):

`sudo spectre-meltdown-checker --variant {{1|2|3|3a|4|l1tf|msbds|mfbds|mlpds|mdsum|taa|mcespc|srbds}}`

- Afișează ieșirea utilizând un format specific de ieșire:

`sudo spectre-meltdown-checker --batch {{text|json|nrpe|prometheus|short}}`

- Nu folosiţi interfaţa `/sys` chiar dacă este prezentă:

`sudo spectre-meltdown-checker --no-sysfs`

- Verificați un nucleu care nu rulează:

`sudo spectre-meltdown-checker --kernel {{path/to/kernel_file}}`
