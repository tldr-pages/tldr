# curl

> انتقال داده از/به سرور.
> از اکثر پروتکل‌ها از جمله HTTP، FTP و POP3 پشتیبانی می‌کند.
> اطلاعات بیشتر: <https://curl.se/docs/manpage.html>.

- دانلود محتوای یک URL و ذخیره آن در یک فایل(با نام دلخواه):

`curl {{http://example.com}} --output {{path/to/file}}`

- دانلود یک فایل و ذخیره آن با نام فایل مشخص شده توسط URL:

`curl --remote-name {{http://example.com/filename}}`

- دانلود یک فایل، با دنبال کردن تغییرمسیرهای لینک(location redirects) و ادامه خودکار(از سرگیری) انتقال فایل قبلی. درصورت بروز دادن خطای سرور، خطا نمایش داده خواهد شد:

`curl --fail --remote-name --location --continue-at - {{http://example.com/filename}}`

- ارسال داده(فرم) رمزگذاری شده (درخواست POST از نوع application/x-www-form-urlencoded). برای خواندن از STDIN، از --data @file_name یا --data @'-' استفاده کنید:

`curl --data {{'name=bob'}} {{http://example.com/form}}`

- ارسال یک درخواست با استفاده از متود HTTP دلخواه و هدرهای(header) اضافی:

`curl --header {{'X-My-Header: 123'}} --request {{PUT}} {{http://example.com}}`

- ارسال داده به صورت JSON، با مشخص کردن content-type مناسب:

`curl --data {{'{"name":"bob"}'}} --header {{'Content-Type: application/json'}} {{http://example.com/users/1234}}`

- مشخص کردن یک نام کاربری و درخواست وارد کردن رمزعبور از سرور، به منظور احراز هویت:

`curl --user {{username}} {{http://example.com}}`

- عبور از گواهی و کلید کاربر یک منبع(رد شدن از اعتبارسنجی گواهی):

`curl --cert {{client.pem}} --key {{key.pem}} --insecure {{https://example.com}}`
