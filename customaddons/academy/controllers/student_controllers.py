from odoo import http


class StudentController(http.Controller):
    @http.route('/student', auth='user')
    def welcome(self):
        return "Welcome Odoo!:))"

    @http.route('/student/all', auth="public")
    def all_student_information(self):
        # noinspection PyBroadException
        try:
            student_information = http.request.env['student.student'].search([])
        except:
            return "<h1>Can't get information student</h1>"
        output = "<h1>Student Name</h1><ul>"
        for information in student_information:
            output += '<li>' + information['student_name'] + '</li>'
        output += '</ul>'
        return output

    @http.route('/student/field', auth="public")
    def detail_field_request(self):
        return http.request.render('academy.field')

    @http.route('/student/required', auth="public", methods=["GET"])
    def detail_student_information(self):
        kwargs = ["student_name", "student_id", "student_score", "student_sex"]
        # noinspection PyBroadException
        try:
            student_information = http.request.env['student.student'].search([])
        except:
            return "<h1>Can't get information student</h1>"
        output = "<h1>Student Name</h1><ul>"
        for information in student_information:
            for field in kwargs:
                output += '<li>' + str(information[field]) + '</li>'
            output += "<h1>Student Name</h1>"
        output += '</ul>'
        return output
