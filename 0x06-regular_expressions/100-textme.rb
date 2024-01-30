#!/usr/bin/env ruby

# Get the input string from command line arguments
input_string = ARGV[0]

# Use a regular expression with named capture groups to extract specific information
matches = input_string.scan(/\[from:(?<from>.*?)\] \[to:(?<to>.*?)\] \[flags:(?<flags>.*?)\]/)

# Output the matches joined into a single string
puts matches.map { |match| "#{match[0]},#{match[1]},#{match[2]}" }.join(",")

