# tqdm

> Show progress over time of a command.
> More information: <https://tqdm.github.io/>.

- Show iterations per second and use `stdout` afterwards:

`{{seq 10000000}} | tqdm | {{command}}`

- Create a progress bar:

`{{seq 10000000}} | tqdm --total 10000000 | {{command}}`

- Specify unit and total:

`tar -zcf - {{docs/}} | tqdm --bytes --total $(du -sb {{docs/}} | cut -f1) > {{backup.tgz}}`
