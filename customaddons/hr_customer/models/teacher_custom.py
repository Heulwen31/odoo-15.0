from odoo import models, fields


class TeacherCustom(models.Model):
    _name = "teacher.teacher"
    _inherit = "teacher.teacher"
    _description = "Teacher"

    image = fields.Binary(string='Small-sized image', attachment=True)

    # def name_get(self):
    #     result = []
    #     for record in self:
    #         result.append((record.id, record.teacher_name))
    #     return result
