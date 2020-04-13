from odoo import models, fields, api


class StudentDetails(models.Model):
    _name = 'student.details'
    _rec_name = 'name'
    __description = 'Detail of Students'

    name = fields.Char(string="Student Name")
    DOB = fields.Date(string="Date Of Birth", required=False)
    age = fields.Char(string="age", required=False, compute="_calculate_age")
    standard = fields.Integer(string="Standard", required=False)
    division = fields.Integer(string="Division", required=False)
    father = fields.Char(string="Father Name", required=False)
    mother = fields.Char(string="Mother name", required=False)
    subjects = fields.Many2one('school.subject', string="Subject", required=False)
    marks_line = fields.One2many('subject.marks.line', 'sub_marks', string="Subject Marks", required=False)

    state = fields.Selection([("draft", "draft"), ("confirm", "confirm")], default="draft", string="Status",
                              required=False)
    state = fields.Selection([("draft", "draft"), ("confirm", "confirm")], default="draft", string="Status",
                              readonly=False)
    
    @api.multi
    def confirm_enrollment(self):
         for record in self:
                record.state = "confirm"
                
    @api.depends('DOB')
    def _calculate_age(self):
        for record in self:
            if record.DOB:
                today = fields.date.today()
                dob_obj = record.DOB
                record.age = relativedelta(today, dob_obj).years


class SchoolSubject(models.Model):
    _name = 'school.subject'
    _rec_name = 'name'

    name = fields.Char(string="Subjects", required=False)


class SubjectMarksLine(models.Model):
    _name = 'subject.marks.line'
    _rec_name = 'name'

    name = fields.Char(string="Name", required=False)
    subjects = fields.Many2one('school.subject', string="Subject", required=False)
    marks = fields.Float(string="Marks", required=False)
    sub_marks = fields.Many2one("student.details", Marks="Marks", required=False)


 class InheritedSaleOrder(models.Model):
     _inherit = "sale.order"

     x_field = fields.Char(string="X FIELD", required=False)
