# packwiz

> Create, edit and manage Minecraft modpacks.
> More information: <https://packwiz.infra.link/reference/commands/packwiz/>.

- Interactively create a new modpack in the current directory:

`packwiz init`

- Add a mod from Modrinth or Curseforge:

`packwiz {{modrinth|curseforge}} add {{url|slug|search_term}}`

- List all mods in the modpack:

`packwiz list`

- Update `index.toml` after manually editing files:

`packwiz refresh`

- Export as a Modrinth (`.mrpack`) or Curseforge (`.zip`) file:

`packwiz {{modrinth|curseforge}} export`
