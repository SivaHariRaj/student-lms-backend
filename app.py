from flask import Flask, render_template
import logging

app = Flask(__name__)

# ---------------- LOGGING ----------------
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s"
)

# ---------------- ROUTES ----------------

@app.route("/")
def dashboard():
    logging.info("Dashboard page loaded")
    return render_template("index.html")


@app.route("/students")
def students():
    logging.info("Students page loaded")
    return render_template("students.html")


@app.route("/courses")
def courses():
    logging.info("Courses page loaded")
    return render_template("courses.html")


@app.route("/enrollments")
def enrollments():
    logging.info("Enrollments page loaded")
    return render_template("enrollments.html")


@app.route("/health")
def health():
    return {
        "status": "running",
        "service": "Learning Management System"
    }


# ---------------- MAIN ----------------
if __name__ == "__main__":
    logging.info("Starting LMS application")
    app.run(host="0.0.0.0", port=5000)
