# go clean

> Objektumfájlok és gyorsítótárazott fájlok eltávolítása. További információ: <https://golang.org/cmd/go/#hdr-Remove_object_files_and_cached_files>.

- Az eltávolítási parancsok kinyomtatása ahelyett, hogy ténylegesen eltávolítana bármit is:

`go clean -n`

- Törölje a build cache-t:

`go clean -cache`

- Törölje az összes gyorsítótárazott teszteredményt:

`go clean -testcache`

- A modul gyorsítótár törlése:

`go clean -modcache`
