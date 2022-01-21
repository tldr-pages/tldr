# qlmanage

> QuickLook server tool.
> More information: <https://ss64.com/osx/qlmanage.html>.

- Display QuickLook for one or multiple files:

`qlmanage -p {{filename}} {{filename2}}`

- Compute 300px wide PNG thumbnails of all JPEGs in the current directory and put them in a directory:

`qlmanage {{*.jpg}} -t -s {{300}} {{path/to/directory}}`

- Reset QuickLook:

`qlmanage -r`
