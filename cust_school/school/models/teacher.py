from datetime import datetime
from dateutil.relativedelta import relativedelta
from odoo import models, fields, api

class TeacherInfo(models.Model):
    _name = 'teacher.info'
    _description = 'Teacher Info'

    name = fields.Char(string='Name')
    image = fields.Binary()
    gender = fields.Selection([
        ('male', "Male"),
        ('female', "Female")
    ])
    date_of_birth = fields.Date(string="Date of Birth", required=True)
    age = fields.Integer(string="Age", compute='_compute_age', store=True)
    designation = fields.Char(string='Designation')
    salary = fields.Integer(string="Salary")
    qualification = fields.Char(string="Qualification")
    experience = fields.Char(string="Experience")
    experience_letter = fields.Binary(string='Experience Letter', attachment=True)
    student_info_ids = fields.One2many('student.info.line', 'teacher_id', string='Student Info')

    @api.depends('date_of_birth')
    def _compute_age(self):
        for record in self:
            if record.date_of_birth:
                date_of_birth = fields.Date.from_string(record.date_of_birth)
                today = fields.Date.today()
                delta = relativedelta(today, date_of_birth)
                record.age = delta.years

class StudentInfoLine(models.Model):
    _name='student.info.line'
    _description='Student Info Line'


    student_id= fields.Many2one('student.info',string='Student')
    roll_number = fields.Char(string='Roll Number')
    teacher_id = fields.Many2one('teacher.info', string='Teacher')


