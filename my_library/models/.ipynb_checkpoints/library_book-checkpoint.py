from odoo import models, fields


class TestModule(models.Model):
    _name = 'test.module'
    _description = 'Test Module'

    name = fields.Char('Title', required=True)
    date_release = fields.Date('Release Date')
    author_ids = fields.Many2many('res.partner', string='Authors')