# firewall-cmd

> کارخواه firewalld.
> مشاهده و تغییر وضعیت پیکربندی زمان اجرا یا دائمی دیوار آتش.
> اطلاعات بیشتر: <https://firewalld.org/documentation/man-pages/firewall-cmd>.

- مشاهدهٔ همهٔ ناحیه‌ها و قواعد موجود دیوار آتش در وضعیت پیکربندی زمان اجرا:

`firewall-cmd --list-all-zones`

- انتقال دائمی رابط به ناحیهٔ block و در نتیجه مسدود کردن همهٔ ارتباطات:

`firewall-cmd --permanent --zone {{block}} --change-interface {{enp1s0}}`

- باز کردن دائمی درگاه یک سرویس در ناحیهٔ مشخص (مانند درگاه 443 در ناحیهٔ `public`):

`firewall-cmd --permanent --zone {{public}} --add-service {{https}}`

- بستن دائمی درگاه یک سرویس در ناحیهٔ مشخص (مانند درگاه 80 در ناحیهٔ `public`):

`firewall-cmd --permanent --zone {{public}} --remove-service {{http}}`

- هدایت دائمی درگاه بسته‌های ورودی در ناحیهٔ مشخص (مانند درگاه 443 به 8443 هنگام ورود به ناحیهٔ `public`):

`firewall-cmd --permanent --zone {{public}} --add-rich-rule 'rule family "{{ipv4|ipv6}}" forward-port port "{{443}}" protocol "{{udp|tcp}}" to-port "{{8443}}"'`

- بارگذاری مجدد firewalld برای دور ریختن تغییرات زمان اجرا و اعمال فوری پیکربندی دائمی:

`firewall-cmd --reload`

- ذخیرهٔ وضعیت پیکربندی زمان اجرا در پیکربندی دائمی:

`firewall-cmd --runtime-to-permanent`

- فعال کردن حالت اضطراری؛ همهٔ ترافیک دور انداخته و همهٔ اتصال‌های فعال قطع می‌شوند:

`firewall-cmd --panic-on`
