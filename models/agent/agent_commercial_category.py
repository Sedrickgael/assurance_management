from odoo import models, fields, api
import logging

_logger = logging.getLogger(__name__)


class CategorieCommerciale(models.Model):
    _inherit = "assurance.categorie.commerciale"

    name = fields.Char(string="Nom",
                       help_text="Merci de renseigner le nom de la catégorie")
    description = fields.Text(string='Description',
                              help_text="Merci de décrire la catégorie ex.\
                               Commercial avec plus de 5 ans d'expèrience")
    status = fields.Boolean(string="Status",
                            help_text="Merci de cochez cette case si la catégorie doit être visible\
                             dans la liste déroulante du formulaire des commerciaux")