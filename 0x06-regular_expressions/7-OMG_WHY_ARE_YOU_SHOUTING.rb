#!/usr/bin/env ruby

# Get the input string from command line arguments
input_string = ARGV[0]

# Use a regular expression to find all sequences of zero or more uppercase letters
matches = input_string.scan(/[A-Z]*/)

# Output the matches joined into a single string
puts matches.join

