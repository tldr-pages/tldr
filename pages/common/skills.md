# skills

> Manage reusable agent skills across AI coding agents.
> More information: <https://github.com/vercel-labs/skills>.

- Search for skills interactively or by keyword:

`skills {{[f|find]}} {{keyword}}`

- List all installed skills:

`skills {{[ls|list]}}`

- Install all skills from a repository:

`skills {{[a|add]}} {{owner}}/{{repo}}`

- Install specific skills to particular agents:

`skills {{[a|add]}} {{owner}}/{{repo}} {{[-s|--skill]}} {{skill_name}} {{[-a|--agent]}} {{agent_name}}`

- Remove installed skills:

`skills {{[rm|remove]}} {{skill_name}}`

- Update all installed skills:

`skills update`

- Create a new `SKILL.md` template:

`skills init {{[skill_name]}}`
