from datetime import datetime
from dateutil.relativedelta import relativedelta
from odoo import models, fields, api

class ImageInfo(models.Model):
    _name = 'image.info'
    _description = 'Image Information'

    name = fields.Char(string="Name")
    image = fields.Binary(string="Image")
    date_of_birth = fields.Date(string="Date of Birth")
    age = fields.Integer(string="Age", compute='_compute_age', store=True) # store=True to make the field searchable
    teacher_ids = fields.Many2many('teacher.info', 'teacher_student_rel', 'student_id', 'teacher_id', string='Teachers')
    @api.depends('date_of_birth')
    def _compute_age(self):
        for record in self:
            if record.date_of_birth:
                date_of_birth = fields.Date.from_string(record.date_of_birth)
                today = datetime.today().date()
                delta = relativedelta(today, date_of_birth)
                record.age = delta.years
