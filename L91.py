#The authors are Maggie Dunn and Cody Brown

lines = ["Haiku frogs in snow", "A limerick came from Nantucket", "Tetrametric drum-beats thrumming, Hiawathianic rhythm."]
a = "<br>"

def breakify(x):
    b = a.join(x)
    print(b)

breakify(lines)
