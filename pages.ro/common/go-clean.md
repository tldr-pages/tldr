# go clean

> Eliminați fișierele obiect și fișierele memorate în cache.
> Mai multe informaţii: <https://golang.org/cmd/go/#hdr-Remove_object_files_and_cached_files>

- Imprimați comenzile de eliminare în loc de a elimina de fapt nimic:

`go clean -n`

- Ștergeți memoria cache de compilare:

`go clean -cache`

- Ștergeți toate rezultatele testelor memorate în cache:

`go clean -testcache`

- Ștergeți memoria cache a modulului:

`go clean -modcache`
