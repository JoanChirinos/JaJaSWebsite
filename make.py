#! /usr/bin/python

import cgi,cgitb

cgitb.enable()

def go():
    print 'Content-type: text/html\n\n'
    html = openclose("itemPageTemplate.html")
    what = "Small_Pot"
    itemData = openclose("itemFiles/items.csv").split("\n")
    for s in itemData:
        if s[:len(what)] == what:
            itemData = s.replace("_", " ").split(",")
            break
    html = html.replace("ITEMNAME", itemData[0])
    html = html.replace("ITEMPRICE", itemData[1])
    html = html.replace("ITEMDETAILS", itemData[2])
    html = html.replace("IMAGENAME", itemData[3])
    print html
    
def openclose(fileName):
    straw = open(fileName, "rU")
    data = straw.read()
    straw.close()
    return data

go()
