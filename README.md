This project will show the data analysis of the placentas of women who smoked during pregnancy through a webpage.
Smoking increases the risk of preterm delivery and complications such as placental preia and abruption. Results
provide insight into the molecular basis of smoke-induced placenta abnormalities.

Currently I have a working parser called parser_template1.py. I have transferred the geo data set into a file called samples.txt.
I have formatted the data set table to make it look neater by tabulating each column, the code for this is available under tabulatingtable.py.
The file called data.md will have all the bits of code I have used and what the code does.
The parser_template1 allows the data set to be imported into the tables made in MySQL.
The code for these tables are available under mysql_table_code.

cgi_methods.py is a template, so that you don't need to keep writing out the same basic code in every script.

models.py is a class, that would have completed if there was more time available.



Tables have been made for the data genes.txt, probes.txt and expression.txt, the data was loaded into the tables, the code for this is also available under mysql_table_code
A new table was made for the expression.txt data as I wasn't sure how to add another column, the table is now called
expression1_info. I also accidently called the column sample_name instead of naming it gene_ID, so I changed it using the ALTER function but I accidently changed the data type in that column to be an INTEGER instead of VARCHAR.
This was then changed back.
An example of how the tables were linked is also avaliable under mysql_table_code

Probes.txt, genes.txt and expression.txt  have the required data for the tables probe_info, gene_info and expression1_info respectively.

public_html is a new directory and another README file will be available there.

