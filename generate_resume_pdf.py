import os
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, HRFlowable
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch

pdf_path = os.path.join('assets', 'Mashukur_Manik_Resume.pdf')
doc = SimpleDocTemplate(
    pdf_path,
    pagesize=letter,
    leftMargin=0.5 * inch,
    rightMargin=0.5 * inch,
    topMargin=0.45 * inch,
    bottomMargin=0.45 * inch
)

styles = getSampleStyleSheet()

# Custom colors extracted from palette
SUN_GOLD = colors.HexColor('#D97706') # For print contrast
MAROON = colors.HexColor('#4A0E13')
DARK_TEXT = colors.HexColor('#1E293B')
MUTED_TEXT = colors.HexColor('#475569')

name_style = ParagraphStyle(
    'NameStyle',
    fontName='Helvetica-Bold',
    fontSize=22,
    leading=26,
    textColor=MAROON,
    alignment=0
)

title_style = ParagraphStyle(
    'TitleStyle',
    fontName='Helvetica-Bold',
    fontSize=11,
    leading=14,
    textColor=SUN_GOLD,
    alignment=0
)

contact_style = ParagraphStyle(
    'ContactStyle',
    fontName='Helvetica',
    fontSize=8.5,
    leading=12,
    textColor=MUTED_TEXT,
    alignment=0
)

section_heading = ParagraphStyle(
    'SectionHeading',
    fontName='Helvetica-Bold',
    fontSize=11,
    leading=14,
    textColor=MAROON,
    spaceAfter=3
)

item_title = ParagraphStyle(
    'ItemTitle',
    fontName='Helvetica-Bold',
    fontSize=9.5,
    leading=12.5,
    textColor=DARK_TEXT
)

body = ParagraphStyle(
    'Body',
    fontName='Helvetica',
    fontSize=8.5,
    leading=12,
    textColor=DARK_TEXT
)

bullet = ParagraphStyle(
    'Bullet',
    fontName='Helvetica',
    fontSize=8.2,
    leading=11.5,
    textColor=DARK_TEXT,
    leftIndent=10
)

story = []

# Header
story.append(Paragraph("MASHUKUR MANIK", name_style))
story.append(Paragraph("Undergraduate CSE Student @ SUST • Full Stack Web Developer & ML / DL Engineer", title_style))
story.append(Spacer(1, 3))
story.append(Paragraph("Email: mashukurmanik2552@gmail.com | GitHub: github.com/mashukurmanilk | Location: Sylhet / Dhaka, Bangladesh", contact_style))
story.append(Spacer(1, 6))
story.append(HRFlowable(width="100%", thickness=1.5, color=SUN_GOLD, spaceAfter=8))

# Summary
story.append(Paragraph("PROFESSIONAL SUMMARY", section_heading))
story.append(Paragraph(
    "Undergraduate Computer Science & Engineering student at Shahjalal University of Science and Technology (SUST). "
    "Full Stack Web Developer and Machine Learning / Deep Learning practitioner with proven expertise building scalable "
    "applications with Next.js, React, Node.js, Express, and MongoDB, alongside training deep learning neural architectures "
    "(CNNs, Transformers, predictive modeling) using PyTorch, TensorFlow, and Scikit-Learn.",
    body
))
story.append(Spacer(1, 8))

# Education
story.append(Paragraph("EDUCATION", section_heading))
story.append(Paragraph("<b>Shahjalal University of Science and Technology (SUST)</b>", item_title))
story.append(Paragraph("<i>B.Sc. (Engineering) in Computer Science & Engineering (CSE)</i> — Undergrad Student", body))
story.append(Paragraph("• Core Coursework: Data Structures, Algorithms, Machine Learning, Deep Learning, Operating Systems, DBMS, Software Engineering, Object-Oriented Programming.", bullet))
story.append(Spacer(1, 4))
story.append(Paragraph("<b>Higher Secondary Certificate (HSC)</b> — Science Division (GPA 5.00)", item_title))
story.append(Paragraph("• Core Subjects: Mathematics, Physics, Chemistry, Information & Communication Technology (ICT).", bullet))
story.append(Spacer(1, 8))

# Technical Skills
story.append(Paragraph("TECHNICAL SKILLS", section_heading))
skills_data = [
    [Paragraph("<b>ML & Deep Learning:</b>", item_title), Paragraph("PyTorch, TensorFlow, Keras, Scikit-Learn, NumPy, Pandas, OpenCV, CNNs, Transformers, Model Optimization", body)],
    [Paragraph("<b>Frontend:</b>", item_title), Paragraph("React.js, Next.js 14 (App Router), TypeScript, JavaScript (ES6+), Tailwind CSS, DaisyUI, HTML5, CSS3", body)],
    [Paragraph("<b>Backend & APIs:</b>", item_title), Paragraph("Node.js, Express.js, RESTful APIs, JWT Authentication, Better Auth, FastAPI basics", body)],
    [Paragraph("<b>Databases & Tools:</b>", item_title), Paragraph("MongoDB, Mongoose ORM, Prisma ORM, SQLite, Git, GitHub, Vite, Postman, Vercel, Docker basics", body)]
]
skills_table = Table(skills_data, colWidths=[1.4 * inch, 6.1 * inch])
skills_table.setStyle(TableStyle([
    ('VALIGN', (0,0), (-1,-1), 'TOP'),
    ('BOTTOMPADDING', (0,0), (-1,-1), 1.5),
    ('TOPPADDING', (0,0), (-1,-1), 1.5),
]))
story.append(skills_table)
story.append(Spacer(1, 8))

# Featured Projects (BookNook, Private Vault, Cyber-Hub)
story.append(Paragraph("PROJECT VAULT (FEATURED WORK)", section_heading))

# 1. BookNook
story.append(Paragraph("<b>BookNook – Full-Stack Library Ecosystem & ML Recommendations</b> | <i>React, Next.js, Express, MongoDB, Tailwind, Scikit-Learn</i>", item_title))
story.append(Paragraph("• Built comprehensive library management platform with book borrowing workflows, status tracking, and inventory control.", bullet))
story.append(Paragraph("• Implemented content-based book recommendation engine using cosine similarity and reader preference vectors.", bullet))
story.append(Paragraph("• Live URL: booknook-client.vercel.app | Repo: github.com/mashukurmanilk/BookNook-frontend", bullet))
story.append(Spacer(1, 5))

# 2. Private Vault
story.append(Paragraph("<b>Private Vault – Self-Hosted Media & Cloud Storage Hub</b> | <i>Next.js 14, TypeScript, Tailwind, Prisma, SQLite, HTTP 206</i>", item_title))
story.append(Paragraph("• Engineered personal cloud storage platform with drag-and-drop batch upload, clipboard screenshot paste, and master PIN auth.", bullet))
story.append(Paragraph("• Implemented native HTTP 206 Partial Content range requests for instant video scrubbing across devices.", bullet))
story.append(Paragraph("• Live URL: private-cloud-vault.vercel.app | Repo: github.com/mashukurmanilk/private-cloud-vault", bullet))
story.append(Spacer(1, 5))

# 3. Cyber-Hub
story.append(Paragraph("<b>Cyber-Hub – Gamified Developer Productivity Terminal & Analytics</b> | <i>React, Vite, Web Audio API, Canvas, Predictive Trends</i>", item_title))
story.append(Paragraph("• Created high-tech developer command center with synthesized Web Audio 8-bit sound effects and interactive 60 FPS canvas grid.", bullet))
story.append(Paragraph("• Designed habit tracking protocols, productivity regression forecasting, and streak tracking logic.", bullet))
story.append(Paragraph("• Live URL: cyber-hud.vercel.app | Repo: github.com/mashukurmanilk/cyber-hud", bullet))
story.append(Spacer(1, 8))

# Strengths
story.append(Paragraph("CORE COMPETENCIES", section_heading))
story.append(Paragraph("• Strong foundation in algorithmic problem-solving, data structures, and computer science theory from SUST CSE.", body))
story.append(Paragraph("• Hands-on experience taking complex web applications and deep learning models from ideation to production deployment.", body))

doc.build(story)
print("Updated Resume PDF generated successfully at:", pdf_path)
