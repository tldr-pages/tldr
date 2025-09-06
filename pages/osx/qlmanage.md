# qlmanage

> QuickLook server tool.
> More information: <https://keith.github.io/xcode-man-pages/qlmanage.1.html>.

- Display QuickLook for one or multiple files:

`qlmanage -p {{path/to/file1 path/to/file2 ...}}`

- Compute 300px wide PNG thumbnails of all JPEGs in the current directory and put them in a directory:

`qlmanage {{*.jpg}} -t -s {{300}} {{path/to/directory}}`

- Reset QuickLook:

`qlmanage -r`
