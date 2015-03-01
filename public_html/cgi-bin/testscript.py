#!/usr/local/bin/python
'''This imports the cgi module so that the HTML form can interact with the database'''
import cgi 
import cgitb
''' This activates a special exception handler that will display information in the web browser if any errors occur.'''
cgitb.enable() 

'''This stores the information that is entered into the form'''
form = cgi.FieldStorage() 
'''This imports the mysql database so it can be queried'''
import mysqldb 
'''The mysql query; queries the gene_symbol'''
sql="SELECT gene_symbol, description FROM gene_info where gene_ID=%s" 

'''my personal details to access MySQL'''
db=MySQLdb.connect(db='frehman', user=' frehman', passwd='XFzNi39a') 
'''Activates the cursor'''
cursor=db.cursor()
cursor.executed(sql, form[''].value)
'''Executes it'''
result=cursor.fethall()
result

'''This gets the result'''
EXPsql='SELECT sum(expression_value)/count(expression_value) FROM sample INNER JOIN expression1_info ON sample.gene_ID=expression.gene_ID JOIN probes_info ON expression.ID_REF=probes.ID_REF WHERE gene_ID= %s"
cursor.execute(EXPsql,(self.gene_ID,)self.ID_REF)
EXPsqlresult=cursor.fetchall()
EXPsqlresult

'''This executes the sql search'''

print "Content-Type: text/html"     # HTML is following
print                               # blank line, end of headers
print "<html><head><TITLE>CGI script output</TITLE></head>" #This displays nicely formatted text with a header.
print "<body><H1>Gene Information</H1>"
print"<b>gene ID:	</b>"

for k in form.keys():
        print "<tr><td>%s</td><td>%s</td></tr>"%(k, form[k].value)


'''Prints the table'''
print "<table>"
print "<b> Gene Symbol, Description</b>"
print result
print "</body></html>"
'''Prints the results of the query'''
print EXPsqlresult