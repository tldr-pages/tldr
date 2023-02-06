# sips

> Apple Scriptable Image Processing System. Raster/Query képek és ColorSync ICC profilok. További információ: <https://ss64.com/osx/sips.html>.

- Adjon meg egy kimeneti könyvtárat, hogy az eredetiek ne módosuljanak:

`sips --out {{path/to/out_dir}}`

- A kép újramintázása megadott méretben, A kép kép képaránya megváltozhat:

`sips --resampleHeightWidth {{1920}} {{300}} {{image.ext}}`

- A kép újramintazása úgy, hogy a magasság és szélesség ne legyen nagyobb a megadott méretnél (vegye figyelembe a nagy Z betűt):

`sips --resampleHeightWidthMax {{1920}} {{300}} {{image.ext}}`

- A könyvtárban lévő összes kép újramintazása, hogy 960px szélességű legyen (a képarány tiszteletben tartásával):

`sips --resampleWidth {{960}} {{path/to/images}}`

- Egy kép átalakítása CMYK-ból RGB-be:

`sips --matchTo "/System/Library/ColorSync/Profiles/Generic RGB Profile.icc" {{path/to/image.ext}} {{path/to/out_dir}}`

- ColorSync ICC-profil eltávolítása egy képről:

`sips --deleteProperty profile --deleteColorManagementProperties {{path/to/image.ext}}`
