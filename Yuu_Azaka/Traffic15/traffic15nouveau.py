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
    image=open("traffic15.svg","w")
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
    return "<polygon points=\"0 "+str(c)+" ,"+str(c/2)+" "+str(c-hauteur)+" , "+str(c)+" "+str(c)+"\" fill=\"none\" stroke=\"blue\" transform="+transform+"/>\n"

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
    s="<!-- Les bords intérieurs et exterieurs / -->\n"
    image.write(s)
    #bord exterieur (bords arrondis)
    image.write(rectangle(largeur=3*cote+2*ep,hauteur=3*cote+2*ep,rx=rx,ry=ry))
    """
    # L'emplacement pour ranger la pièce en trop
    decaly=1.5*cote+ep
    decalx=-2.25*cote
    image.write(ligne((0*cote,0*cote),(0*cote,3*cote)))
    image.write(ligne((0*cote,0*cote),(2*cote,0*cote)))
    image.write(ligne((0*cote,3*cote),(2*cote,3*cote)))
    image.write(ligne((2*cote,3*cote),(2*cote,0*cote)))
    image.write(arc4(cote,0))
    decalx=0
    decaly=0
    """
    # rectangle interieur (deux bords arrondis)
    decalx=ep
    decaly=ep
    image.write(ligne((0*cote,0*cote),(2.5*cote,0*cote),couleur="lime"))
    s="<path d=\" M "+str(2.5*cote+decalx)+" "+str(decaly)+" \n a "+str(cote/2)+" "+str(cote/2)+" 0 0 1 "+str(cote/2)+" "+str(cote/2)+"\" fill=\"none\" stroke=\"lime\"/>\n"
    image.write(s)
    #image.write(arc4(2.5*cote,0,couleur="lime"))
    image.write(ligne((3*cote,0.5*cote),(3*cote,3*cote),couleur="lime"))
    image.write(ligne((3*cote,3*cote),(0.5*cote,3*cote),couleur="lime"))
    #image.write(arc1(0*cote,2*cote,couleur="lime"))
    s="<path d=\" M "+str(decalx)+" "+str(decaly+2.5*cote)+" \n a "+str(cote/2)+" "+str(cote/2)+" 0 0 0 "+str(cote/2)+" "+str(cote/2)+"\" fill=\"none\" stroke=\"lime\"/>\n"
    image.write(s)
    image.write(ligne((0*cote,2.5*cote),(0*cote,0*cote),couleur="lime"))
    petitRayon=3

    """
    On va dessiner chacune des pièces comme un chemin, et on les place comme sur la photo de départ
    On part d'en bas à gauche
    """
    # dimensions paramétrables des divers objets
    # Largeur du corps des flèches
    largeurFleche=cote/5
    longueurFleche=5*cote/12
    # centrage de la hampe de la flèche
    u=(cote/2)-2*largeurFleche
   
    largeurPointe=largeurFleche+2*u
    theta=pi/6
    largeurPointeCos=largeurPointe*cos(theta)
    largeurPointeSin=largeurPointe*sin(theta)
    
   
    
    decalx=ep
    decaly=ep
    s="<!-- Pièce en haut à gauche / -->\n"
    image.write(s)
    s="<!-- Pièce en haut à gauche ligne du bas/ -->\n"
    image.write(s)
    # Piece 1 (en haut à gauche)
    
    
    # Hampe coudée
    s="<!-- Pièce en haut à gauche la hampe de flèche tordue/ -->\n"
    image.write(s)
    pc1=cote/4
    gc1=pc1+largeurFleche*tan(pi/6)
    image.write(ligne(((cote-largeurFleche)/2,cote),(cote/2-largeurFleche/2,cote-pc1-petitRayon),couleur="blue"))# garde
    image.write(ligne(((cote+largeurFleche)/2,cote),(cote/2+largeurFleche/2,cote-gc1-petitRayon),couleur="blue"))# garde
    # Les deux virages (pas le bon angle)
    s="<path d=\" M  "+str(cote/2-largeurFleche/2+decalx)+ " "+str(cote-pc1-petitRayon+decaly)+ " a "+str(petitRayon)+" "+str(petitRayon)+" 1 0 0 "+ str(-petitRayon)+" "+str(-petitRayon)+ "\" stroke=\"blue\"  fill=\"none\" />\n"
    image.write(s)
    s="<path d=\" M  "+str(cote/2+largeurFleche/2+decalx)+ " "+str(cote-gc1-petitRayon+decaly)+ " a "+str(petitRayon)+" "+str(petitRayon)+" 1 0 0 "+ str(-petitRayon)+" "+str(-petitRayon)+ "\" stroke=\"blue\"  fill=\"none\" />\n"
    image.write(s)
    
    # fin de la hampe
   

    
   
    s="<!-- Pièce en haut à gauche le grand coin arrondi à gauche/ -->\n"
    image.write(s)
    s="<path d=\" M  "+str(decalx)+ " "+str(decaly+cote/2)+ " a "+str(cote/2)+" "+str(cote/2)+" 0 0 1 "+ str(cote/2)+" "+str(-cote/2)+ "\" stroke=\"blue\"  fill=\"none\" />\n"
    image.write(s)

    # Piece du milieu en haut
    s="<!-- Pièce en haut au milieu/ -->\n"
    image.write(s)
    
    image.write(ligne((cote+cote/2-largeurFleche/2,0),(cote+cote/2-largeurFleche/2,gc1 ),couleur="blue"))# garde
    image.write(ligne((cote+cote/2+largeurFleche/2,0),(cote+cote/2+largeurFleche/2,pc1 ),couleur="blue")) # garde
    
   
    # Piece en haut à droite
   

    # Piece du milieu à gauche
    s="<path d=\" M  "+str(decalx)+ " "+str(decaly+cote+cote/2)+ " a "+str(cote/2)+" "+str(cote/2)+" 0 0 1 "+ str(cote/2)+" "+str(-cote/2)+ "\" stroke=\"blue\"  fill=\"none\" />\n"
    image.write(s)

    #Changement d'avis : on va découper les grandes lignes interieures, bien mettre tous les coins
    #et on peaufinea les trous à la fin
    """
    for i in range(2):
        image.write(ligne(((i+1)*cote,0),((i+1)*cote,3*cote),couleur="blue"))
        image.write(ligne((0,(i+1)*cote),(3*cote,(i+1)*cote),couleur="blue"))
    """
    #image.write(ligne((cote,0),(cote,3*cote),couleur="blue"))
    image.write(ligne((cote,0),(cote,largeurFleche),couleur="blue"))
    image.write(ligne((cote,2*largeurFleche),(cote,cote+largeurFleche),couleur="blue"))
    image.write(ligne((cote,1.5*cote-u),(cote,2.5*cote+u),couleur="blue"))
    image.write(ligne((cote,2.5*cote+largeurFleche+u),(cote,3*cote),couleur="blue"))

    #image.write(ligne((2*cote,0),(2*cote,3*cote),couleur="blue"))
    image.write(ligne((2*cote,0),(2*cote,2.5*cote-largeurFleche/2),couleur="blue"))
    image.write(ligne((2*cote,3*cote),(2*cote,2.5*cote+largeurFleche/2),couleur="blue"))

    image.write(ligne((0,cote),(3*cote,cote),couleur="blue"))
    image.write(ligne((0,2*cote),(2.5*cote-largeurFleche/2,2*cote),couleur="blue"))
    image.write(ligne((3*cote,2*cote),(2.5*cote+largeurFleche/2,2*cote),couleur="blue"))


    
    # Les coins arrondis
    
    # debut coherent
    
    s="<path d=\" M  "+str(decalx)+ " "+str(2*cote+decaly-petitRayon)+ " a "+str(petitRayon)+" "+str(petitRayon)+" 0 0 0 "+ str(petitRayon)+" "+str(petitRayon)+ "\" stroke=\"blue\"  fill=\"none\" />\n"
    image.write(s)
    s="<path d=\" M  "+str(cote+decalx)+ " "+str(2*cote+decaly-petitRayon)+ " a "+str(petitRayon)+" "+str(petitRayon)+" 0 0 0 "+ str(petitRayon)+" "+str(petitRayon)+ "\" stroke=\"blue\"  fill=\"none\" />\n"
    image.write(s)
    s="<path d=\" M  "+str(2*cote+decalx)+ " "+str(2*cote+decaly-petitRayon)+ " a "+str(petitRayon)+" "+str(petitRayon)+" 0 0 0 "+ str(petitRayon)+" "+str(petitRayon)+ "\" stroke=\"blue\"  fill=\"none\" />\n"
    image.write(s)
    
 
    s="<path d=\" M  "+str(decalx)+ " "+str(cote+decaly-petitRayon)+ " a "+str(petitRayon)+" "+str(petitRayon)+" 0 0 0 "+ str(petitRayon)+" "+str(petitRayon)+ "\" stroke=\"blue\"  fill=\"none\" />\n"
    image.write(s)
    s="<path d=\" M  "+str(cote+decalx)+ " "+str(cote+decaly-petitRayon)+ " a "+str(petitRayon)+" "+str(petitRayon)+" 0 0 0 "+ str(petitRayon)+" "+str(petitRayon)+ "\" stroke=\"blue\"  fill=\"none\" />\n"
    image.write(s)
    s="<path d=\" M  "+str(2*cote+decalx)+ " "+str(cote+decaly-petitRayon)+ " a "+str(petitRayon)+" "+str(petitRayon)+" 0 0 0 "+ str(petitRayon)+" "+str(petitRayon)+ "\" stroke=\"blue\"  fill=\"none\" />\n"
    image.write(s)

    s="<path d=\" M  "+str(cote+decalx)+ " "+str(3*cote+decaly-petitRayon)+ " a "+str(petitRayon)+" "+str(petitRayon)+" 0 0 0 "+ str(petitRayon)+" "+str(petitRayon)+ "\" stroke=\"blue\"  fill=\"none\" />\n"
    image.write(s)
    s="<path d=\" M  "+str(2*cote+decalx)+ " "+str(3*cote+decaly-petitRayon)+ " a "+str(petitRayon)+" "+str(petitRayon)+" 0 0 0 "+ str(petitRayon)+" "+str(petitRayon)+ "\" stroke=\"blue\"  fill=\"none\" />\n"
    image.write(s)

    
    
    s="<path d=\" M  "+str(decalx+cote-petitRayon)+ " "+str(cote+decaly)+ " a "+str(petitRayon)+" "+str(petitRayon)+" 0 0 0 "+ str(petitRayon)+" "+str(-petitRayon)+ "\" stroke=\"blue\"  fill=\"none\" />\n"
    image.write(s)
    s="<path d=\" M  "+str(decalx+cote-petitRayon)+ " "+str(2*cote+decaly)+ " a "+str(petitRayon)+" "+str(petitRayon)+" 0 0 0 "+ str(petitRayon)+" "+str(-petitRayon)+ "\" stroke=\"blue\"  fill=\"none\" />\n"
    image.write(s)
    s="<path d=\" M  "+str(decalx+cote-petitRayon)+ " "+str(3*cote+decaly)+ " a "+str(petitRayon)+" "+str(petitRayon)+" 0 0 0 "+ str(petitRayon)+" "+str(-petitRayon)+ "\" stroke=\"blue\"  fill=\"none\" />\n"
    image.write(s)


    
    s="<path d=\" M  "+str(decalx+2*cote-petitRayon)+ " "+str(cote+decaly)+ " a "+str(petitRayon)+" "+str(petitRayon)+" 0 0 0 "+ str(petitRayon)+" "+str(-petitRayon)+ "\" stroke=\"blue\"  fill=\"none\" />\n"
    image.write(s)
    s="<path d=\" M  "+str(decalx+2*cote-petitRayon)+ " "+str(2*cote+decaly)+ " a "+str(petitRayon)+" "+str(petitRayon)+" 0 0 0 "+ str(petitRayon)+" "+str(-petitRayon)+ "\" stroke=\"blue\"  fill=\"none\" />\n"
    image.write(s)
    s="<path d=\" M  "+str(decalx+2*cote-petitRayon)+ " "+str(3*cote+decaly)+ " a "+str(petitRayon)+" "+str(petitRayon)+" 0 0 0 "+ str(petitRayon)+" "+str(-petitRayon)+ "\" stroke=\"blue\"  fill=\"none\" />\n"
    image.write(s)

    s="<path d=\" M  "+str(decalx+3*cote-petitRayon)+ " "+str(cote+decaly)+ " a "+str(petitRayon)+" "+str(petitRayon)+" 0 0 0 "+ str(petitRayon)+" "+str(-petitRayon)+ "\" stroke=\"blue\"  fill=\"none\" />\n"
    image.write(s)
    s="<path d=\" M  "+str(decalx+3*cote-petitRayon)+ " "+str(2*cote+decaly)+ " a "+str(petitRayon)+" "+str(petitRayon)+" 0 0 0 "+ str(petitRayon)+" "+str(-petitRayon)+ "\" stroke=\"blue\"  fill=\"none\" />\n"
    image.write(s)
    
    s="<path d=\" M  "+str(decalx+3*cote-petitRayon)+ " "+str(3*cote+decaly)+ " a "+str(petitRayon)+" "+str(petitRayon)+" 0 0 0 "+ str(petitRayon)+" "+str(-petitRayon)+ "\" stroke=\"blue\"  fill=\"none\" />\n"
    image.write(s)
    
    
    s="<path d=\" M  "+str(decalx+cote-petitRayon)+ " "+str(decaly)+ " a "+str(petitRayon)+" "+str(petitRayon)+" 0 0 1 "+ str(petitRayon)+" "+str(petitRayon)+ "\" stroke=\"blue\"  fill=\"none\" />\n"
    image.write(s)
    s="<path d=\" M  "+str(decalx+cote-petitRayon)+ " "+str(cote+decaly)+ " a "+str(petitRayon)+" "+str(petitRayon)+" 0 0 1 "+ str(petitRayon)+" "+str(petitRayon)+ "\" stroke=\"blue\"  fill=\"none\" />\n"
    image.write(s)
    s="<path d=\" M  "+str(decalx+cote-petitRayon)+ " "+str(2*cote+decaly)+ " a "+str(petitRayon)+" "+str(petitRayon)+" 0 0 1 "+ str(petitRayon)+" "+str(petitRayon)+ "\" stroke=\"blue\"  fill=\"none\" />\n"
    image.write(s)

    s="<path d=\" M  "+str(decalx+2*cote-petitRayon)+ " "+str(decaly)+ " a "+str(petitRayon)+" "+str(petitRayon)+" 0 0 1 "+ str(petitRayon)+" "+str(petitRayon)+ "\" stroke=\"blue\"  fill=\"none\" />\n"
    image.write(s)
    s="<path d=\" M  "+str(decalx+2*cote-petitRayon)+ " "+str(cote+decaly)+ " a "+str(petitRayon)+" "+str(petitRayon)+" 0 0 1 "+ str(petitRayon)+" "+str(petitRayon)+ "\" stroke=\"blue\"  fill=\"none\" />\n"
    image.write(s)
    s="<path d=\" M  "+str(decalx+2*cote-petitRayon)+ " "+str(2*cote+decaly)+ " a "+str(petitRayon)+" "+str(petitRayon)+" 0 0 1 "+ str(petitRayon)+" "+str(petitRayon)+ "\" stroke=\"blue\"  fill=\"none\" />\n"
    image.write(s)

    s="<path d=\" M  "+str(decalx+3*cote-petitRayon)+ " "+str(cote+decaly)+ " a "+str(petitRayon)+" "+str(petitRayon)+" 0 0 1 "+ str(petitRayon)+" "+str(petitRayon)+ "\" stroke=\"blue\"  fill=\"none\" />\n"
    image.write(s)
    s="<path d=\" M  "+str(decalx+3*cote-petitRayon)+ " "+str(2*cote+decaly)+ " a "+str(petitRayon)+" "+str(petitRayon)+" 0 0 1 "+ str(petitRayon)+" "+str(petitRayon)+ "\" stroke=\"blue\"  fill=\"none\" />\n"
    image.write(s)

    
   
    s="<path d=\" M  "+str(decalx+2*cote-petitRayon)+ " "+str(1*cote+decaly)+ " a "+str(petitRayon)+" "+str(petitRayon)+" 0 0 1 "+ str(petitRayon)+" "+str(petitRayon)+ "\" stroke=\"blue\"  fill=\"none\" />\n"
    image.write(s)
    s="<path d=\" M  "+str(decalx+2*cote-petitRayon)+ " "+str(2*cote+decaly)+ " a "+str(petitRayon)+" "+str(petitRayon)+" 0 0 1 "+ str(petitRayon)+" "+str(petitRayon)+ "\" stroke=\"blue\"  fill=\"none\" />\n"
    image.write(s)
    
   
        
    
    s="<path d=\" M  "+str(decalx+2*cote)+ " "+str(2*cote+decaly+petitRayon)+ " a "+str(petitRayon)+" "+str(petitRayon)+" 0 0 1 "+ str(petitRayon)+" "+str(-petitRayon)+ "\" stroke=\"blue\"  fill=\"none\" />\n"
    image.write(s)
    s="<path d=\" M  "+str(decalx+2*cote)+ " "+str(1*cote+decaly+petitRayon)+ " a "+str(petitRayon)+" "+str(petitRayon)+" 0 0 1 "+ str(petitRayon)+" "+str(-petitRayon)+ "\" stroke=\"blue\"  fill=\"none\" />\n"
    image.write(s)
    s="<path d=\" M  "+str(decalx+2*cote)+ " "+str(0*cote+decaly+petitRayon)+ " a "+str(petitRayon)+" "+str(petitRayon)+" 0 0 1 "+ str(petitRayon)+" "+str(-petitRayon)+ "\" stroke=\"blue\"  fill=\"none\" />\n"
    image.write(s)
   
    s="<path d=\" M  "+str(decalx+1*cote)+ " "+str(2*cote+decaly+petitRayon)+ " a "+str(petitRayon)+" "+str(petitRayon)+" 0 0 1 "+ str(petitRayon)+" "+str(-petitRayon)+ "\" stroke=\"blue\"  fill=\"none\" />\n"
    image.write(s)
    s="<path d=\" M  "+str(decalx+1*cote)+ " "+str(1*cote+decaly+petitRayon)+ " a "+str(petitRayon)+" "+str(petitRayon)+" 0 0 1 "+ str(petitRayon)+" "+str(-petitRayon)+ "\" stroke=\"blue\"  fill=\"none\" />\n"
    image.write(s)
    s="<path d=\" M  "+str(decalx+1*cote)+ " "+str(0*cote+decaly+petitRayon)+ " a "+str(petitRayon)+" "+str(petitRayon)+" 0 0 1 "+ str(petitRayon)+" "+str(-petitRayon)+ "\" stroke=\"blue\"  fill=\"none\" />\n"
    image.write(s)
   

    s="<path d=\" M  "+str(decalx+0*cote)+ " "+str(2*cote+decaly+petitRayon)+ " a "+str(petitRayon)+" "+str(petitRayon)+" 0 0 1 "+ str(petitRayon)+" "+str(-petitRayon)+ "\" stroke=\"blue\"  fill=\"none\" />\n"
    image.write(s)
    s="<path d=\" M  "+str(decalx+0*cote)+ " "+str(1*cote+decaly+petitRayon)+ " a "+str(petitRayon)+" "+str(petitRayon)+" 0 0 1 "+ str(petitRayon)+" "+str(-petitRayon)+ "\" stroke=\"blue\"  fill=\"none\" />\n"
    image.write(s)

    decalx=ep
    decaly=ep
    
    # Les deux corps de flèche horizontaux
    image.write(ligne((cote-longueurFleche,largeurFleche),(cote,largeurFleche)))
    image.write(ligne((cote-longueurFleche,2*largeurFleche),(cote,2*largeurFleche)))
    image.write(ligne((cote-longueurFleche,largeurFleche),(cote-longueurFleche,2*largeurFleche)))
    decalx=decalx+cote+longueurFleche
    image.write(ligne((cote-longueurFleche,largeurFleche),(cote,largeurFleche)))
    image.write(ligne((cote-longueurFleche,2*largeurFleche),(cote,2*largeurFleche)))
    image.write(ligne((cote,largeurFleche),(cote,2*largeurFleche)))
    decalx=ep
    # les deux corps de flèche verticaux
    image.write(ligne((3*cote-2*largeurFleche,cote-longueurFleche),(3*cote-2*largeurFleche,cote) ))
    image.write(ligne((3*cote-largeurFleche,cote-longueurFleche),(3*cote-largeurFleche,cote) ))
    image.write(ligne((3*cote-largeurFleche,cote-longueurFleche),(3*cote-2*largeurFleche,cote-longueurFleche) ))
    decaly=decaly+2*cote
    image.write(ligne((3*cote-2*largeurFleche,cote-longueurFleche),(3*cote-2*largeurFleche,cote) ))
    image.write(ligne((3*cote-largeurFleche,cote-longueurFleche),(3*cote-largeurFleche,cote) ))
    image.write(ligne((3*cote-largeurFleche,cote-longueurFleche),(3*cote-2*largeurFleche,cote-longueurFleche) ))
    decaly=ep

    decaly=decaly+3*cote-3*largeurFleche
    decalx=decalx+longueurFleche
    image.write(ligne((cote-longueurFleche,largeurFleche),(cote,largeurFleche)))
    image.write(ligne((cote-longueurFleche,2*largeurFleche),(cote,2*largeurFleche)))
    image.write(ligne((cote,largeurFleche),(cote,2*largeurFleche)))
    decalx=ep
    decaly=ep

    # les tetes de fleches en bord de carré
    
    image.write(ligne((cote,cote/2-largeurPointe),(cote+largeurPointeSin,1.5*largeurFleche)))
    image.write(ligne((cote,cote/2),(cote+largeurPointeSin,1.5*largeurFleche)))
   
    image.write(ligne((cote,cote+cote/2-largeurPointe),(cote+largeurPointeSin,cote+1.5*largeurFleche)))
    image.write(ligne((cote,cote+cote/2),(cote+largeurPointeSin,cote+1.5*largeurFleche)))
    # en bas a gauche
    image.write(ligne((cote,2*cote+cote/2),(cote-largeurPointeSin,3*cote-1.5*largeurFleche)))
    image.write(ligne((cote,2*cote+cote/2+largeurPointe),(cote-largeurPointeSin,3*cote-1.5*largeurFleche)))
    # Les tetes toutes seules dirigées vers le bas
    # A droite
    image.write(ligne((2.5*cote-largeurPointe/2,2*cote),(2.5*cote,2*cote+largeurPointeSin)))
    image.write(ligne((2.5*cote+largeurPointe/2,2*cote),(2.5*cote,2*cote+largeurPointeSin)))
    # A gauche bas
    image.write(ligne((0.5*cote,2*cote),(0.5*cote+largeurPointe/2,2*cote+largeurPointeSin)))
    image.write(ligne((0.5*cote+largeurPointe,2*cote),(0.5*cote+largeurPointe/2,2*cote+largeurPointeSin)))
    # A gauche haut
    image.write(ligne((0.5*cote,2*cote),(0.5*cote+largeurPointe/2,2*cote-largeurPointeSin)))
    image.write(ligne((0.5*cote+largeurPointe,2*cote),(0.5*cote+largeurPointe/2,2*cote-largeurPointeSin)))
    # La plus basse a droite
    image.write(ligne((2*cote,2.5*cote-largeurPointe/2),(2*cote+largeurPointeSin,2.5*cote)))
    image.write(ligne((2*cote+largeurPointeSin,2.5*cote),(2*cote,2.5*cote+largeurPointe/2)))
    # Les petites fleches (il y en a trois)
    petiteLongueur=cote/4
    ecart=largeurPointe-largeurFleche
    image.write(ligne((2.5*cote-largeurFleche/2,2*cote),(2.5*cote-largeurFleche/2,2*cote-petiteLongueur)))
    image.write(ligne((2.5*cote+largeurFleche/2,2*cote),(2.5*cote+largeurFleche/2,2*cote-petiteLongueur)))
    image.write(ligne((2.5*cote-largeurFleche/2,2*cote-petiteLongueur),(2.5*cote-largeurPointe/2,2*cote-petiteLongueur)))
    image.write(ligne((2.5*cote-largeurPointe/2,2*cote-petiteLongueur),(2.5*cote,2*cote-petiteLongueur-largeurPointeSin)))
    
    image.write(ligne((2.5*cote+largeurPointe/2,2*cote-petiteLongueur),(2.5*cote+largeurFleche/2,2*cote-petiteLongueur)))
    image.write(ligne((2.5*cote,2*cote-petiteLongueur-largeurPointeSin),(2.5*cote+largeurPointe/2,2*cote-petiteLongueur)))
   
    # Les deux petites fleches horizontales

    image.write(ligne((2*cote-petiteLongueur-largeurPointeSin,1.5*cote),(2*cote-petiteLongueur,1.5*cote-largeurPointe/2)))
    image.write(ligne((2*cote-petiteLongueur-largeurPointeSin,1.5*cote),(2*cote-petiteLongueur,1.5*cote+largeurPointe/2)))

    image.write(ligne((2*cote-petiteLongueur,1.5*cote-largeurFleche/2),(2*cote-petiteLongueur,1.5*cote-largeurPointe/2)))
    image.write(ligne((2*cote-petiteLongueur,1.5*cote+largeurFleche/2),(2*cote-petiteLongueur,1.5*cote+largeurPointe/2)))
    image.write(ligne((2*cote-petiteLongueur,1.5*cote+largeurFleche/2),(2*cote,1.5*cote+largeurFleche/2)))
    image.write(ligne((2*cote-petiteLongueur,1.5*cote-largeurFleche/2),(2*cote,1.5*cote-largeurFleche/2)))

    decaly+=cote
    
    image.write(ligne((2*cote-petiteLongueur-largeurPointeSin,1.5*cote),(2*cote-petiteLongueur,1.5*cote-largeurPointe/2)))
    image.write(ligne((2*cote-petiteLongueur-largeurPointeSin,1.5*cote),(2*cote-petiteLongueur,1.5*cote+largeurPointe/2)))

    image.write(ligne((2*cote-petiteLongueur,1.5*cote-largeurFleche/2),(2*cote-petiteLongueur,1.5*cote-largeurPointe/2)))
    image.write(ligne((2*cote-petiteLongueur,1.5*cote+largeurFleche/2),(2*cote-petiteLongueur,1.5*cote+largeurPointe/2)))
    image.write(ligne((2*cote-petiteLongueur,1.5*cote+largeurFleche/2),(2*cote,1.5*cote+largeurFleche/2)))
    image.write(ligne((2*cote-petiteLongueur,1.5*cote-largeurFleche/2),(2*cote,1.5*cote-largeurFleche/2)))
    decaly=ep

    """
    # les lignes de découpe des pièces internes mobiles
    image.write(arc1(50,0))

    #image.write(arc2(50,0,"blue"))
    #image.write(arc3(50,0,"lime"))
    #image.write(arc4(50,0,"orange"))
    
    image.write(ligne((2*cote,1*cote),(2*cote,5*cote)))
    image.write(arc3(cote,3*cote))
    image.write(arc3(0,4*cote))
    image.write(ligne((cote,3*cote),(2*cote,3*cote)))
    image.write(arc4(2*cote,5*cote))
    image.write(ligne((2*cote,5*cote),(4*cote,5*cote)))
    image.write(ligne((3*cote,6*cote),(3*cote,5*cote)))
    image.write(ligne((4*cote,5*cote),(4*cote,3*cote)))
    image.write(arc4(3*cote,3*cote))
    image.write(ligne((3*cote,3*cote),(3*cote,1*cote)))
    image.write(ligne((2*cote,1*cote),(3*cote,1*cote)))
    image.write(ligne((3*cote,3*cote),(4*cote,3*cote)))
    image.write(ligne((4*cote,3*cote),(4*cote,4*cote)))
    image.write(ligne((4*cote,4*cote),(5*cote,4*cote)))
    image.write(ligne((5*cote,4*cote),(5*cote,3*cote)))
    image.write(ligne((5*cote,3*cote),(6*cote,3*cote)))
    image.write(ligne((6*cote,3*cote),(6*cote,1*cote)))
    image.write(ligne((6*cote,1*cote),(5*cote,1*cote)))
    image.write(arc2(4*cote,2*cote))
    image.write(arc2(3*cote,3*cote))
    image.write(arc1(4*cote,0*cote))
    image.write(ligne((6*cote,2*cote),(7*cote,2*cote)))
    image.write(arc2(7*cote,2*cote))
    image.write(ligne((8*cote,1*cote),(9*cote,1*cote)))
    image.write(ligne((7*cote,2*cote),(7*cote,3*cote)))
    image.write(ligne((7*cote,3*cote),(6*cote,3*cote)))
    image.write(arc1(6*cote,3*cote))
    image.write(ligne((7*cote,4*cote),(8*cote,4*cote)))
    image.write(arc2(8*cote,4*cote))
    image.write(ligne((7*cote,4*cote),(7*cote,5*cote)))
    image.write(arc2(6*cote,6*cote))
    image.write(ligne((5*cote,4*cote),(7*cote,4*cote)))
    image.write(arc2(4*cote,5*cote))
    """
    fin(image)

    
    
