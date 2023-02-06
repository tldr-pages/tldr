# git-imerge

> Két Git ág között inkrementálisan végezhet összeolvasztást vagy újraalapozást. Az ágak közötti konfliktusok a konfliktuskezelés egyszerűsítése érdekében az egyes commitok párjaiig követhetők. További információ: <https://github.com/mhagger/git-imerge>.

- Indítsa el az imerge-alapú újraalapozást (először ellenőrizze az újraalapozandó ágat):

`git imerge rebase {{branch_to_rebase_onto}}`

- Imerge-alapú egyesítés indítása (először az egyesítendő ágat kell ellenőrizni):

`git imerge merge {{branch_to_be_merged}}`

- A folyamatban lévő egyesítés vagy újraalapozás ASCII-diagramjának megjelenítése:

`git imerge diagram`

- Folytassa az imerge műveletet a konfliktusok feloldása után (`git add` az ütköző fájlokat először):

`git imerge continue --no-edit`

- Az imerge művelet befejezése, miután minden konfliktus megoldódott:

`git imerge finish`

- Az imerge művelet megszakítása, és visszatérés az előző ághoz:

`git-imerge remove && git checkout {{previous_branch}}`
