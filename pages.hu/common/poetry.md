# poetry

> Python csomagok és függőségek kezelése. További információ: <https://python-poetry.org/docs/cli/>.

- Hozzon létre egy új Poetry projektet a könyvtárban egy adott névvel:

`poetry new {{project_name}}`

- Telepítsen egy függőséget és annak alfüggőségeit:

`poetry add {{dependency}}`

- Telepítsen egy fejlesztési függőséget és annak alfüggőségeit:

`poetry add --group dev {{dependency}}`

- Interaktívan inicializálja az aktuális könyvtárat új Poetry projektként:

`poetry init`

- Az összes függőség legújabb verziójának lekérdezése és frissítése: `poetry.lock`:

`poetry update`

- Parancs végrehajtása a projekt virtuális környezetében:

`poetry run {{command}}`

- A projekt minor verziójának felemelése a `pyproject.toml`:

`poetry version minor`
