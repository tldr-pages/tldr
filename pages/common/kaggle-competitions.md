# kaggle competitions

> Manage Kaggle competitions from the command-line.
> More information: <https://github.com/Kaggle/kaggle-api/blob/main/docs/README.md#competitions>.

- List all competitions:

`kaggle competitions list`

- Download Competition Data:

`kaggle competitions download -c {{competition_name}}`

- Download specific file:

`kaggle competitions download -c {{competition_name}} -f {{file}}`

- Submit files to a competition:

`kaggle competitions submit -c {{competition-name}} -f {{file-path}} -m "{{message}}"`

- Show or Download leaderboard:

`kaggle competitions leaderboard {{competition-name}} {{--show|--download}}`

- View Submissions:

`kaggle competitions submissions -c {{competition_name}}`
