from datetime import date

date_object = date.today()
year = date_object.strftime("%Y")

inf = open('request.txt', 'r')
r = inf.readlines()
inf.close()

inf2 = open('partial.txt', 'r')
p = inf2.readlines()
inf2.close()

sections = []#process sections
i = 2
while r[i] != '\n':
    sections.append(r[i])
    i=i+1

outf = open('index.html', 'w')

outf.write(p[0])

outf.write(r[0])#tab title

outf.write(p[1])

outf.write(r[0])#nav bar title

outf.write(p[2])

for s in sections:#nav bar items
    outf.write('<li class="page-scroll"><a href="#'+s+'">'+s+'</a></li>')

outf.write(p[3])

outf.write(r[len(sections)+3])#big image

outf.write(p[4])

outf.write(r[len(sections)+5])#big text

outf.write(p[5])

i = len(sections)+7#second line of text
while r[i] != '\n':
    outf.write(r[i])
    i=i+1

outf.write(p[6])

for s in sections:#main sections
      outf.write(p[9]+s+p[10]+s+p[11])
      i=i+1
      while i < len(r) and r[i] != '\n':
          outf.write(r[i])
          i=i+1
      outf.write(p[12])
      
outf.write(p[7])

outf.write(r[0]+" "+year)#footer

outf.write(p[8])

outf.close()
