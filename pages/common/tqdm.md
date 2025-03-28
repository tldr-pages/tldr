# tqdm

> Show progress over time of a command.
> More information: <https://tqdm.github.io/>.

- Show iterations per second and use `stdout` afterwards:

`{{seq 10000000}} | tqdm | {{command}}`

- Create a progress bar:

`{{seq 10000000}} | tqdm --total 10000000 | {{command}}`

- Create an archive out of a directory and use the file count of that directory to create a progress bar:

`zip -r {{backup.zip}} {{dir}} | tqdm --total $(find {{dir}} | wc -l) --unit files --null`
