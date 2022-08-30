from odoo import models, fields, api
from odoo.exceptions import ValidationError


class Student(models.Model):
    _name = 'student.student'
    _description = 'student.student'

    student_id = fields.Char('ID', required=True)
    student_name = fields.Char('Name')
    student_dob = fields.Date('Date of birth')
    student_poo = fields.Char('Place of origin')
    student_score = fields.Float('Score', digits=0)
    student_sex = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female')
    ], string="Sex", default="male")
    teacher_id = fields.Many2one(
        comodel_name="teacher.teacher", string="Teacher Id")
    student_subject_ids = fields.Many2many(
        "subject.subject", "student_id", "student_id", string="Learn")
    status = fields.Char(compute="_computed_status")

    student_stupid = fields.Char("You ar stupid", default="Stupid")
    _sql_constraints = [
        ('check_student_score', 'CHECK(student_score >= 0 AND student_score <= 4)',
         'The score should be from 0 to 4!'),
        ('unique_student_id', 'UNIQUE(student_id)', 'The Id should be unique'),
    ]

    @api.constrains('student_dob')
    def _check_date_student_dob(self):
        for record in self:
            if record.student_dob > fields.Date.today():
                raise ValidationError("The date is invalid????")


    @api.depends("student_score")
    def _computed_status(self):
        for record in self:
            if record.student_score < 2:
                record.status = "Fail"
            elif record.student_score < 2.5:
                record.status = "Ordinary"
            elif record.student_score < 3:
                record.status = "Average Good"
            elif record.student_score < 3.2:
                record.status = "Good"
            elif record.student_score < 3.5:
                record.status = "Very Good"
            else:
                record.status = "Excellent"

    def set_stupid(self):
        for record in self:
            record.student_stupid = "Stupid"
        return {
            'effect': {
                'fadeout': 'slow',
                'message': 'You are stupid',
                'type': 'rainbow_man',
            }
        }

    def set_smart(self):
        for record in self:
            record.student_stupid = "Smart"
        return {
            'effect': {
                'fadeout': 'slow',
                'message': 'You are smart',
                'type': 'rainbow_man',
            }
        }
