#!/usr/bin/env ruby
# Parses the input string in ARGV[0] to extract sender, receiver, and flags.
# Outputs the sender and receiver phone numbers or names (with optional country codes),
# along with the corresponding flags enclosed in square brackets.
# Usage: ./script_name.rb "[from:SENDER] [to:RECEIVER] [flags:1:2:3:4:5]"
puts ARGV[0].scan(/\[from:(\+?\w+)\] \[to:(\+?\w+)\] \[flags:(-?\d:-?\d:-?\d:-?\d:-?\d)\]/).join(",")
