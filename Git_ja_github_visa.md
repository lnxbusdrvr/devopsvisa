#Tässä on myös pistelasku, jos ei haluta niin otetaan pois. Joku halusi niitä silmukoita, mutta niistä ei ole sovittu tarkemmin. Alan olla kypsä vetämään tyyppejä niihin silmukoihin. 
score = 0
score = int(score)

print("Viisi kysymystä GitHubista!")
print("Vastaa vaihtoehdon numerolla")
#Viisi ysymystä GitHubista.
#Vastaa vaihtoehdon numerolla. 

#Eka kyssäri sit 

print("""Mikä on oikea vaihtoehto, kun lisätään GitHubiin tiedostoja?
1. git add git commit git push
2. git commit git add git push 
3. git commit git checkout 
4. git add git branch git commit""")

answer1 = "1"
response1 = input("Vastaat:")

if (response1 != answer1):
    print("Kertaa vielä")
else:
    print("Vastasit oikein! ")
    score = score + 1

print("Pistetilanteesi on " + str(score) +  " viidestä")

#Toka

print("""Mihin päähaara masteria ja sen haaroja eli branches käytetään?
1. Uusien ominaisuuksien toteuttamiseen 
2. Bugikorjauksiin
3. Versionhallintaan 
4. Kaikkiin edellämainittuihin""")

answer2 = "4"
response2 = input("Vastaat:")

if (response2 != answer2):
    print("Kertaa vielä")


else:
    print("Vastasit oikein!  ")
    score = score + 1

print("Pistetilanteesi on  " + str(score) + " viidestä")

#Kolmas

print("""Koska tehdään pull- tai merge-request?
1. Kun aloitetaan projektityö  
2. Kun halutaan saada kavereiden kommentit 
3. Kun halutaan yhdistää branchit  
4. Kaikki vaihtoehdot ovat oikein""")

answer3 = "4"
response3 = input("Vastaat:")

if (response3 != answer3):
    print("Kertaa vielä, GitHub on monipuolinen!")
else:
    print("Vastasit oikein ! ") 
    score = score + 1

print("Pistetilanteesi on " + str(score) + " viidestä")

#Nelonen!
print("""Millä komennolla Gitissä poistetaan tiedosto?
1. git delete 
2. git rm
3. git remove
4. git del""")

answer4 = "2"
response4 = input("Vastaat:")

if (response4 != answer4):
    print("Kertaa vielä!")
else:
    print("Vastasit oikein! ")
    score = score + 1

print("Pistetilanteesi on " + str(score) + " viidestä")

#Viimienen kysymys
print ("""Työskentelyn alussa ja lopussa on keskeistä AINA muistaa?
1. Luoda aina uusi branch ja lopussa mergetä se
2. Nimetä projekti uudestaan
3. Tehdä alussa pull ja sitten lopettaessa push. 
4. Päivittää README-tiedostoon, mitä on tehnyt""")

answer5 = "3"
response5 = input("Vastaat:")

if (response5 != answer5):
    print("Kertaa vielä")
else:
    print("Vastasit oikein! ")
    score = score + 1

print("Kokonaispistemääräsi on " + str(score) +  " viidestä")
