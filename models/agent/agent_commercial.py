from odoo import models, fields, api
import logging

_logger = logging.getLogger(__name__)


class Employe(models.Model):

    _inherit = "hr.employee"

    est_un_commercial = fields.Boolean(string="Est un.e commercial.e", help_text="Cochez cette case si l'employé est un.e commercial.e")
