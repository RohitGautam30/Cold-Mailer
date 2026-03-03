🚀 Cold Mailer Platform

An automated cold email sending platform that transforms manual internship/job applications into a fast, structured, and scalable workflow.

Instead of repeatedly copying, pasting, and attaching resumes manually, this platform automates the entire outreach process with dynamic resume attachment support.

📌 Problem It Solves

Applying for internships and jobs often requires sending dozens (sometimes hundreds) of personalized emails manually. This process is:

Time-consuming

Repetitive

Error-prone

Difficult to scale

Cold Mailer eliminates this manual workflow by automating personalized email sending with resume attachments in a structured and secure way.

🛠 Tech Stack

Backend: Python, Flask

Frontend: HTML, CSS, JavaScript

Email Service: SMTP

APIs: REST APIs

Deployment: Vercel

⚙️ Features

✅ Send personalized cold emails

✅ Automatic resume (PDF) attachment

✅ Upload / Replace resume anytime

✅ Secure SMTP authentication

✅ Bulk email workflow support

✅ Simple and responsive UI

✅ Real-time status feedback

🏗 How It Works

Upload your resume (PDF format).

Enter recipient details and message.

The system attaches your latest uploaded resume automatically.

Emails are sent securely using SMTP authentication.

Status feedback is displayed on the UI.

📂 Project Structure
Cold-Mailer/
│
├── static/            # CSS & JS files
├── templates/         # HTML templates
├── uploads/           # Stored resume file
├── app.py             # Flask backend
├── requirements.txt   # Dependencies
└── README.md
🚀 Installation & Setup
1️⃣ Clone the repository
git clone https://github.com/RohitGautam30/Cold-Mailer.git
cd Cold-Mailer
2️⃣ Create virtual environment
python -m venv venv
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate      # Windows
3️⃣ Install dependencies
pip install -r requirements.txt
4️⃣ Run the application
python app.py

Open in browser:

http://127.0.0.1:5000/
🔐 Environment Variables (Recommended)

For security, store your email credentials in environment variables:

EMAIL_USER=your_email@gmail.com
EMAIL_PASS=your_app_password
📈 Why This Project Matters

Demonstrates real-world problem solving

Shows backend + frontend integration

Implements secure email authentication

Automates repetitive workflows

Practical use case (internship/job outreach automation)

🌍 Future Improvements

CSV upload for bulk recipients

Email tracking & analytics

Template-based personalization

Rate limiting & retry system

Cloud database integration

👨‍💻 Author

Rohit Gautam
GitHub: https://github.com/RohitGautam30
