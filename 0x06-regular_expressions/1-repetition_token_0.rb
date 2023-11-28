#!/usr/bin/env ruby
# Outputs all words that start with 'h', end with 'n', and contain 2 to 5 occurrences of the letter 't' in between.
# Usage: ./1-repetition_token_0.rb
puts ARGV[0].scan(/hbt{2,5}n/).join
