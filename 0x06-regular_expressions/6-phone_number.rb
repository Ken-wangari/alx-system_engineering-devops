#!/usr/bin/env ruby

# Get the input string from command line arguments
input_string = ARGV[0]

# Use a regular expression to find a sequence of exactly 10 digits at the beginning of the string
matches = input_string.match(/^\d{10}/)

# Output the matched sequence or an empty string if no match is found
puts matches ? matches[0] : ""

