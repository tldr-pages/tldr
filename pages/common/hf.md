# hf

> Interact with Hugging Face Hub.
> Login, manage local cache, download, or upload files.
> More information: <https://huggingface.co/docs/huggingface_hub/guides/cli>.

- Login to Hugging Face Hub:

`hf login`

- Display the name of the logged in user:

`hf whoami`

- Log out:

`hf logout`

- Print information about the environment:

`hf env`

- Download files from a repository and print out the path (omit filenames to download entire repository):

`hf download --repo-type {{repo_type}} {{repo_id}} {{filename1 filename2 ...}}`

- Upload an entire folder or a file to Hugging Face:

`hf upload --repo-type {{repo_type}} {{repo_id}} {{path/to/local_file_or_directory}} {{path/to/repo_file_or_directory}}`

- Scan cache to see downloaded repositories and their disk usage:

`hf scan-cache`

- Delete the cache interactively:

`hf delete-cache`
