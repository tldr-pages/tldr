# cradle install

> Instalează componentele cadru Cradle PHP.
> Mai multe informaţii: <https://cradlephp.github.io/docs/3.B.-Reference-Command-Line-Tools.html#install>

- Instalați componentele Cradle (Utilizatorul va fi solicitat pentru detalii suplimentare):

`cradle install`

- Suprascrie forțat fișierele:

`cradle install --force`

- Treci peste rularea migrărilor SQL:

`cradle install --skip-sql`

- Treci peste rularea pachetelor actualizări:

`cradle install --skip-versioning`

- Utilizează detaliile specifice ale bazei de date:

`cradle install -h {{hostname}} -u {{username}} -p {{password}}`
