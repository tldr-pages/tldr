# sealert

> تحلیل و توضیح پیام‌های رد دسترسی AVC در SELinux.
> بخشی از بستهٔ `setroubleshoot-server`.
> همچنین : `audit2why`, `ausearch`, `audit2allow`.
> اطلاعات بیشتر: <https://manned.org/sealert>.

- تحلیل همهٔ رد دسترسی‌های اخیر SELinux:

`sudo sealert {{[-a|--analyze]}} {{/var/log/audit/audit.log}}`

- تحلیل شناسهٔ هشدار مشخص از گزارش‌های سیستم:

`sudo sealert {{[-l|--lookupid]}} {{alert_id}}`

- نمایش خلاصهٔ هشدارهای اخیر SELinux:

`sudo sealert {{[-b|--browser]}}`

- پایش بلادرنگ گزارش ممیزی برای هشدارهای جدید:

`sudo tail {{[-f|--follow]}} {{/var/log/audit/audit.log}} | sealert {{[-l|--lookupid]}} -`
