#!/usr/bin/env ruby

require "json"

commands = {}

Dir["pages/**/*.md"].each do |file|
    path = file.split("/")
    name = path.pop().gsub(".md", "")
    platform = path.pop()

    unless commands.key?(name)
        commands[name] = {
            name: name,
            platform: [platform]
        } 
    else
        commands[name][:platform] << platform
    end
end

File.write("pages/index.json", {commands: commands.values}.to_json)

puts "Index rebuilt."
