# ng new

> Create and initialize a new Angular application.
> More information: <https://angular.dev/cli/new>.

- Create a new Angular application:

`ng new {{app_name}}`

- Preview the actions without creating files:

`ng new {{app_name}} {{[-d|--dry-run]}}`

- Skip generating unit test (`spec.ts`) files:

`ng new {{app_name}} {{[-S|--skip-tests]}}`

- Skip automatic package installation:

`ng new {{app_name}} --skip-install`

- Skip Git repository initialization:

`ng new {{app_name}} {{[-g|--skip-git]}}`

- Configure AI tooling for the project:

`ng new {{app_name}} --ai-config {{claude|copilot|cursor|gemini|jetbrains|none|windsurf}}`

- Disable interactive prompts:

`ng new {{app_name}} --interactive false`
