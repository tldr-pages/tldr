# ar

> Create, modify, and extract from archives (`.a`, `.so`, `.o`).
> More information: <https://manned.org/ar>.

- E[x]tract all members from an archive:

`ar x {{path/to/file.a}}`

- Lis[t] contents in a specific archive:

`ar t {{path/to/file.a}}`

- [r]eplace or add specific files to an archive:

`ar r {{path/to/file.a}} {{path/to/file1.ext path/to/file2.ext ...}}`

- In[s]ert an object file index (equivalent to using `ranlib`):

`ar s {{path/to/file.a}}`

- Create an archive with specific files and an accompanying object file index:

`ar rs {{path/to/file.a}} {{path/to/file1.ext path/to/file2.ext ...}}`
