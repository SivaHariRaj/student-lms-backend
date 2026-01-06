from flask import Blueprint, jsonify
from data.courses import courses
from utils.logger import logger

courses_bp = Blueprint("courses", __name__)

@courses_bp.route("/courses")
def get_courses():
    logger.info("Fetching all courses")
    return jsonify(courses)

@courses_bp.route("/courses/<course_id>")
def get_course_by_id(course_id):
    for course in courses:
        if course["courseId"] == course_id:
            return jsonify(course)
    return jsonify({"error": "Course not found"}), 404
