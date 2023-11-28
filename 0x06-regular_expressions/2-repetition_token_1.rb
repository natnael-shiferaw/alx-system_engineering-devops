#!/usr/bin/env ruby
# Outputs the substring that matches the regular expression "hb?tn" from the provided string.
# Usage: ./2-repetition_token_1.rb
puts ARGV[0].scan(/hb?tn/).join
