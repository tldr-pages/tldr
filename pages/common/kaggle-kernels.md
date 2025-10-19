# kaggle kernels

> Work with Kaggle kernels (notebooks and scripts).
> More information: <https://github.com/Kaggle/kaggle-api/blob/main/docs/README.md#kernels>.

- List kernels matching a search term and written in Python:

`kaggle kernels list -s {{search_term}} --language {{python}}`

- Download the source for a kernel into a directory:

`kaggle kernels get {{owner/kernel_name}} -p {{path/to/directory}}`

- Initialize kernel metadata in the current directory:

`kaggle kernels init`

- Update a kernel with the code in a folder and run it:

`kaggle kernels update -p {{path/to/kernel_directory}}`

- Download the latest output files from a kernel run:

`kaggle kernels output {{owner/kernel_name}} -p {{path/to/directory}}`

- Check the execution status of the latest kernel run:

`kaggle kernels status {{owner/kernel_name}}`
