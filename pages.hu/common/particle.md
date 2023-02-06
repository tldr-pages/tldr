# particle

> Parancssori eszköz a Particle eszközökkel való interakcióhoz. További információ: <https://docs.particle.io/tutorials/developer-tools/cli>.

- Jelentkezzen be vagy hozzon létre fiókot a Particle CLI-hez:

`particle setup`

- Az eszközök listájának megjelenítése:

`particle list`

- Új Particle projekt létrehozása interaktív módon:

`particle project create`

- Particle projekt fordítása:

`particle compile {{device_type}} {{path/to/source_code.ino}}`

- Egy eszköz frissítése egy adott alkalmazás távoli használatára:

`particle flash {{device_name}} {{path/to/program.bin}}`

- Egy eszköz frissítése a legújabb firmware használatára soros kapcsolaton keresztül:

`particle flash --serial {{path/to/firmware.bin}}`

- Funkció végrehajtása egy eszközön:

`particle call {{device_name}} {{function_name}} {{function_arguments}}`
