# pacman

> ആർച്ച് ലിന്ക്സിന്റെ പാക്കേജ് മാനേജുമെന്റ് യൂട്ടിലിറ്റി.
> ഇതും കാണുക: `pacman-database`, `pacman-deptest`, `pacman-files`, `pacman-key`, `pacman-mirrors`, `pacman-query`, `pacman-remove`, `pacman-sync`, `pacman-upgrade`.
> കൂടുതൽ വിവരങ്ങൾ: <https://man.archlinux.org/man/pacman.8>.

- ഇൻസ്റ്റാൾ ചെയ്‌ത എല്ലാ പാക്കേജും അപ്‌ഡേറ്റു ചെയ്യുക:

`sudo pacman -Syu`

- പുതിയ പാക്കേജ് ഇൻസ്റ്റാൾ ചെയ്യുക:

`sudo pacman -S {{പാക്കേജ്}}`

- ഒരു പാക്കേജും അത് ആശ്രയിക്കുന്ന മറ്റ് പാക്കേജുകളെയും കളയുക:

`sudo pacman -Rs {{പാക്കേജ്}}`

- ഇൻസ്റ്റാൾ ചെയ്‌ത എല്ലാ പാക്കേജുകളും അതിന്റെ പതിപ്പും കാണിക്കുക:

`pacman -Q`

- നേരെ ഇൻസ്റ്റാൾ ചെയ്ത പാക്കേജ്‌സ് മാത്റം കാണിക്കുക:

`pacman -Qe`

- പാക്കേജ് ക്യാഷ് കാലിയാക്കി സ്റ്റോറേജ്‌ മുക്തമാക്കുക:

`sudo pacman -Scc`
