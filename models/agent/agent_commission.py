from odoo import models, fields, api
import logging

_logger = logging.getLogger(__name__)


class Commission(models.Model):
    _name = "assurance.commission"

    name = fields.Char(string="Nom", help_text="Merci de renseigner le nom de la commission")