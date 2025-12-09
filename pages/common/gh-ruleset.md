# gh ruleset

> Manage GitHub repository rulesets.
> More information: <https://cli.github.com/manual/gh_ruleset>.

- List all rulesets for the current repository:

`gh {{[rs|ruleset]}} {{[ls|list]}}`

- List all rulesets for a specific organization:

`gh {{[rs|ruleset]}} {{[ls|list]}} {{[-o|--org]}} {{organization_name}}`

- Check the rules that apply to the current branch:

`gh {{[rs|ruleset]}} check`

- Check the rules that apply to a specific branch in another repository:

`gh {{[rs|ruleset]}} check {{branch_name}} {{[-R|--repo]}} {{owner}}/{{repo}}`

- Interactively select and view a ruleset for the current repository:

`gh {{[rs|ruleset]}} view`

- View a specific ruleset by its ID:

`gh {{[rs|ruleset]}} view {{ruleset_id}}`

- View an organization-level ruleset by its ID:

`gh {{[rs|ruleset]}} view {{ruleset_id}} {{[-o|--org]}} {{organization_name}}`

- Open the list of rulesets for a specific repository in the browser:

`gh {{[rs|ruleset]}} {{[ls|list]}} {{[-R|--repo]}} {{owner}}/{{repo}} {{[-w|--web]}}`
