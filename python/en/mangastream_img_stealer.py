import requests
import os
from bs4 import BeautifulSoup


select = input("Single(1) or Multi(2):")

if(select == "1"):
    id2 = input("ID: ")
    url = "https://example.com/query.php?&auth=AUTH&id="+id2 # Website URL ve AUTH KEY
    idclass = "aligncenter size-full "
    r = requests.get(url)
    soup = BeautifulSoup(r.content, "html.parser")
    div = soup.find('h1',{"class":"entry-title"})
   

    divtext = div.text
    if(divtext == 'notfound'):
        print("Not Found")
        exit()
    
    filess2 = str.maketrans(":|/[]'", "aaaaaa")
    filess = divtext.translate(filess2)
    path = filess
    os.mkdir(path)
    print("'% s' File Created")

    for i, j in enumerate(soup.find_all('img',{"id":"content"})):
        try:
            data = requests.get(j.get("src"), stream=True)
            if b"PNG" in data.content:
                filename = f"{filess}/img{i}.png"
                print({i})
            elif b"JFIF" in data.content:
                filename = f"{filess}/img{i}.jpg"
                print({i})
            else:
                filename = f"{filess}/img{i}.png"
                print({i})
            with open(filename, "wb") as f:
                for chunk in data.iter_content(chunk_size=4096):
                    f.write(chunk)
        except ValueError as err:
            print("process completed")
if(select == "2"):
    row = int(input("How Many Will Be Download?:"))  
    column = 1
    matrix = []  
    print("Enter ID:")  
    
     
    for i in range(row):         
        a =[]  
        for j in range(column):  
            a.append(int(input()))  
            
        matrix.append(a)  
    
     
    for i in range(row):  
        for j in range(column):  
            id2 = str(matrix[i][j])
            url = "https://example.com/query.php?&auth=AUTH&id="+id2 # Website URL ve AUTH KEY
            idclass = "aligncenter size-full "
            r = requests.get(url)
            soup = BeautifulSoup(r.content, "html.parser")
            div = soup.find('h1',{"class":"entry-title"})

            divtext = div.text
            if(divtext == 'notfound'):
                print("Not Found")
                continue
            filess2 = str.maketrans(":|/[]'", "aaaaaa")
            filess = divtext.translate(filess2)
            path = filess
            os.mkdir(path)
            print("'% s' File Created")

            for i, j in enumerate(soup.find_all('img',{"id":"content"})):
                try:
                    data = requests.get(j.get("src"), stream=True)
                    if b"PNG" in data.content:
                        filename = f"{filess}/img{i}.png"
                        print({i})
                    elif b"JFIF" in data.content:
                        filename = f"{filess}/img{i}.jpg"
                        print({i})
                    else:
                        filename = f"{filess}/img{i}.png"
                        print({i})
                    with open(filename, "wb") as f:
                        for chunk in data.iter_content(chunk_size=4096):
                            f.write(chunk)
                except ValueError as err:
                    print("process completed")





