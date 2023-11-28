#!/usr/bin/env ruby
# Outputs all characters that match the pattern "hbt*n" from the provided string.
puts ARGV[0].scan(/hbt*n/).join
