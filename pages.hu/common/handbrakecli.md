# handbrakecli

> A HandBrake videókonvertáló és DVD-rippelő eszköz parancssori interfésze. További információ: <https://handbrake.fr/>.

- Videofájl átalakítása MKV-vé (AAC 160kbit hang és x264 CRF20 videó):

`handbrakecli --input {{input.avi}} --output {{output.mkv}} --encoder x264 --quality 20 --ab 160`

- Videofájl átméretezése 320x240-re:

`handbrakecli --input {{input.mp4}} --output {{output.mp4}} --width 320 --height 240`

- A rendelkezésre álló előbeállítások listája:

`handbrakecli --preset-list`

- AVI videó átalakítása MP4-be az Android előbeállítás használatával:

`handbrakecli --preset="Android" --input {{input.ext}} --output {{output.mp4}}`

- Egy DVD tartalmának kinyomtatása, a CSS-kulcsok megszerzése közben:

`handbrakecli --input {{/dev/sr0}} --title 0`

- Egy DVD első sávjának másolása a megadott eszközön. A hangsávok és a feliratozási nyelvek listaként vannak megadva:

`handbrakecli --input {{/dev/sr0}} --title 1 --output {{out.mkv}} --format av_mkv --encoder x264 --subtitle {{1,4,5}} --audio {{1,2}} --aencoder copy --quality {{23}}`
