# diff

> مقایسه فایل(ها) و پوشه(ها).
> اطلاعات بیشتر: <https://man7.org/linux/man-pages/man1/diff.1.html>.

- مقایسه فایل ها (فهرست تغییرات فایل های قدیمی به جدید) :

`diff {{old_file}} {{new_file}}`

- مقایسه فایل ها، با صرف نظر از فاصله های خالی:

`diff --ignore-all-space {{old_file}} {{new_file}}`

- مقایسه فایل ها، با نمایش تفاوت ها در کنار هم:

`diff --side-by-side {{old_file}} {{new_file}}`

- مقایسه فایل ها، به نمایش تفاوت ها به صورت یکپارچه (همانند `git diff`) :

`diff --unified {{old_file}} {{new_file}}`

- مقایسه بازگشتی پوشه ها (نمایش اسامی متفاوت فایل ها و پوشه ها و همچنین تغییرات فایل ها):

`diff --recursive {{old_directory}} {{new_directory}}`

- نمایش نام فایل های متفاوت مقایسه شده:

`diff --recursive --brief {{old_directory}} {{new_directory}}`

- از تفاوت دو فایل متنی یک بروزرسانی میسازد، فایل های ناموجود را خالی فرض میکند :

`diff --text --unified --new-file {{old_file}} {{new_file}} > {{diff.patch}}`
