# կռունկ արտահանում

> Արտահանել կոնտեյների պատկերի ֆայլային համակարգը որպես tarball:.
> Լրացուցիչ տեղեկություններ. <https://github.com/google/go-containerregistry/blob/main/cmd/crane/doc/crane_export.md>:.

- Գրեք tarball `stdout` հասցեին՝:

`crane export {{image_name}} -`

- Գրեք tarball ֆայլում.:

`crane export {{image_name}} {{path/to/tarball}}`

- Կարդացեք պատկերը `stdin`-ից:

`crane export - {{path/to/file}}`
