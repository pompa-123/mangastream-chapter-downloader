import requests
import os
from bs4 import BeautifulSoup


select = input("Tekli(1) or Çoklu(2):")

if(select == "1"):
    id2 = input("ID: ")
    url = "https://example.com/query.php?&auth=AUTH&id="+id2 # Site Linki ve AUTH Anahtarı
    idclass = "aligncenter size-full "
    r = requests.get(url)
    soup = BeautifulSoup(r.content, "html.parser")
    div = soup.find('h1',{"class":"entry-title"})
   

    divtext = div.text
    if(divtext == 'notfound'):
        print("Sonuç Bulunamadı")
        exit()
    
    dosya2 = str.maketrans(":|/[]'", "aaaaaa")
    dosya = divtext.translate(dosya2)
    path = dosya
    os.mkdir(path)
    print("Dizin Oluşturma İşlemi Başarılı '% s' Adı Dizin Oluşturuldu")

    for i, j in enumerate(soup.find_all('img',{"id":"icerik"})):
        try:
            data = requests.get(j.get("src"), stream=True)
            if b"PNG" in data.content:
                filename = f"{dosya}/img{i}.png"
                print({i})
            elif b"JFIF" in data.content:
                filename = f"{dosya}/img{i}.jpg"
                print({i})
            else:
                filename = f"{dosya}/img{i}.png"
                print({i})
            with open(filename, "wb") as f:
                for chunk in data.iter_content(chunk_size=4096):
                    f.write(chunk)
        except ValueError as err:
            print("işlem tamamlandı")
if(select == "2"):
    row = int(input("Kaç Tane Çekilecek:"))  
    column = 1
    matrix = []  
    print("ID giriniz:")  
    
     
    for i in range(row):         
        a =[]  
        for j in range(column):  
            a.append(int(input()))  
            
        matrix.append(a)  
    
     
    for i in range(row):  
        for j in range(column):  
            id2 = str(matrix[i][j])
            url = "https://example.com/query.php?&auth=AUTH&id="+id2 # Site Linki ve AUTH Anahtarı
            idclass = "aligncenter size-full "
            r = requests.get(url)
            soup = BeautifulSoup(r.content, "html.parser")
            div = soup.find('h1',{"class":"entry-title"})

            divtext = div.text
            if(divtext == 'notfound'):
                print("Sonuç Bulunamadı")
                continue
            dosya2 = str.maketrans(":|/[]'", "aaaaaa")
            dosya = divtext.translate(dosya2)
            path = dosya
            os.mkdir(path)
            print("Dizin Oluşturma İşlemi Başarılı '% s' Adı Dizin Oluşturuldu")

            for i, j in enumerate(soup.find_all('img',{"id":"icerik"})):
                try:
                    data = requests.get(j.get("src"), stream=True)
                    if b"PNG" in data.content:
                        filename = f"{dosya}/img{i}.png"
                        print({i})
                    elif b"JFIF" in data.content:
                        filename = f"{dosya}/img{i}.jpg"
                        print({i})
                    else:
                        filename = f"{dosya}/img{i}.png"
                        print({i})
                    with open(filename, "wb") as f:
                        for chunk in data.iter_content(chunk_size=4096):
                            f.write(chunk)
                except ValueError as err:
                    print("işlem tamamlandı")





