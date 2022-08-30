from odoo import models, fields, api, _


class Teacher(models.Model):
    _name = "teacher.teacher"
    _description = "teacher.teacher"
    _rec_name = "teacher_id"

    # teacher_id = fields.Char("Teacher ID", required=True, )
    teacher_name = fields.Char("Name", required=True)
    teacher_dob = fields.Date("Date of birth")
    teacher_poo = fields.Char("Place of origin")
    teacher_phone = fields.Char("Phone number")
    teacher_id = fields.Char(string="ID", required=True, copy=False, readonly=True,
                                    default=lambda self: _('New'))
    teacher_sex = fields.Selection([
        ('male', "Male"),
        ('female', 'Female')
    ], string="Sex", default="male")
    teacher_avatar = fields.Binary(string="Avatar")
    _sql_constraints = [
        ('unique_teacher_id', 'UNIQUE(teacher_id)', 'The Id should be unique'),
    ]

    # sequence
    @api.model
    def create(self, vals_list):
        if vals_list.get('teacher_id', _('New')) == _('New'):
            vals_list['teacher_id'] = self.env['ir.sequence'].next_by_code('teacher.teacher') or _('New')
        res = super(Teacher, self).create(vals_list)
        return res