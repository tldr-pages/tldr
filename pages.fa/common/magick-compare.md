# magick compare

> ایجاد یک تصویر مقایسه ای برای مشخص کردن تفاوتهای دو عکس به صورت بصری.
> بخشی از ImageMagick است.
> اطلاعات بیشتر: <https://imagemagick.org/script/compare.php>.

- مقایسه دو عکس:

`magick compare {{path/to/image1.png}} {{path/to/image2.png}} {{path/to/diff.png}}`

- مقایسه دو عکس با استفاده از معیار دلخواه:

`magick compare -verbose -metric {{PSNR}} {{path/to/image1.png}} {{path/to/image2.png}} {{path/to/diff.png}}`
