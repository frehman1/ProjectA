fh=open('samples.txt')
for line in fh.readlines():
    line=line.replace('none no exposure non', '\tnon\tno exposure\non'), 
    print(line)

fh1=open('samples.txt')
for line in fh1.readlines():
    line1=line.replace('tobacco smoke light exposure light', '\ttobacco smoke\tlight exposure\tlight')
    print(line1)

fh2=open('samples.txt')
for line in fh2.readlines():
    line2= line.replace('tobacco smoke heavy exposure heavy smoker', '\ttobacco smoke\theavy exposure\theavy')
    print(line2)
