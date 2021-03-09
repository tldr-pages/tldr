#!/bin/bash

# Check if the user is in tldr/scripts/
directory=$(pwd | grep -o ".\{13\}$")
if [ $directory != "/tldr/scripts" ]; then
    echo "Please make sure your current working directory is tldr/scripts/"
    exit 1
fi

# Print info message
echo "Creating list of all executables on your system which don't yet have a tldr page."
echo "For a list of missing translations, please refer to https://lukwebsforge.github.io/tldri18n/."

# Create needed files
mkdir /tmp/find-undocumented
touch /tmp/find-undocumented/bin-files
touch /tmp/find-undocumented/tldr-pages
touch /tmp/find-undocumented/bin-files-sorted
touch /tmp/find-undocumented/tldr-pages-sorted
touch ../undocumented.txt

# Create list of all binaries on the system
for path in ${PATH//:/ }; do
    ls $path >> /tmp/find-undocumented/bin-files
done

# Create a list of all tldr pages
pagelist=( ../pages/common/ ../pages/linux/ ../pages/osx/ ../pages/sunos/ ../pages/windows/ )
for path in ${pagelist[@]}; do
    ls $path | cut -d "." -f 1 >> /tmp/find-undocumented/tldr-pages
done

# Sort both files and delete duplicate entries
sort -u /tmp/find-undocumented/bin-files > /tmp/find-undocumented/bin-files-sorted
sort -u /tmp/find-undocumented/tldr-pages > /tmp/find-undocumented/tldr-pages-sorted

# Create a diff with all files which are in
diff /tmp/find-undocumented/bin-files-sorted /tmp/find-undocumented/tldr-pages-sorted | grep "<" | cut -c 3- > ../undocumented.txt

# Clean up
rm /tmp/find-undocumented/bin-files
rm /tmp/find-undocumented/tldr-pages
rm /tmp/find-undocumented/bin-files-sorted
rm /tmp/find-undocumented/tldr-pages-sorted
rmdir /tmp/find-undocumented

echo "List created successfully"
echo "Output file is tldr/undocumented.txt"
