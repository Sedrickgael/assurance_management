from odoo import models, fields, api
import logging

_logger = logging.getLogger(__name__)


class TypeDeCommission(models.Model):
    _name = "assurance.type.commission"

    name = fields.Char(string="Nom",
                       help_text="Merci de renseigner le nom du type de commission")
    code = fields.Char(string="Code")
    description = fields.Text(string='Description',
                              help_text="Merci de décrire le type de commission ex.\
                               Commission forfetaire")
    regle_de_calcul = fields.Selection([('Pourcentage', 'Pourcentage'), ('Montant Fixe', 'Montant fixe')], string="Règle de calcul")
    pourcentage = fields.Float(string="Pourcentage") # Visible si regle de calcul est Pourcentage
    montant = fields.Float(string="Montant Fixe") # Visible si regle de calcul est Montant Fixe
    status = fields.Boolean(string="Status",
                            help_text="Merci de cochez cette case si le type de commission doit être visible\
                             dans la liste déroulante du formulaire des commissions")
