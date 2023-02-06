# beep

> A PC hangszórójának hangjelzéséhez szükséges segédprogram. További információ: <https://github.com/spkr-beep/beep>.

- Hangjelzés lejátszása:

`beep`

- Ismétlődő hangjelzés lejátszása:

`beep -r {{repetitions}}`

- Ismétlődő hangjelzés lejátszása megadott frekvenciával (Hz) és időtartammal (milliszekundum):

`beep -f {{frequency}} -l {{duration}}`

- Minden új frekvencia és időtartam különálló hangjelzésként történő lejátszása:

`beep -f {{frequency}} -l {{duration}} -n -f {{frequency}} -l {{duration}}`

- A C-dúr skála lejátszása:

`beep -f {{262}} -n -f {{294}} -n -f {{330}} -n -f {{349}} -n -f {{392}} -n -f {{440}} -n -f {{494}} -n -f {{523}}`
