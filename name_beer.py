from textblob import TextBlob 
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4, letter
import random

w, h = A4
print("Generador automático de Nombres de cerveza")
city = input("¿Cuál es tu ciudad?\t")
color = TextBlob(input("¿Cuál es tu color favorito?\t"))
animal = input("¿Qué animal te gustaría ser?\t")

rand = random.randint(0, 5)
lenguaje = ""
match rand:
    case 0:
        lenguaje = "fr"
    case 1:
        lenguaje = "en"
    case 2:
        lenguaje = "pt"
    case 3:
        lenguaje = "de"
    case 4:
        lenguaje = "it"
    case 5:
        lenguaje = "la"

color = str(color.translate(from_lang='es', to=lenguaje) )


name_beer = (city[0:3] + animal + " " + color).upper()

c = canvas.Canvas("name_beer.pdf", pagesize=A4)
c.drawString(50, h - 40, "Tu cerveza va a llamarse: " )
c.setFillColorRGB(1, 0, 0)
c.drawString(50, h - 60, name_beer)


x = 120
y = h - 45
c.setFillColorRGB(0, 0, 0)
c.drawString(30, h - 100, "Rectángulo")
c.rect(x, h - 120, 100, 50)
c.drawString(30, h - 170, "Círculo")
c.circle(170, h - 165, 20)
c.drawString(30, h - 240, "Elipse")
c.ellipse(x, y - 170, x + 100, y - 220)
c.drawString(30, h - 310, "Línea")
c.line(x, y - 260, x + 100, y - 260)

c.showPage()
c.save()