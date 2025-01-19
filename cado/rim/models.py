from django.db import models

class BaseCadorim(models.Model):
    MOIS_CHOICES = [
        ("Janvier", "Janvier"),
        ("Février", "Février"),
        ("Mars", "Mars"),
        ("Avril", "Avril"),
        ("Mai", "Mai"),
        ("Juin", "Juin"),
        ("Juillet", "Juillet"),
        ("Août", "Août"),
        ("Septembre", "Septembre"),
        ("Octobre", "Octobre"),
        ("Novembre", "Novembre"),
        ("Décembre", "Décembre"),
    ]

    mois = models.CharField(max_length=20, choices=MOIS_CHOICES, db_index=True, unique=True)  # Nom du mois
    rechargements_especes = models.IntegerField("Rechargements en Espèces Mauri Pay", default=0)
    chargement_transfert = models.IntegerField("Chargement Transfert Bancaire", default=0)
    paiement_facture = models.IntegerField("Paiement de Facture Mauri Pay", default=0)
    paiement_marchand = models.IntegerField("Paiement Marchand", default=0)
    paiement_salaire = models.IntegerField("Paiement de Salaire Mauri Pay", default=0)
    rechargements_telephoniques = models.IntegerField("Rechargements Téléphoniques Mauri Pay", default=0)
    transactions_administrations = models.IntegerField("Transactions avec les Administrations Publiques", default=0)
    transfert_p2p = models.IntegerField("Transfert Personne à Personne Mauri Pay", default=0)
    transfert_p2e = models.IntegerField("Transfert Personne à Entreprise", default=0)
    retraits_cashout_cadorim = models.IntegerField("Retraits (Cash-out) Cadorim SA", default=0)
    retraits_cashout_mauripay = models.IntegerField("Retraits (Cash-out) Mauri Pay", default=0)

    class Meta:
        abstract = True  # Indique que ce modèle est abstrait

    def __str__(self):
        return self.mois

class Volume_cadorim(BaseCadorim):
    pass

class Valeur_cadorim(BaseCadorim):
    pass



class Volume_mauripay(BaseCadorim):
    pass

class Valeur_mauripay(BaseCadorim):
    pass



class Volume_limara(BaseCadorim):
    pass

class Valeur_limara(BaseCadorim):
    pass