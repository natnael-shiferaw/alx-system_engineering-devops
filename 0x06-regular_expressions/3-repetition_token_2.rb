#!/usr/bin/env ruby
# Outputs all words that start with 'h', end with 'n', and have any single character in between.
puts ARGV[0].scan(/hbt+n/).join
