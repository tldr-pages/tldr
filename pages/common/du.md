# du

> Disk usage: estimate and summarize file and directory space usage.

- List the sizes of a directory and any subdirectories, in the given unit (B/KB/MB):

`du -{{b|k|m}} {{path/to/directory}}`

- List the sizes of a directory and any subdirectories, in human-readable form (i.e. auto-selecting the appropriate unit for each size):

`du -h {{path/to/directory}}`

- Show the size of a single directory, in human readable units:

`du -sh {{path/to/directory}}`

- The (x) is used to exclude NFS or other file types within the partition that is being scanned:

`du -xsh {{path/to/directory}}`

- List the human-readable sizes of a directory and of all the files and directories within it:

`du -ah {{path/to/directory}}`

- List the top 10 largest files in megabytes, sorted by largest:

`du -Sm /var/log | sort -rn | sed '{11,$D; =}' | sed 'N; s/\n/ /' | awk '{printf $1 ":" "\t" $2 "\t" $3 "\n"}'`

- List the human-readable sizes of a directory and any subdirectories, up to N levels deep:

`du -h --max-depth=N {{path/to/directory}}`

- List the human-readable size of all .jpg files in subdirectories of the current directory, and show a cumulative total at the end:

`du -ch */*.jpg`

- Number of files search:

``echo "Detailed Inode usage for: $(pwd)" ; for d in `find -maxdepth 1 -type d |cut -d\/ -f2 |grep -xv . |sort`; do c=$(find $d |wc -l) ; printf "$c\t\t- $d\n" ; done ; printf "Total: \t\t$(find $(pwd) | wc -l)\n"``

`find . -printf "%h\n" | cut -d/ -f-2 | sort | uniq -c | sort -rn`

`find / -xdev -printf '%h\n' | sort | uniq -c | sort -k 1 -n`
