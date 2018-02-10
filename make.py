#! /usr/bin/python

import cgi,cgitb

cgitb.enable()

def go():
    print 'Content-type: text/html'
    html = opensaveclose("itemPageTemplate.html")
    vals = cgi.FieldStorage()
    what = vals.getValue("what")
    itemData = opensaveclose("itemFiles/items.csv").split("\n")
    for s in itemData:
        if s[:len(what) == what]:
            itemData = s.replace("_", " ").split(",")
            break
    html.replace("ITEMNAME", itemData[0])
    html.replace("ITEMPRICE", itemData[1])
    html.replace("ITEMDETAILS", itemData[2])
    html.replace("IMAGENAME", itemData[3])
    print html
    
def opensaveclose(fileName) {
    straw = open(fileName, "rU")
    data = straw.read()
    straw.close()
    straw = open(fileName, "w+")
    straw.write(data)
    straw.close()
    return data
}

go()