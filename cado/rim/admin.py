from django.contrib import admin
from .models import Volume_cadorim, Valeur_cadorim, Volume_mauripay, Valeur_mauripay, Volume_limara, Valeur_limara

# Liste des modèles à enregistrer avec les mêmes configurations
model_configs = [
    (Volume_cadorim, 'VolumeCadorimAdmin'),
    (Valeur_cadorim, 'ValeurCadorimAdmin'),
    (Volume_mauripay, 'VolumeMauripayAdmin'),
    (Valeur_mauripay, 'ValeurMauripayAdmin'),
    (Volume_limara, 'VolumeLimaraAdmin'),
    (Valeur_limara, 'ValeurLimaraAdmin')
]

# Champs communs pour list_display et search_fields
common_list_display = ('mois', 'rechargements_especes', 'chargement_transfert', 'paiement_facture',
                       'paiement_marchand', 'paiement_salaire', 'rechargements_telephoniques',
                       'transactions_administrations', 'transfert_p2p', 'transfert_p2e',
                       'retraits_cashout_cadorim', 'retraits_cashout_mauripay')

common_search_fields = ('mois',)

# Fonction générique pour configurer les modèles
for model, admin_name in model_configs:
    admin_class = type(admin_name, (admin.ModelAdmin,), {
        'list_display': common_list_display if hasattr(model, 'rechargements_especes') else ('mois',),
        'search_fields': common_search_fields
    })
    admin.site.register(model, admin_class)
