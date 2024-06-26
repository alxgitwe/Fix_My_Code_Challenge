#!/usr/bin/env ruby

###
#
#  Sort integer arguments (ascending) 
#
###

result = []
ARGV.each do |arg|
    # skip if not integer
    next unless arg =~ /^-?\d+$/

    # convert to integer
    i_arg = arg.to_i
    
    # insert result at the right position
    index = result.bsearch_index { |x| x <=> i_arg }
    if index.nil?
        result << i_arg
    else
        result.insert(index, i_arg)
    end
end

result.sort.each do |num|
    puts num
end
