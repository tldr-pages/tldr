# kaggle

> Official CLI for Kaggle implemented in Python 3.
> More information: <https://github.com/Kaggle/kaggle-api/blob/main/docs/README.md>.

- View current configuration values:

`kaggle config view`

- Download a specific file from a competition dataset:

`kaggle competitions download {{competition}} {{[-f|--file]}} {{filename}}`

- List competitions matching a search term:

`kaggle competitions list -s {{search_term}}`

- List files available for a specific competition:

`kaggle competitions files {{competition}}`

- Submit a file to a competition with a message:

`kaggle competitions submit {{competition}} -f {{submission.csv}} -m "{{message}}"`

- List datasets matching a search term:

`kaggle datasets list -s {{search_term}}`

- Download all files from a dataset:

`kaggle datasets download {{owner/dataset_name}}`

- List kernels (notebooks) matching a search term:

`kaggle kernels list -s {{search_term}}`
