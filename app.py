from flask import Flask, render_template, request, jsonify
import smtplib
from email.message import EmailMessage
import os

app = Flask(__name__)

SENDER_EMAIL = "YOUR_EMAIL_ID"
APP_PASSWORD = "YOUR_16_DIGIT_APP_PASSWORD"

UPLOAD_FOLDER = "uploads"
ATTACHMENT_PATH = os.path.join(UPLOAD_FOLDER, "resume.pdf")

os.makedirs(UPLOAD_FOLDER, exist_ok=True)


@app.route("/", methods=["GET", "POST"])
def index():
    
    if request.method == "GET":
        return render_template("index.html")

    
    receiver = request.form["receiver"]
    subject = request.form["subject"]
    message = request.form["message"]

    msg = EmailMessage()
    msg["From"] = SENDER_EMAIL
    msg["To"] = receiver
    msg["Subject"] = subject
    msg.set_content(message)

    if os.path.exists(ATTACHMENT_PATH):
        with open(ATTACHMENT_PATH, "rb") as f:
            msg.add_attachment(
                f.read(),
                maintype="application",
                subtype="pdf",
                filename="resume.pdf"
            )

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(SENDER_EMAIL, APP_PASSWORD)
    server.send_message(msg)
    server.quit()

    return jsonify({"status": "success"})


@app.route("/upload", methods=["POST"])
def upload():
    file = request.files.get("pdf")

    if not file or file.filename == "":
        return jsonify({"status": "error", "message": "No file uploaded"})

    file.save(ATTACHMENT_PATH)

    return jsonify({"status": "success", "message": "PDF updated successfully"})


if __name__ == "__main__":
    app.run(debug=True)
