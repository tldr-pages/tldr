# fisher

> Fisher, egy fish-shell plugin menedzser. Telepítse a pluginokat név szerint vagy egy menedzselt 'fishfile' fájlból a csomagban történő telepítéshez. További információ: <https://github.com/jorgebucaran/fisher>.

- Telepítsen egy vagy több bővítményt:

`fisher {{plugin1}} {{plugin2}}`

- Telepítsen egy plugint egy GitHub gistből:

`fisher {{gist_url}}`

- A 'fishfile' kézi szerkesztése a kedvenc szerkesztőjével, és több plugin telepítése:

`{{editor}} ~/.config/fish/fishfile; fisher`

- Telepített bővítmények listázása:

`fisher ls`

- Pluginok frissítése:

`fisher update`

- Egy vagy több bővítmény eltávolítása:

`fisher remove {{plugin1}} {{plugin2}}`
