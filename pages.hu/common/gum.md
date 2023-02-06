# gum

> Egy eszköz elbűvölő shell szkriptek készítéséhez. További információ: <https://github.com/charmbracelet/gum>.

- Interaktívan kiválaszthat egy adott opciót a `stdout` címre történő nyomtatáshoz:

`gum choose "{{option_1}}" "{{option_2}}" "{{option_3}}"`

- Interaktív prompt megnyitása a felhasználó számára, hogy egy adott helyőrzővel ellátott karakterláncot írjon be:

`gum input --placeholder "{{value}}"`

- Interaktív megerősítő prompt megnyitása és kilépés a `0` vagy a `1` címmel:

`gum confirm "{{Continue?}}" --default=false --affirmative "{{Yes}}" --negative "{{No}}" {{&& echo "Yes selected" || echo "No selected"}}`

- Egy pörgettyű megjelenítése egy parancs végrehajtása közben, mellette szöveggel:

`gum spin --spinner {{dot|line|minidot|jump|pulse|points|globe|moon|monkey|meter|hamburger}} --title "{{loading...}}" -- {{command}}`

- A szöveg formázása emojik beillesztésére:

`gum format -t {{emoji}} "{{:smile: :heart: hello}}"`

- Interaktívan kérhet többsoros szöveget (CTRL + D a mentéshez) és írhat a `data.txt` címre:

`gum write > {{data.txt}}`
