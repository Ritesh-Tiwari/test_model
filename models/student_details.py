from odoo import fields ,models


class StudentDetails(models.Model):
    _name = 'student.details'
    _rec_name = 'name'
    _description = 'Details of Students'

    name = fields.Char(string="Student Name")
    dob = fields.Date(string="Date Of Birth", required=False)
    age = fields.Integer(string="Age", required=False)
    standard = fields.Integer(str="Standard", required=False)
    division = fields.Integer(string="Division", required=False)
    father = fields.Char(string="Father", required=False)
    mother = fields.Char(string="Mother", required=False)
