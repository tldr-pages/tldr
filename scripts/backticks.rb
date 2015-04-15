#!/usr/bin/env ruby

def plural num
  's' unless num == 1
end

def missing_backticks? str
  str.count('`').odd?   
end

total = 0

Dir["pages/**/*.md"].each do |page|
  lines = File.readlines(page).find_all { |line| missing_backticks?(line) }

  unless lines.empty?
    puts "Found #{lines.size} missing backtick#{plural(lines.length)} in #{page}:"
    lines.each { |line| puts "    #{line.chomp}" }
    puts
  end

  total += lines.length
end

puts "Okay, found #{total} missing backtick#{plural(total)} in all."
