# kaggle models

> Manage Kaggle models and their instances.
> More information: <https://github.com/Kaggle/kaggle-api/blob/main/docs/README.md#models>.

- List models filtered by a search term and sort by download count:

`kaggle models list -s {{search_term}} --sort-by {{downloadCount}}`

- Download a model's metadata into a directory:

`kaggle models get {{owner/model_name}} -p {{path/to/directory}}`

- Initialize model metadata in the current directory:

`kaggle models init`

- Create a new model using the prepared metadata:

`kaggle models create -p {{path/to/model_directory}}`

- Update an existing model with edited metadata:

`kaggle models update -p {{path/to/model_directory}}`

- Delete a model by its owner and slug:

`kaggle models delete {{owner/model_name}}`
