import csv


def newH():
    nodes=[]
    links=[]
    onlyLinks=[]
    market=[]
    club=[]
    ads=[]
    schol=[]
    board=[]
    aq=[]
    sex=[]
    schools=[]
    f = open('survey - Copy.csv','rb')
    reader = csv.reader(f)
    for row in reader:
        nodes.append(row[1+2].lower()+" "+row[2+2])
        links.append(list((1,row[10+2])))
        market.append(row[5+2])
        club.append(row[7+2])
        ads.append(row[5+2])
        schol.append(row[8+2])
        board.append(row[3+2])
        aq.append(row[9+2])
        sex.append(row[1])
        schools.append(row[2])
        
    for i in range(len(links)):
        links[i].pop(0)
    f.close()
    final=[]
    f = open("board.net", "w")
    f.write("*Vertices 135 ic Black \n")
    f.write("1 'Marketing' ic Black \n")
    f.write("2 'Club_Events' ic Black \n")
    f.write("3 'Advertisement' ic Black  \n")
    f.write("4 'HU_School_Events' ic Black \n")
    f.write("5 'Aquaintance' ic Black \n")
    f.write("6 'Sindh Board' ic Black \n")
    f.write("7 'O/A Level Board' ic Black \n")
    f.write("8 'Agha Khan Board' ic Black \n")
    f.write("9 'Federal Board' ic Black \n")
    for i in range(1,127):
        if sex[i]=="Female":
            if schools[i]=="SSE":
                f.write(str(i+9)+" "+"'"+str(i)+"'"+" "+"ic Blue"+" box"+"\n")
            elif schools[i]=="Undecided":
                 f.write(str(i+9)+" "+"'"+str(i)+"'"+" "+"ic Blue"+" triangle"+"\n")
            else:
                f.write(str(i+9)+" "+"'"+str(i)+"'"+" "+"ic Blue"+"\n")

        if sex[i]=="Male":
            if schools[i]=="SSE":
                f.write(str(i+9)+" "+"'"+str(i)+"'"+" "+"ic Pink"+" box"+"\n")
            elif schools[i]=="Undecided":
                 f.write(str(i+9)+" "+"'"+str(i)+"'"+" "+"ic Pink"+" triangle"+"\n")
            else:
                f.write(str(i+9)+" "+"'"+str(i)+"'"+" "+"ic Pink"+"\n")
        if sex[i]=="Other":
            if schools[i]=="SSE":
                f.write(str(i+9)+" "+"'"+str(i)+"'"+" "+"ic Green"+" box"+"\n")
            elif schools[i]=="Undecided":
                 f.write(str(i+9)+" "+"'"+str(i)+"'"+" "+"ic Green"+" triangle"+"\n")
            else:
                f.write(str(i+9)+" "+"'"+str(i)+"'"+" "+"ic Green"+"\n")


    f.write("*Arcslist \n")
    for i in range(1,127):
        for j in range(len(links[i])):
            for k in links[i]:
                newlist=k.split(",")
                final.append(newlist)
            for k in newlist:
                k=k.lower()
                if k in nodes:
                    ind=nodes.index(k)
                    f.write(str(i+9)+ " "+str(ind+1)+"\n")
##        if market[i]=='1':
##            f.write(str(i+9)+" 1 \n")
##        if club[i]=="1 (most influence)":
##            f.write(str(i+9)+" 2 \n")
##        if ads[i]=="1 (most influence)":
##            f.write(str(i+9)+" 3 \n")
##        if schol[i]=="1 (most influence)":
##            f.write(str(i+9)+" 4 \n")
##        if aq[i]=="1 (most influence)":
##            f.write(str(i+9)+" 5 \n")
##            if board[i]!=None:
                
                if board[i]=='Sindh board':
                    f.write(str(i+9)+" 6 \n")
                elif board[i]=='O/A levels':
                    f.write(str(i+9)+" 7 \n")
                elif board[i]=='Agha Khan Board':
                    f.write(str(i+9)+" 8 \n")
                elif board[i]=='Federal Board':
                    f.write(str(i+9)+" 9 \n")
              

              

newH()
