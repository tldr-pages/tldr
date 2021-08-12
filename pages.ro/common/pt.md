# pt

> Căutător de platină.
> Un instrument de căutare cod similar cu `ag`.
> Mai multe informaţii: <https://github.com/monochromegane/the_platinum_searcher>

- Găsiți fișiere care conțin „foo” și imprimați fișierele cu potriviri evidențiate:

`pt {{foo}}`

- Găsiți fișiere care conțin „foo” și numărul de afișare a meciurilor în fiecare fișier:

`pt -c {{foo}}`

- Găsiți fișiere care conțin „foo” ca un cuvânt întreg și ignorați cazul său:

`pt -wi {{foo}}`

- Găsiți „foo” în fișiere cu o extensie dată utilizând o expresie regulată:

`pt -G='{{\.bar$}}' {{foo}}`

- Găsiți fișiere al căror conținut se potrivește cu expresia obișnuită, până la 2 directoare adânci:

`pt --depth={{2}} -e '{{^ba[rz]*$}}'`
