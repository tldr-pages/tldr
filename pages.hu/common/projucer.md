# Projucer

> A JUCE keretrendszer alkalmazásainak projektmenedzsere. További információ: <https://juce.com/discover/stories/projucer-manual#10.4-command-line-tools>.

- Egy projektre vonatkozó információk megjelenítése:

`Projucer --status {{path/to/project_file}}`

- A projektben lévő összes fájl és erőforrás újramentése:

`Projucer --resave {{path/to/project_file}}`

- A verziószám frissítése egy projektben:

`Projucer --set-version {{version_number}} {{path/to/project_file}}`

- JUCE-projekt generálása PIP-fájlból:

`Projucer --create-project-from-pip {{path/to/PIP}} {{path/to/output}}`

- Az összes JUCE-stílusú megjegyzés eltávolítása (`//=====`, `//-----` vagy `///////`):

`Projucer --tidy-divider-comments {{path/to/target_folder}}`

- Súgó megjelenítése:

`Projucer --help`
