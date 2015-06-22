require 'csv'

arr_of_arrs = CSV.read("sight.csv")
arr_of_arrs.shift

adjust_ary = arr_of_arrs.map do |ele|
    ele[1].gsub!(/[“”]/,'')
    [ele[0],"#{ele[1]}。#{ele[2]}"]
end

place_ary = arr_of_arrs.map do |e|
    e[0]
end.uniq

h = Hash.new

place_ary.each do |place|
    h[place] = ''
end


h.each do |key, value|
    selected_ary = adjust_ary.select { |arr| arr[0] == key }
    selected_ary.each do |s|
        s[1].gsub!(/[\"\s]/, '')
        h[key] << s[1]
    end
end

CSV.open("sight_modified.csv", "wb") do |csv|
  csv << ['sight', 'comment']
  h.each do |key, value|
    csv << [key, value]
  end
end


