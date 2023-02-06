# dvc gc

> A nem használt fájlok és könyvtárak eltávolítása a gyorsítótárból vagy a távoli tárolóból. További információ: <https://dvc.org/doc/command-reference/gc>.

- Szemétgyűjtés a gyorsítótárból, csak az aktuális munkaterület által hivatkozott verziók megtartásával:

`dvc gc --workspace`

- Szemétgyűjtés a gyorsítótárból, csak az ágak, címkék és commitok által hivatkozott verziók megtartása:

`dvc gc --all-branches --all-tags --all-commits`

- Szemétgyűjtés a gyorsítótárból, beleértve az alapértelmezett felhőalapú távoli tárolót (ha be van állítva):

`dvc gc --all-commits --cloud`

- Szemétgyűjtés a gyorsítótárból, beleértve egy adott felhő távoli tárolót:

`dvc gc --all-commits --cloud --remote {{remote_name}}`
