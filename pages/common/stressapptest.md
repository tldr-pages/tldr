# stressapptest

> Userspace memory and IO test.
> More information: <https://github.com/stressapptest/stressapptest>.

- Test the given amount of memory (in Megabytes):

`stressapptest -M {{memory}}`

- Test memory as well as I/O for the given file:

`stressapptest -M {{memory}} -f {{path/to/file}}`

- Test specifying the verbosity level, where 0=lowest, 20=highest, 8=default:

`stressapptest -M {{memory}} -v {{level}}`
