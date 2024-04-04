from datetime import datetime
from dateutil.relativedelta import relativedelta
from odoo import models, fields, api


class StudentInfo(models.Model):
    _name = "student.info"
    _description = "Student"

    course_name=fields.Char(string="course_name")
    qualification = fields.Char(string="qualification")
    image=fields.Binary(string="Image")
    name = fields.Char(string="Name")
    date_of_birth = fields.Date(string="date_of_birth", required=True)
    age = fields.Integer(string="Age", compute='_compute_age', store=True)
    gender = fields.Selection([
        ('male', "Male"),
        ('female', "Female")])
    percentage = fields.Float(string="Percentage")
    is_fees_paid = fields.Boolean(string="Fees paid")
    address=fields.Char(string="address")
    Education_document=fields.Binary(string='Education document', attachment=True)
    commented_by_teacher=fields.Char(string="commented by teacher ")
    teacher_id = fields.Many2one('teacher.info', string='Teacher')

# <------------------age calculator logic-------------------------------------------->

    @api.depends('date_of_birth')
    def _compute_age(self):
        for record in self:
            if record.date_of_birth:
                date_of_birth = fields.Date.from_string(record.date_of_birth)
                today = datetime.today().date()
                delta = relativedelta(today, date_of_birth)
                record.age = delta.years
