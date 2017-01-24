<?php

// Convert a .md file to HTML

if ($argc < 3)
{
   echo "Please provide the name of an .md file and an output/html file.\n";
   echo "usage: $argv[0] file.md newfile.html\n";
   exit(1);
}

$md = fopen($argv[1], "r");
if (! $md)
{
   echo "The .md file $argv[1] was not found.\n";
   exit(2);
}

$html = fopen($argv[2], "w");
if (! $html)
{
   echo "Was not able to create the html file $argv[2].\n";
   exit(3);
}

$block = false;
$input = fgets($md);
while ($input)
{
   // start making changes
   // replace lines starting with # with header markers

   if ($input[0] == '#')
   {
      $input = trim($input);
      $output = str_replace('# ', '<b>', $input);
      $output = $output . '</b><br><br>';
   }
   else if ($input[0] == '>')
   {
      $input = trim($input);
      $output = str_replace('> ', '<b>', $input);
      $output = $output . '</b><br><br>';
   }
   // Handle opening and closing block quotes
   else if ( strpos($input, '```') !== FALSE)
   {
      if ($block)
      {
        $output = '</blockquote>';
        $block = false;
      }
      else
      {
         $output = "<blockquote>\n";
         $block = true;
      }
   }
   else if ($input[0] == '`')
   {
       $input = trim($input);
       $output = '<blockquote>' . substr($input, 1);
       $output = str_replace('`', '</blockquote>', $output);
   }
   else
     $output = $input;

   $output = str_replace('{{', '<i>', $output);
   $output = str_replace('}}', '</i>', $output);
   // When working in a block quote, add a newline
   if ($block)
      $output = $output . '<br>';
   fputs($html, $output);

   $input = fgets($md);
}   // end of reading from md file

fputs($html, "\n");
fclose($md);
fclose($html);

