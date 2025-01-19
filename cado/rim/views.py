from django.shortcuts import render
from .models import *

def extract_data(objects):
    """ Fonction pour extraire les données des objets et éviter la redondance. """
    return {
        "rechargements_especes": [obj.rechargements_especes for obj in objects],
        "chargement_transfert": [obj.chargement_transfert for obj in objects],
        "paiement_facture": [obj.paiement_facture for obj in objects],
        "paiement_marchand": [obj.paiement_marchand for obj in objects],
        "paiement_salaire": [obj.paiement_salaire for obj in objects],
        "rechargements_telephoniques": [obj.rechargements_telephoniques for obj in objects],
        "transactions_administrations": [obj.transactions_administrations for obj in objects],
        "transfert_p2p": [obj.transfert_p2p for obj in objects],
        "transfert_p2e": [obj.transfert_p2e for obj in objects],
        "retraits_cashout_cadorim": [obj.retraits_cashout_cadorim for obj in objects],
        "retraits_cashout_mauripay": [obj.retraits_cashout_mauripay for obj in objects],
    }

# Dictionnaire de conversion des mois en texte
mois_mapping = {
    "01": "Janvier", "02": "Février", "03": "Mars", "04": "Avril",
    "05": "Mai", "06": "Juin", "07": "Juillet", "08": "Août",
    "09": "Septembre", "10": "Octobre", "11": "Novembre", "12": "Décembre"
}

# Liste des mois pour le tri
ordre_mois = list(mois_mapping.values())

def analyse_graphique(request):
    # Récupération des filtres
    start_month = request.GET.get('startMonth')
    end_month = request.GET.get('endMonth')

    # Récupération des données depuis la base de données
    volumes = Volume_cadorim.objects.all()
    valeurs = Valeur_cadorim.objects.all()
    volumem = Volume_mauripay.objects.all()
    valeurm = Valeur_mauripay.objects.all()
    volumel = Volume_limara.objects.all()
    valeurl = Valeur_limara.objects.all()

    # Appliquer les filtres si définis
    if start_month and end_month:
        volumes = volumes.filter(mois__gte=start_month, mois__lte=end_month)
        valeurs = valeurs.filter(mois__gte=start_month, mois__lte=end_month)
        volumem = volumem.filter(mois__gte=start_month, mois__lte=end_month)
        valeurm = valeurm.filter(mois__gte=start_month, mois__lte=end_month)
        volumel = volumel.filter(mois__gte=start_month, mois__lte=end_month)
        valeurl = valeurl.filter(mois__gte=start_month, mois__lte=end_month)

    # Extraire les données des objets
    volume_data = extract_data(volumes)
    valeur_data = extract_data(valeurs)
    volumem_data = extract_data(volumem)
    valeurm_data = extract_data(valeurm)
    volumel_data = extract_data(volumel)
    valeurl_data = extract_data(valeurl)

    # Obtenir la liste unique des mois en format texte
    mois = sorted(set(
        [mois_mapping.get(str(volume.mois).zfill(2), volume.mois) for volume in volumes] +
        [mois_mapping.get(str(volume.mois).zfill(2), volume.mois) for volume in volumem] +
        [mois_mapping.get(str(volume.mois).zfill(2), volume.mois) for volume in volumel]
    ), key=lambda m: ordre_mois.index(m))

    context = {
        'mois': mois,
        'volume_data': volume_data,
        'valeur_data': valeur_data,
        'volumem_data': volumem_data,
        'valeurm_data': valeurm_data,
        'volumel_data': volumel_data,
        'valeurl_data': valeurl_data,
    }
    
    return render(request, 'rim/navigation.html', context)
