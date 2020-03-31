import server.odoo.fields
import server.odoo.models


class StudentDetails(server.odoo.models.Model):
    _name = 'student_details'
    _rec_name = 'name'
    _description = 'Details of Students'

    name = server.odoo.fields.Char(string="Student Name")
    dob = server.odoo.fields.Date(string="Date Of Birth", required=False)
    age = server.odoo.fields.Integer(string="Age", required=False)
    standard = server.odoo.fields.Integer(str="Standard", required=False)
    division = server.odoo.fields.Integer(string="Division", required=False)
    father = server.odoo.fields.Char(string="Father", required=False)
    mother = server.odoo.fields.Char(string="Mother", required=False)
