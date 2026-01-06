from flask import Blueprint, jsonify
from data.enrollments import enrollments
from utils.logger import logger

enrollments_bp = Blueprint("enrollments", __name__)

@enrollments_bp.route("/enrollments")
def get_all_enrollments():
    logger.info("Fetching all enrollments")
    return jsonify(enrollments)

@enrollments_bp.route("/enrollments/student/<student_id>")
def get_enrollments_by_student(student_id):
    result = [e for e in enrollments if e["studentId"] == student_id]
    if not result:
        return jsonify({"message": "No enrollments found"}), 404
    return jsonify(result)
