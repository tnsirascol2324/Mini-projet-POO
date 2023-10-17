import locale 
locale.setlocale(locale.LC_TIME,"") #Pour avoir l'affichage de la date en français

import time
import datetime

liste_calendriers = []
                
class Evenement :

    """
    Crée des objets évènements qui doivent obligatoirement appartenir à un calendrier

    Création d'une instance : instance = Evenement(pnom : str, pheure_debut : int, pminute_debut : int, pjour_debut : int, pmois_debut : int, pannee_debut : int, pheure_fin : int, pminute_fin : int, pjour_fin : int, pmois_fin : int, pannee_fin : int, prappel : int, plieu : str)

    Attributs d'instance :
        nom : str, nom de l'évènement
        debut : date et heure du début de l'évènement
        fin : date et heure de la fin de l'évènement
        rappel : int, heure du rappel (nombre de minutes avant le début de l'évènement)
        lieu : str, lieu de l'évènement

    Méthodes :
        validite_jour(jour : int, mois : int, annee : int) -> bool : Vérifie que le jour existe dan le mois et l'année donnée
        afficher_debut() -> str : renvoie la date et l'heure du début de l'évènement
        afficher_fin() -> str : renvoie la date et l'heure de fin de l'évènement
        afficher_nom() -> str : renvoie le nom de l'évènement
        afficher_rappel() -> str : renvoie la valeur de l'attribut rappel
        afficher_lieu() -> str : renvoie le lieu de l'évènement
        changer_nom(nouveay_nom : str) : permet de changer le nom de l'évènement 
        changer_h_debut(heure, minute) : permet de modifier l'heure de début de l'évènement
        changer_h_fin(heure, minute) : permet de modifier l'heure de fin de l'évènement
        changer_date_début(jour : int, moi : int, annee : int) : permet de modifier la date de début de l'évènement
        changer_date_fin(jour : int, mois : int, annee : int) : permet de modifier la date de fin de l'évènement
        changer_rappel(nouveau_rappel : int) : permet de changer l'heure d'envoi du rappel
        changer_lieu(nouveau_lieu : str) : permet de changer le lieu de l'évènement
        get_rappel() : renvoie l'heure du rappel
        lancer_rappel() -> str : envoie un message de rappel 
        commencer_evenement() : envoie un message à l'heure de l'évènement

    """

    def __init__(self, pnom : str, pheure_debut : int, pminute_debut : int, pjour_debut : int, pmois_debut : int, pannee_debut : int, pheure_fin : int, pminute_fin : int, pjour_fin : int, pmois_fin : int, pannee_fin : int, prappel : int, plieu : str) -> None:
            
        if type(pnom) == str :
            self.nom = pnom
        else :
            self.nom = "Nouvel évènement"
            print("Nom invalide. Vous pouvez le redéfinir avec la méthode changer_nom.")
        
        self.debut = datetime.datetime.today()
        self.fin = datetime.datetime.today()

        if type(pheure_debut) == int and 0 <= pheure_debut < 24 :
            self.debut = self.debut.replace(hour=pheure_debut)
        else :
            print("Heure de début invalide. Vous pouvez la modifier avec la méthode changer_heure_debut.")

        if type(pminute_debut) == int and 0 <= pminute_debut < 60 :
            self.debut = self.debut.replace(minute=pminute_debut)
        else :
            print("Minute de début invalide. Vous pouvez la modifier avec la méthode changer_heure_debut.")

        if type(pmois_debut) == int and 0 < pmois_debut <= 12 :
            self.debut = self.debut.replace(day=1)
            self.debut = self.debut.replace(month=pmois_debut)
        else :
            print("Mois de début invalide. Vous pouvez le modifier avec la méthode changer_date_debut.")

        if type(pannee_debut) == int and 1 <= pannee_debut <= 9999 :
            self.debut = self.debut.replace(year=pannee_debut)
        else :
            print("Année de bébut invalide. Vous pouvez la modifier avec la méthode changer_date_debut.")

        if type(pjour_debut) == int and self.validite_jour(pjour_debut, self.debut.month, self.debut.year) == True :
            self.debut = self.debut.replace(day=pjour_debut)
        else :
            print("Jour de début invalide. Vous pouvez le modifier avec la méthode changer_date_debut.")
            if self.validite_jour(datetime.datetime.today().day, self.debut.month, self.debut.year) == True :
                self.debut = self.debut.replace(day=datetime.datetime.today().day)

        


        if type(pheure_fin) == int and 0 <= pheure_fin < 24 :
            self.fin = self.fin.replace(hour=pheure_fin)
        else :
            print("Heure de fin invalide. Vous pouvez la modifier avec la méthode changer_heure_fin.")

        if type(pminute_fin) == int and 0 <= pminute_fin < 60 :
            self.fin = self.fin.replace(minute=pminute_fin)
        else :
            print("Minute de fin invalide. Vous pouvez la modifier avec la méthode changer_heure_fin.")

        if type(pmois_fin) == int and 0 < pmois_fin <= 12 :
            self.fin = self.fin.replace(day=1)
            self.fin = self.fin.replace(month=pmois_fin)
        else :
            print("Mois de fin invalide. Vous pouvez le modifier avec la méthode changer_date_fin.")

        if type(pannee_fin) == int and 1 <= pannee_fin <= 9999 :
            self.fin = self.fin.replace(year=pannee_fin)
        else :
            print("Année de fin invalide. Vous pouvez la modifier avec la méthode changer_date_fin.")

        if type(pjour_fin) == int and self.validite_jour(pjour_fin, self.fin.month, self.fin.month) == True :
            self.fin = self.fin.replace(day=pjour_fin)
        else :
            print("Jour de fin invalide. Vous pouvez le modifier avec la méthode changer_date_fin.")
            if self.validite_jour(datetime.datetime.today().day, self.fin.month, self.fin.year) == True :
                self.fin = self.fin.replace(day=datetime.datetime.today().day) 

        if type(prappel) == int and prappel >= 0 :
            self.rappel = prappel
        else :
            print("Heure de rappel invalidde. Vous pouvez la modifier avec la méthode changer_rappel.")
            self.rappel = 0

        if type(plieu) == str :
            self.lieu = plieu
        else :
            print("Le lieu est invalide. Vous pouvez le modifier avec la méthode changer_lieu.")
            self.lieu = "lieu inconnu"

        if self.debut > self.fin :
            self.fin = self.debut.replace(hour=self.debut.hour+1)
            print("Erreur : vous avez mis la date de fin avant le début. Valeur par défaut appliquée.")
            


    def validite_jour(self, jour : int, mois : int, annee : int) -> bool :
        if mois == 1 or mois == 3 or mois == 5 or mois == 7 or mois == 8 or mois == 10 or mois == 12 :
            if 1 <= jour <= 31 and type(jour) == int :
                return True
            else :
                return False
        elif mois == 4 or mois == 6 or mois == 9 or mois == 11 :
            if 1 <= jour <= 30 and type(jour) == int :
                return True
            else :
                return False
        elif mois == 2 :
            if annee % 4 == 0 :
                if 1 <= jour <=29 and type(jour) == int :
                    return True
                else :
                    return False
            else : 
                if 1 <= jour <= 28 and type(jour) == int :
                    return True
                else :
                    return False
                
    def afficher_debut(self) -> str :
        return "L'évènement " + self.nom + " commencera le " + str(self.debut.strftime("%A %d %B %Y")) + " à " + str(self.debut.strftime("%Hh%M")) + "."
        
    def afficher_fin(self) -> str :
        return "L'évènement " + self.nom + " finira le " + str(self.fin.strftime("%A %d %B %Y")) + " à " + str(self.fin.strftime("%Hh%M")) + "."
    
    def afficher_nom(self) -> str :
        return str(self.nom)
    
    def afficher_rappel(self) -> str :
        return "Un rappel sera envoyé " + str(self.rappel) + " minutes avant l'évènement " + str(self.nom) +"."

    def afficher_lieu(self) -> str :
        return "Lévènement " + str(self.nom) + " se déroulera à " + str(self.lieu) + "."
    
    def changer_nom(self, nv_nom : str) :
        if type(nv_nom) == str :
            self.nom = nv_nom
        else :
            print("Nom invalide. Le nom n'a pas pû être changé.")

    def changer_h_debut(self, nv_heure : int, nv_minute : int) :
        ancienne_heure : self.debut
        if type(nv_heure) == int and 0 <= nv_heure < 24 :
            self.debut = self.debut.replace(hour=nv_heure)
        else :
            print("Heure invalide. L'heure n'a pas pû être changée.")
        
        if type(nv_minute) == int and 0 <= nv_minute < 60 :
            self.debut = self.debut.replace(minute=nv_minute)
        else :
            print("Minute invalide. Les minutes n'ont pas pû être changées.")
        
        if self.debut > self.fin :
            self.debut = ancienne_heure
            print("Vous avez mis la date de début avant la date de fin. L'heure de début n'a pas pû être changée.")
    
    def changer_h_fin(self, nv_heure : int, nv_minute : int) :
        ancienne_heure = self.fin
        if type(nv_heure) == int and 0 <= nv_heure < 24 :
            self.fin = self.fin.replace(hour=nv_heure)
        else :
            print("Heure invalide. L'heure n'a pas pû être changée.")
        
        if type(nv_minute) == int and 0 <= nv_minute < 60 :
            self.fin = self.fin.replace(minute=nv_minute)
        else :
            print("Minute invalide. Les minutes n'ont pas pû être changées.")

        if self.fin < self.debut :
            self.fin = ancienne_heure
            print("Vous avez mis la date de fin avant la date de début. L'heure de fin n'as pas pû être modifiée.")

    
    def changer_date_debut(self, jour : int, mois : int, annee : int) :
        ancienne_date = self.debut
        if type(annee) == int and 1 <= annee <= 9999 :
            self.debut = self.debut.replace(year=annee)
        else :
            print("Année invalide. L'année n'a pas pû être changée.")

        if type(mois) == int and 1 <= mois <= 12 :
            self.debut = self.debut.replace(month=mois)
        else :
            print("Mois invalide. Le mois n'a pas pû être changé.")

        if type(jour) == int and self.validite_jour(jour, self.debut.month, self.debut.year) == True :
            self.debut = self.debut.replace(day=jour)
        else :
            print("Jour invalide. Le jour n'a pas pû être changé.")

        if self.debut > self.fin :
            self.debut = ancienne_date
            print("Vous avez mis la date de début avant la date de fin. La date de début n'as pas pû être changée.")

    def changer_date_fin(self, jour : int, mois : int, annee : int) :
        ancienne_date = self.fin
        if type(annee) == int and 1 <= annee <= 9999 :
            self.fin = self.fin.replace(year=annee)
        else :
            print("Année invalide. L'année n'a pas pû être changée.")

        if type(mois) == int and 1 <= mois <= 12 :
            self.fin = self.fin.replace(month=mois)
        else :
            print("Mois invalide. Le mois n'a pas pû être changé.")

        if type(jour) == int and self.validite_jour(jour, self.fin.month, self.fin.year) == True :
            self.fin = self.fin.replace(day=jour)
        else :
            print("Jour invalide. Le jour n'a pas pû être changé.")

        if self.debut > self.fin :
            self.fin = ancienne_date
            print("Vous avez mis la date de début avant la date de fin. La date de fin n'as pas pû être changée.")

    def changer_rappel(self, nv_rappel : int) :
        if type(nv_rappel) == int and nv_rappel <= 0 :
            self.rappel = nv_rappel
        else :
            print("Rappel invalide. L'heure du rappel n'a pas pû être changée.")

    def changer_lieu(self, nv_lieu : str) :
        if type(nv_lieu) == str :
            self.lieu = nv_lieu
        else :
            print("Lieu invalide. Le lieu n'a pas pû être changé.")

    def get_rappel(self) :
        return self.debut - datetime.timedelta(minutes=self.rappel)
    
    def lancer_rappel(self) -> str :
        return "L'évènement " + str(self.nom) + " commencera dans " + str(self.rappel) + " minutes à " + str(self.lieu) + "."
    
    def commencer_evenement(self) -> str :
        return "L'évènement " + str(self.nom) + " commence maintenant à " + str(self.lieu) + ". Il se terminera à " + str(self.fin.strftime("%Hh%M")) + " le " + str(self.fin.strftime("%A %d %B"))


class Calendrier :

    """
    Crée des objets calendrier pouvant contenir des objets évènements
    Les calendriers doivent obligatoirement être ajoutés à la liste liste_calendriers

    Création d'une instance : instance = Calendrier(mail : str)

    Attributs d'instance :
        __calendrier : list, contient des objets de la classe évènement
        __adrese_mail : str, adresse mail à laquelle envoyer de messages

    Méthodes :
        get_events() -> lit : renvoie la liste des évènements du calendrier
        ajouter_event(evenement) : ajoute des évènements au calendrier. Les évènements doivent être des instances de la classe Evenement.
        supprimer_event(evenement) : supprime un évènement du calendrier s'il est dedans
        adresse_valide(mail) -> bool : renvoie True si la forme de l'adresse mail donnée est valide et False sinon. Permet d'implémenter une méthode pour envoyer des mails de rappel.
        get_mail() -> str : renvoie l'adresse mail
    """

    def __init__(self, pmail : str) -> None:
        self.__calendrier = []
        if self.adresse_valide(pmail) == True :
            self.__adresse_mail = pmail
        else :
            self.__adresse_mail = None 

    def get_events(self) -> list :
        return self.__calendrier

    def ajouter_event(self,evenement) :
        self.__calendrier.append(evenement)
        
    def supprimer_event(self, event) :
        if event in self.__calendrier :
            self.__calendrier.remove(event)

    def adresse_valide(self, mail : str) -> bool :
        fin_mail = False
        if type(mail) != str :
            return False
        for char in mail :
            if char == "@" :
                if fin_mail == True :
                    return False
                else :
                    fin_mail = True
                    continue
            elif char == " " :
                return False
            elif char.isdigit() :
                if fin_mail == True  :
                    return False
                else :
                    continue
            elif char.isupper() or char.islower() :
                continue
            elif char in "!#$%&'*+-/=?^_`{|}~" :
                if fin_mail == True :
                    return False
                else :
                    continue
            elif char == "." :
                continue
        if fin_mail == False :
            return False
        else :
            for i in range(1, len(mail)) :
                if mail[-i] == "." :
                    return True
                elif mail[-i] == "@" :
                    return False
                else :
                    continue
    
    def get_mail(self) -> str :
        return self.__adresse_mail


def temps() :
    """
    Permet de vérifier s'il est l'heure d'envoyer des messages de rappel ou pour le début des évènements
    """
    temps_actuel = datetime.datetime.today()
    for calendar in liste_calendriers :
        for event in calendar.get_events() :
            if event.get_rappel().date() == temps_actuel.date() and event.get_rappel().hour == temps_actuel.hour and event.get_rappel().minute == temps_actuel.minute :
                print(event.lancer_rappel())
            if event.debut.date() == temps_actuel.date() and event.debut.hour == temps_actuel.hour and event.debut.minute == temps_actuel.minute :
                print(event.commencer_evenement())


calendar =  Calendrier("")
liste_calendriers.append(calendar)
event1 = Evenement("Evenement 1", 16, 22, 8, 10, 2023, 14, 55, 9, 10, 2023, 1, "ici")
event2 = Evenement("evenement 2", 16, 25, 8, 10, 2023, 15, 12, 8, 10, 2023, 5, "ici aussi")
calendar.ajouter_event(event1)
calendar.ajouter_event(event2)



while True :
    min_actuelle = datetime.datetime.today().minute
    temps()
    time.sleep(40)
    while min_actuelle == datetime.datetime.today().minute :
        time.sleep(10)




