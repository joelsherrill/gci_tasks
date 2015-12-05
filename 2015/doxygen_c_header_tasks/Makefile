
all:
	./gen_file_list
	(cat header ; cat *.csv|  grep -v ^name | grep -v "^$$" ) >../all.csv
	
clean:
	rm -rf file_lists/* csv files* *.csv ../all.csv

