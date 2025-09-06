# stl2gts

> Convert STL files into the GTS (GNU triangulated surface library) file format.
> More information: <https://manned.org/stl2gts>.

- Convert an STL file to a GTS file:

`stl2gts < {{path/to/file.stl}} > {{path/to/file.gts}}`

- Convert an STL file to a GTS file and revert face normals:

`stl2gts --revert < {{path/to/file.stl}} > {{path/to/file.gts}}`

- Convert an STL file to a GTS file and do not merge vertices:

`stl2gts --nomerge < {{path/to/file.stl}} > {{path/to/file.gts}}`

- Convert an STL file to a GTS file and display surface statistics:

`stl2gts --verbose < {{path/to/file.stl}} > {{path/to/file.gts}}`

- Display help:

`stl2gts --help`
