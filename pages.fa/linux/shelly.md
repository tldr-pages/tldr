# shelly

> مدیر بستهٔ مدرن و یکپارچه برای Arch Linux.
> همچنین : `pacman`, `paru`, `yay`.
> اطلاعات بیشتر: <https://www.seafoam-labs.org/shelly-alpm/docs/cli-reference/>.

- ارتقای همهٔ بسته‌ها از همهٔ منابع (مخزن، AUR، Flatpak، AppImage):

`shelly {{[-Ux|upgrade all]}}`

- نصب بسته:

`shelly {{package}}`

- حذف بستهٔ نصب‌شده و وابستگی‌های یتیم آن:

`shelly {{[-Rs|remove standard]}} {{[-c|--cascade]}} {{package}}`

- جست‌وجوی بسته در مخازن استاندارد:

`shelly {{[-Ss|search standard]}} {{[-v|--available]}} {{search_term}}`

- جست‌وجوی بسته فقط در AUR:

`shelly {{[-Sa|search aur]}} {{search_term}}`

- حذف بسته‌های یتیم (نصب‌شده به‌عنوان وابستگی اما دیگر مورد نیاز نیستند):

`shelly {{[-Zs|purify standard]}} {{[-o|--orphans]}}`
