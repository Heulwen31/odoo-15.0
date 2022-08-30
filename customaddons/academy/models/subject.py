from odoo import models, fields, api


class Subject(models.Model):
    _name = "subject.subject"
    _description = "Subject"

    subject_id = fields.Char("Subject ID", required=True)
    subject_name = fields.Char("Name of subject", required=True)
    subject_credit = fields.Integer("Credit of subject", required=True)
    teacher_subject_id = fields.Many2many(
        'teacher.teacher', 'subject_id', 'subject_id', string="Teacher Subject")