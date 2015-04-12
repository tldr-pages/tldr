#!/usr/bin/env ruby

require "json"

commands = {}

Dir["#{ENV["TLDRHOME"]}/pages/**/*.md"].each do |file|
    # "./pages/osx/xsltproc.md",
    file = file.split("/")
    name = file.pop().gsub(".md","")
    platform = file.pop()

    unless commands.key?(name)
        commands[name] = {
            name: name,
            platform: [platform]
        } 
    else
        commands[name][:platform] << platform
    end
end

commands = commands.map do |k,v| v end

File.write("#{ENV["TLDRHOME"]}/pages/index.json", {commands: commands}.to_json)
