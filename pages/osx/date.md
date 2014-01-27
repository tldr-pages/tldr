# date

> display or set the system date

- display the date

`date`

- format the date

    	date +FORMAT

    	FROMAT options (basic)
    	====
    	Date based:
    	%c  locale's date and time
    	%d  day of month (01)
    	%m  month (01..12)
    	%y  year (00..99)
    	%Y  year (2000..)

    	Time based:
    	%H  hour (00..23)
    	%h  hour (0..23)
    	%I  hour (01..12)
    	%i  hour (1..12)
    	%M  minute (0..59)
    	%S  seconds (00.60)

	    Example:
	    ====
	    date +"%d/%m/%Y %H:%M:%S"

