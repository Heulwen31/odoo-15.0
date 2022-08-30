from odoo import models, fields, api, _


class HrEmployee(models.Model):
    _name = 'hr.employee'
    _inherit = 'hr.employee'
    _description = 'HR Employee'

    teacher_id = fields.Many2one('teacher.teacher', string='Teacher')
    # teacher_icon = fields.Binary(
    #     related="teacher_id.image", string="Teacher Icon")
    teacher_phone = fields.Char(related="teacher_id.teacher_phone")
    teacher_name = fields.Char(related="teacher_id.teacher_name")
