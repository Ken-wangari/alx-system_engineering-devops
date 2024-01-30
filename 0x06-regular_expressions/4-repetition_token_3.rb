#!/usr/bin/env ruby

# Get the input string from command line arguments
input_string = ARGV[0]

# Use a regular expression to find all matches of the pattern hbt*n
matches = input_string.scan(/hbt*n/)

# Output the matches joined into a single string
puts matches.join

