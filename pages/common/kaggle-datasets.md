# kaggle datasets

> Manage Kaggle datasets.
> More information: <https://github.com/Kaggle/kaggle-api/blob/main/docs/README.md#datasets>.

- List datasets that match a search term and sort by votes:

`kaggle datasets list -s {{search_term}} --sort-by {{votes}}`

- Show the files contained in a dataset:

`kaggle datasets files {{owner/dataset}}`

- Download an entire dataset into a directory and unzip it:

`kaggle datasets download {{owner/dataset}} -p {{path/to/directory}} --unzip`

- Initialize metadata for creating a new dataset in the current directory:

`kaggle datasets init`

- Create a new public dataset from a local folder:

`kaggle datasets create -p {{path/to/dataset_directory}} --public`

- Publish a new dataset version with a message:

`kaggle datasets version -p {{path/to/dataset_directory}} -m "{{update_message}}" --dir-mode {{zip}}`
