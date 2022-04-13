#voiture
class Voiture(object):
    def __init__(self,marque,couleur):
        self.marque = marque
        self.couleur = couleur
        self.conducteur = 'personne'
        self.vitesse = 0
    def choisirConducteur (self,nom):
        self.conducteur = nom
        return self.conducteur
    def afficherInfos (self):
        print (self.marque,self.couleur,self.conducteur,self.vitesse)
        
maVoiture = Voiture('ford','rouge')
taVoiture = Voiture('Hyundai','blanche')
saVoiture = Voiture('Suzuki','bleue')
maVoiture.choisirConducteur('Hassan')
taVoiture.choisirConducteur('Hanane')
saVoiture.choisirConducteur('Ali')
maVoiture.afficherInfos()
taVoiture.afficherInfos()
saVoiture.afficherInfos()
