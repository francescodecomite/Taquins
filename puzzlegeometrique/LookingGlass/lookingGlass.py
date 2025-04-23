TAILLE=500
from math import *

#Drop out puzzle, from Geometric puzzle designs page 44

# Taille du coté d'un carré élémentaire
cote=50
# Largeur du tour de la boite
ep=25
# valeur de l'arrondi des rectangles
rx=20
ry=20

decalx=0 # decalage du dessin pour tenir dans la feuille
decaly=0
#Dimensions de la boite.

# Entête du fichier SVG. La taille fixée produit un document carré. Pour obtenir le cadrage dans une feuille A4, le plus simple est de le faire
# à l'intérieur d'Inkscape (FIchiers>Propriétés du document)

def debut(c=TAILLE):
    entete="<svg viewBox=\"0 0 "+str(2*c)+" "+str(2*c)+"\" xmlns=\"http://www.w3.org/2000/svg\">\n"
    pied="</svg>\n"
    # Le nom du fichier SVG, n est le nombre de côtés de la boite
    image=open("dropout.svg","w")
    image.write(entete)
    return image

# Fin du fichier SVG
def fin(image):
    pied="</svg>\n"
    image.write(pied)
    image.close()


def rectangle(largeur=100,hauteur=100,percent="",transform="",rx=5,ry=5,couleur="lime"):
    s="<rect x=\""+str(0+decalx)+"\" y=\""+str(0+decaly)+"\" width=\""+str(largeur)+"\" height=\""+str(hauteur)+"\" rx =\""+str(rx)+"\" ry=\""+str(ry)+"\" fill=\"none\" stroke=\""+couleur+"\" transform=\""+transform+"\"/>\n"
    return s

def ligne(debut,fin,transform="",couleur="blue"):
     s="<line x1=\""+str(debut[0]+decalx)+"\" y1=\""+str(debut[1]+decaly)+"\" x2=\""+str(fin[0]+decalx)+"\" y2=\""+str(fin[1]+decaly)+"\" stroke=\""+couleur+"\"   transform=\""+transform+"\" />\n"
     return s
    

def equilateral(c=TAILLE,transform=""):
    hauteur=c*sqrt(3)/2
    return "<polygon points=\"0 "+str(c)+" ,"+str(c/2)+" "+str(c-hauteur)+" , "+str(c)+" "+str(c)+"\" fill=\"none\" stroke=\"red\" transform="+transform+"/>\n"

def cercle(cx,cy,rayon,couleur="blue"):
    return "<circle cx=\""+str(cx+decalx)+"\" cy=\""+str(cy+decaly)+"\"  r=\""+str(rayon)+"\"  fill=\"none\" stroke=\""+couleur+"\"/>\n"

    




if __name__=="__main__":
  
    
    image=debut(c=TAILLE)
    # les quatre trous de vis
    trou=(ep/5)/1.21
    image.write(cercle(ep+cote/2,ep/2,trou))
    image.write(cercle(ep+3.5*cote,ep/2,trou))
    image.write(cercle(ep+cote/2,3.5*cote+ep/2,trou))
    image.write(cercle(ep+3.5*cote,3.5*cote+ep/2,trou))
    # Le dessus en plexi
    image.write(rectangle(largeur=4*cote+2*ep,hauteur=3*cote+2*ep,rx=rx,ry=ry))
    image.write(cercle(ep+cote/2,ep+1.5*cote,cote/2))
    # l'étage du milieu (y compris les pentominos)
    decalx=4*cote+2*ep+5
    #bord exterieur (bords arrondis)
    image.write(rectangle(largeur=4*cote+2*ep,hauteur=3*cote+2*ep,rx=rx,ry=ry))
    image.write(cercle(ep+cote/2,ep/2,trou))
    image.write(cercle(ep+3.5*cote,ep/2,trou))
    image.write(cercle(ep+cote/2,3.5*cote+ep/2,trou))
    image.write(cercle(ep+3.5*cote,3.5*cote+ep/2,trou))
    # rectangle interieur (bords droits)
    decalx+=ep
    decaly=ep
    image.write(rectangle(largeur=4*cote,hauteur=3*cote,rx=0,ry=0,couleur="blue"))
    # les lignes de découpe des pièces internes mobiles
    image.write(ligne((cote,0),(cote,3*cote+0)))
    image.write(ligne((2*cote,0),(2*cote,3*cote+0)))
    image.write(ligne((3*cote,cote),(3*cote,3*cote+0)))
    image.write(ligne((cote,cote),(4*cote,cote)))
    # le fond
    decalx=2*(4*cote+2*ep+5)
    decaly=0
    image.write(cercle(ep+cote/2,ep/2,trou))
    image.write(cercle(ep+3.5*cote,ep/2,trou))
    image.write(cercle(ep+cote/2,3.5*cote+ep/2,trou))
    image.write(cercle(ep+3.5*cote,3.5*cote+ep/2,trou))
    image.write(rectangle(largeur=4*cote+2*ep,hauteur=3*cote+2*ep,rx=rx,ry=ry))
    # le cercle au fond
    image.write(cercle(ep+cote/2+3*cote,ep+1.5*cote,cote/2))
    fin(image)

    
    
