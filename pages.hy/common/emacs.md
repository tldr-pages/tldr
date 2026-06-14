# emacs

> Ընդարձակելի, կարգավորելի, ինքնուրույն փաստաթղթավորվող, իրական ժամանակի ցուցադրման խմբագիր:.
> Տես նաև՝ `emacsclient`:.
> Լրացուցիչ տեղեկություններ. <https://www.gnu.org/software/emacs>:.

- Սկսեք Emacs-ը և բացեք ֆայլ.:

`emacs {{path/to/file}}`

- Բացեք ֆայլ նշված տողի համարով.:

`emacs +{{line_number}} {{path/to/file}}`

- Գործարկեք Emacs Lisp ֆայլը որպես սցենար.:

`emacs --script {{path/to/file.el}}`

- Սկսեք Emacs-ը վահանակի ռեժիմում (առանց X պատուհանի).:

`emacs {{[-nw|--no-window-system]}}`

- Սկսեք Emacs սերվերը հետին պլանում (հասանելի է `emacsclient`-ի միջոցով):

`emacs --daemon`

- Դադարեցրեք գործող Emacs սերվերը և դրա բոլոր օրինակները՝ խնդրելով հաստատել չպահված ֆայլերը.:

`emacsclient --eval '(save-buffers-kill-emacs)'`

- Պահպանեք ֆայլ Emacs-ում.:

`<Ctrl x><Ctrl s>`

- Դուրս գալ Emacs-ից.:

`<Ctrl x><Ctrl c>`
