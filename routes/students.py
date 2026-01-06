from flask import Blueprint, jsonify
from data.students import students
from utils.logger import logger

students_bp = Blueprint("students", __name__)

@students_bp.route("/students")
def get_students():
    logger.info("Fetching all students")
    return jsonify(students)

@students_bp.route("/students/<student_id>")
def get_student_by_id(student_id):
    for student in students:
        if student["studentId"] == student_id:
            return jsonify(student)
    return jsonify({"error": "Student not found"}), 404
