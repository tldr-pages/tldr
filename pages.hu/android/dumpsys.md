# dumpsys

> Az Android rendszer szolgáltatásairól szóló információk szolgáltatása. Ez a parancs csak a `adb shell` oldalon keresztül használható. További információ: <https://developer.android.com/studio/command-line/dumpsys>.

- Diagnosztikai kimenetek lekérése az összes rendszerszolgáltatáshoz:

`dumpsys`

- Diagnosztikai kimenet lekérése egy adott rendszerszolgáltatáshoz:

`dumpsys {{service}}`

- Az összes szolgáltatás felsorolása: A `dumpsys` tud információt adni:

`dumpsys -l`

- Szolgáltatásspecifikus argumentumok listázása egy szolgáltatáshoz:

`dumpsys {{service}} -h`

- Egy adott szolgáltatás kizárása a diagnosztikai kimenetből:

`dumpsys --skip {{service}}`

- Időkorlátozási időszak megadása másodpercben (alapértelmezett érték 10s):

`dumpsys -t {{seconds}}`
