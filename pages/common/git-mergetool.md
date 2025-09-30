# git mergetool

> Run merge conflict resolution tools to resolve merge conflicts.
> More information: <https://git-scm.com/docs/git-mergetool>.

- Launch the default merge tool to resolve conflicts:

`git mergetool`

- List valid merge tools:

`git mergetool --tool-help`

- Launch the merge tool identified by a name:

`git mergetool {{[-t|--tool]}} {{tool_name}}`

- Don't prompt before each invocation of the merge tool:

`git mergetool {{[-y|--no-prompt]}}`

- Explicitly use the GUI merge tool (see the `merge.guitool` configuration variable):

`git mergetool {{[-g|--gui]}}`

- Explicitly use the regular merge tool (see the `merge.tool` configuration variable):

`git mergetool --no-gui`
