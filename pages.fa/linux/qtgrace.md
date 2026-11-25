# qtgrace

> نمایش، رسم و تحلیل داده‌های دوبعدی.
> بازپیاده‌سازی Qt از Grace (<https://plasma-gate.weizmann.ac.il/Grace/>) با همان رابط خط فرمان.
> اطلاعات بیشتر: <https://sourceforge.net/projects/qtgrace/>.

- رسم یک یا چند فایل داده و رسم فقط دو ستون نخست هر فایل به‌صورت X Y:

`qtgrace {{path/to/file1.dat path/to/file2.dat ...}}`

- رسم یک یا چند فایل داده و رسم همهٔ ستون‌های هر فایل به‌صورت X Y1 Y2 ...:

`qtgrace {{-nxy path/to/file1.dat -nxy path/to/file2.dat ...}}`

- رسم یک یا چند فایل داده با محور x در مقیاس لگاریتمی:

`qtgrace -log x {{path/to/file1.dat path/to/file2.dat ...}}`

- رسم فایل داده با مقیاس لگاریتمی در هر دو محور و داده‌های قالب‌بندی‌شده به‌صورت X Y DY:

`qtgrace -log xy -settype xydy {{path/to/file.dat}}`

- نمایش راهنما:

`qtgrace -help`
