TAILLE=500
from math import *

#9 pieces : un puzzle (voir dessin dans le même répertoire)

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

# Entête du fichier SVG.
def debut(c=TAILLE):
    entete="<svg viewBox=\"0 0 "+str(2*c)+" "+str(2*c)+"\" xmlns=\"http://www.w3.org/2000/svg\">\n"
    pied="</svg>\n"
    # Le nom du fichier SVG, 
    image=open("ninesquare.svg","w")
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

def arc1(depx,depy,couleur="blue"):   
    return "<path d=\" M "+str(depx+decalx)+" "+str(depy+decaly)+" \n a "+str(cote)+" "+str(cote)+" 0 0 0 "+str(cote)+" "+str(cote)+"\" fill=\"none\" stroke=\""+couleur+"\"/>\n"

def arc2(depx,depy,couleur="blue"):   
    return "<path d=\" M "+str(depx+decalx)+" "+str(depy+decaly)+" \n a "+str(cote)+" "+str(cote)+" 0 0 1 "+str(cote)+" "+str(-cote)+"\" fill=\"none\" stroke=\""+couleur+"\"/>\n"

def arc3(depx,depy,couleur="blue"):   
    return "<path d=\" M "+str(depx+decalx)+" "+str(depy+decaly)+" \n a "+str(cote)+" "+str(cote)+" 0 0 0 "+str(cote)+" "+str(-cote)+"\" fill=\"none\" stroke=\""+couleur+"\"/>\n"

def arc4(depx,depy,couleur="blue"):   
    return "<path d=\" M "+str(depx+decalx)+" "+str(depy+decaly)+" \n a "+str(cote)+" "+str(cote)+" 0 0 1 "+str(cote)+" "+str(cote)+"\" fill=\"none\" stroke=\""+couleur+"\"/>\n"


"""
 <path
    d=" M 75 25
	a 50 50 0 0 0 50 -50
      "
    stroke="blue"
    fill="none"
    stroke-width="1"
    fill-opacity="0.5" />
"""

if __name__=="__main__":
  
    
    image=debut(c=TAILLE)
    #bord exterieur (bords arrondis)
    image.write(rectangle(largeur=9*cote+2*ep,hauteur=6*cote+2*ep,rx=rx,ry=ry))
   
    # rectangle interieur (bords droits)
    decalx+=ep
    decaly=ep
    image.write(rectangle(largeur=9*cote,hauteur=6*cote,rx=0,ry=0,couleur="blue"))
    # les lignes de découpe des pièces internes mobiles
    image.write(arc1(50,0))
    image.write(arc2(50,0,"red"))
    image.write(arc3(50,0,"lime"))
    image.write(arc4(50,0,"orange"))
    image.write(ligne((2*cote,1*cote),(2*cote,5*cote)))
    image.write(arc3(cote,3*cote))
    image.write(arc3(0,4*cote))
    image.write(ligne((cote,3*cote),(2*cote,3*cote)))
    image.write(arc4(2*cote,5*cote))
    image.write(ligne((2*cote,5*cote),(4*cote,5*cote)))
    image.write(ligne((3*cote,6*cote),(3*cote,5*cote)))
    image.write(ligne((4*cote,5*cote),(4*cote,3*cote)))
    image.write(arc4(3*cote,3*cote))
    fin(image)

    
    
