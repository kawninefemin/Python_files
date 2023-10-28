from playsound import playsound

print("no of available songs\n1.Be Alright\n2.Iraaday\n3.Galaxies")
order= input('enter the music which you want to play')
if "Be alright" in order:
    playsound('C:\\Users\\kawni\\Music\\Be alright.mp3')
elif"Iraaday" in order:
    playsound('C:\\Users\\kawni\\Music\\Iraaday.mp3')
elif"Galaxies"in order:
    playsound('C:\\Users\\kawni\\Music\\Galaxies.mp3')


