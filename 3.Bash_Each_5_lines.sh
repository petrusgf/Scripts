# Write a script with a function that accepts a string to insert, a line number and filename. The
# function should open the file and insert the string at the first occurrence of line_number and all
# increments of line_number until the end of the file is reached. e.g. if line_number is 5, lines 5,
# 10, 15, etc. should be modified until EOF is reached.

echo "Enter filename:"

read filename

echo "What String do you want to add?"

read str

echo "How many lines?"

read line_number

sed -i ""0~$line_number" "s/^/$str/g"" $filename

grep $str $filename 
