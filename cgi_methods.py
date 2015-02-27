#this is a template, so the code only needs to be written once as it can be tiresome to keep typing out the same basic code into every script

def start_html(title, css=None):
html="""Content-Type: text/html

<!DOCTYPE html>
<html><head><title>%s</title>"""%title

    if css is not None:
      html=html+"\n<link rel="stylehsheet" type="text/css" href='%s'>\n"%css
html=html+"<\head>\nbody>"
return html

#this can be added into the start of the CGI script.