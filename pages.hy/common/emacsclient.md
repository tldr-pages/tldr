# emacsclient

> Բացեք ֆայլերը գոյություն ունեցող Emacs սերվերում:.
> Տես նաև՝ `emacs`:.
> Լրացուցիչ տեղեկություններ. <https://www.gnu.org/software/emacs/manual/html_node/emacs/emacsclient-Options.html>:.

- Բացեք ֆայլ գոյություն ունեցող Emacs սերվերում (օգտագործելով GUI, եթե առկա է).:

`emacsclient {{path/to/file}}`

- Բացեք ֆայլը վահանակի ռեժիմում (առանց X պատուհանի).:

`emacsclient {{[-nw|--no-window-system]}} {{path/to/file}}`

- Բացեք ֆայլը նոր Emacs պատուհանում.:

`emacsclient {{[-c|--create-frame]}} {{path/to/file}}`

- Գնահատեք հրամանը՝ տպելով ելքը `stdout`-ով, այնուհետև դուրս եկեք՝:

`emacsclient {{[-e|--eval]}} '({{command}})'`

- Նշեք այլընտրանքային խմբագիր, եթե Emacs սերվերը չի աշխատում.:

`emacsclient {{[-a|--alternate-editor]}} {{editor}} {{path/to/file}}`

- Դադարեցրեք գործող Emacs սերվերը և դրա բոլոր օրինակները՝ խնդրելով հաստատել չպահված ֆայլերը.:

`emacsclient {{[-e|--eval]}} '(save-buffers-kill-emacs)'`
