# kaggle competitions

> Manage Kaggle competitions from the command-line.
> More information: <https://github.com/Kaggle/kaggle-api/blob/main/docs/README.md#competitions>.

- List competitions filtered by group, category, and sort order:

`kaggle competitions list --group {{general}} --category {{featured}} --sort-by {{reward}}`

- Show the files available for a competition:

`kaggle competitions files -c {{competition_name}}`

- Download all files of a competition into a specific directory:

`kaggle competitions download -c {{competition_name}} -p {{path/to/directory}}`

- Submit a predictions file with a message:

`kaggle competitions submit -c {{competition_name}} -f {{path/to/submission.csv}} -m "{{submission_message}}"`

- Display your submission history for a competition:

`kaggle competitions submissions -c {{competition_name}}`

- View the competition leaderboard in the terminal:

`kaggle competitions leaderboard -c {{competition_name}} --show`
