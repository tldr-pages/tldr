# datamash

> انجام عملیات پایهٔ عددی، متنی و آماری روی فایل‌های دادهٔ متنی ورودی.
> اطلاعات بیشتر: <https://www.gnu.org/software/datamash/manual/datamash.html#Invoking-datamash>.

- دریافت بیشینه، کمینه، میانگین و میانهٔ یک ستون از اعداد:

`seq 3 | datamash max 1 min 1 mean 1 median 1`

- دریافت میانگین یک ستون از اعداد اعشاری (اعداد باید از «,» به جای «.» استفاده کنند):

`echo -e '1.0\n2.5\n3.1\n4.3\n5.6\n5.7' | tr '.' ',' | datamash mean 1`

- دریافت میانگین یک ستون از اعداد با دقت اعشاری مشخص:

`echo -e '1\n2\n3\n4\n5\n5' | datamash {{[-R|--round]}} {{number_of_decimals_wanted}} mean 1`

- دریافت میانگین یک ستون از اعداد با نادیده گرفتن رشته‌های دقیق «Na» و «NaN»:

`echo -e '1\n2\nNa\n3\nNaN' | datamash --narm mean 1`
