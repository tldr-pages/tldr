# composer

> ابزاری بسته محور برای مدیریت وابستگی های پروژه های php.
> اطلاعات بیشتر: <https://getcomposer.org/>.

- ساخت یک فایل `composer.json` به صورت کنشگرا:

`composer init`

- اضافه کردن یک بسته به عنوان وابستگی به این پروژه، همچنین یک ورودی به `composer.json` وارد می کند:

`composer require {{user/package}}`

- نصب تمام وابستگی های این پروژه که در `composer.json` هستند و `composer.lock` را ایجاد می کند:

`composer install`

- حذف یک بسته از این پروژه، وابستگی مربوط به آنرا از `composer.json` و `composer.lock` حذف می کند:

`composer remove {{user/package}}`

- بروزرسانی تمام وابستگی های این پروژه که در `composer.json` هستند و یادداشت کردن نسخه های جدید در فایل `composer.lock`:

`composer update`

- فقط `composer.lock` را بروزرسانی می کند بعد از این که `composer.json` را به صورت دستی بروزرسانی کردید:

`composer update --lock`

- اطلاعات بیشتری درباره دلیل نصب نشدن یک وابستگی ارائه می دهد:

`composer why-not {{user/package}}`

- بروزرسانی کامپوزر به آخرین نسخه اش:

`composer self-update`
