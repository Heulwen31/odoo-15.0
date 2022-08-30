from odoo import api, fields, models, tools, _

import logging
_logger = logging.getLogger(__name__)


class BatchUpdateWizard(models.TransientModel):
    _name = "student.student.batchupdate.wizard"
    _description = "Batch update for student.student model"

    name = fields.Char("Student Name", required=True)

    def multi_update(self):
        ids = self.env.context['active_ids'] # selected record ids
        my_pets = self.env["student.student"].browse(ids)
        new_data = {}
        
        if self.name:
            new_data["student_name"] = self.name
        
        my_pets.write(new_data)    