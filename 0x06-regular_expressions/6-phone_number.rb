#!/usr/bin/env ruby
# Matches a 10-digit phone number and prints it if the provided string is exactly 10 digits long.
puts ARGV[0].scan(/^\d{10,10}$/).join
