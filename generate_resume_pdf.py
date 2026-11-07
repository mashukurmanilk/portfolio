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
    topMargin=0.5 * inch,
    bottomMargin=0.5 * inch
)

styles = getSampleStyleSheet()

# Custom color palette matching the site
SUN_GOLD = colors.HexColor('#D97706') # Darker sun gold for print readability
SUN_ACCENT = colors.HexColor('#F59E0B')
MAROON = colors.HexColor('#4A0E13')
DARK_TEXT = colors.HexColor('#1E293B')
MUTED_TEXT = colors.HexColor('#475569')

name_style = ParagraphStyle(
    'NameStyle',
    fontName='Helvetica-Bold',
    fontSize=24,
    leading=28,
    textColor=MAROON,
    alignment=0
)

title_style = ParagraphStyle(
    'TitleStyle',
    fontName='Helvetica-Bold',
    fontSize=13,
    leading=16,
    textColor=SUN_GOLD,
    alignment=0
)

contact_style = ParagraphStyle(
    'ContactStyle',
    fontName='Helvetica',
    fontSize=9,
    leading=13,
    textColor=MUTED_TEXT,
    alignment=0
)

section_heading = ParagraphStyle(
    'SectionHeading',
    fontName='Helvetica-Bold',
    fontSize=12,
    leading=15,
    textColor=MAROON,
    spaceAfter=4
)

item_title = ParagraphStyle(
    'ItemTitle',
    fontName='Helvetica-Bold',
    fontSize=10,
    leading=13,
    textColor=DARK_TEXT
)

item_sub = ParagraphStyle(
    'ItemSub',
    fontName='Helvetica-Oblique',
    fontSize=9,
    leading=12,
    textColor=SUN_GOLD
)

body = ParagraphStyle(
    'Body',
    fontName='Helvetica',
    fontSize=9,
    leading=12.5,
    textColor=DARK_TEXT
)

bullet = ParagraphStyle(
    'Bullet',
    fontName='Helvetica',
    fontSize=8.5,
    leading=11.5,
    textColor=DARK_TEXT,
    leftIndent=12
)

story = []

# Header
story.append(Paragraph("MASHUKUR MANIK", name_style))
story.append(Paragraph("Full Stack Web Developer • MERN & Next.js Specialist", title_style))
story.append(Spacer(1, 4))
story.append(Paragraph("Email: mashukurmanik2552@gmail.com | GitHub: github.com/mashukurmanilk | Location: Dhaka, Bangladesh", contact_style))
story.append(Spacer(1, 8))
story.append(HRFlowable(width="100%", thickness=1.5, color=SUN_GOLD, spaceAfter=10))

# Summary
story.append(Paragraph("PROFESSIONAL SUMMARY", section_heading))
story.append(Paragraph(
    "Results-driven Full Stack Web Developer skilled in JavaScript, TypeScript, React.js, Next.js, Node.js, Express, and MongoDB. "
    "Passionate about crafting high-performance, visually polished, and scalable web applications. Strong architectural mindset "
    "with proven experience building real-time dashboards, cloud storage hubs, and full-stack management systems.",
    body
))
story.append(Spacer(1, 10))

# Technical Skills
story.append(Paragraph("TECHNICAL SKILLS", section_heading))
skills_data = [
    [Paragraph("<b>Frontend:</b>", item_title), Paragraph("React.js, Next.js 14, JavaScript (ES6+), TypeScript, HTML5, CSS3, Tailwind CSS, DaisyUI", body)],
    [Paragraph("<b>Backend:</b>", item_title), Paragraph("Node.js, Express.js, RESTful APIs, JWT Authentication, Better Auth / NextAuth", body)],
    [Paragraph("<b>Databases:</b>", item_title), Paragraph("MongoDB, Mongoose, Prisma ORM, SQLite", body)],
    [Paragraph("<b>Tools & Workflow:</b>", item_title), Paragraph("Git, GitHub, VS Code, Vite, Postman, Vercel, Netlify, Docker basics", body)]
]
skills_table = Table(skills_data, colWidths=[1.3 * inch, 6.2 * inch])
skills_table.setStyle(TableStyle([
    ('VALIGN', (0,0), (-1,-1), 'TOP'),
    ('BOTTOMPADDING', (0,0), (-1,-1), 2),
    ('TOPPADDING', (0,0), (-1,-1), 2),
]))
story.append(skills_table)
story.append(Spacer(1, 10))

# Featured Projects
story.append(Paragraph("FEATURED PROJECTS", section_heading))

# Project 1: BookNook
story.append(Paragraph("<b>BookNook – Full-Stack Library Management System</b> | <i>React, Next.js, Express, MongoDB, Tailwind CSS</i>", item_title))
story.append(Paragraph("• Built comprehensive book borrowing, inventory tracking, and dynamic catalog filtering workflows.", bullet))
story.append(Paragraph("• Implemented secure JWT authentication and role-based access for readers and administrators.", bullet))
story.append(Paragraph("• Live URL: booknook-client.vercel.app | Repo: github.com/mashukurmanilk/BookNook-frontend", bullet))
story.append(Spacer(1, 6))

# Project 2: Private Cloud Vault
story.append(Paragraph("<b>Private Cloud Vault – Personal Media & Storage Hub</b> | <i>Next.js 14, TypeScript, Tailwind, Prisma, SQLite</i>", item_title))
story.append(Paragraph("• Engineered personal cloud hub with drag-and-drop batch file uploads and clipboard paste support.", bullet))
story.append(Paragraph("• Implemented native HTTP 206 partial content range streaming for instant mobile video scrubbing.", bullet))
story.append(Paragraph("• Live URL: private-cloud-vault.vercel.app | Repo: github.com/mashukurmanilk/private-cloud-vault", bullet))
story.append(Spacer(1, 6))

# Project 3: Cyber-HUD Data Nexus
story.append(Paragraph("<b>Cyber-HUD (Data Nexus) – Gamified Developer Terminal</b> | <i>React, Vite, Web Audio API, Canvas, Tailwind</i>", item_title))
story.append(Paragraph("• Created high-tech cyberpunk productivity dashboard with synthesized retro sound effects and streak tracking.", bullet))
story.append(Paragraph("• Designed responsive animated cyber-grid canvas and interactive habit matrices.", bullet))
story.append(Paragraph("• Live URL: cyber-hud.vercel.app | Repo: github.com/mashukurmanilk/cyber-hud", bullet))
story.append(Spacer(1, 10))

# Education
story.append(Paragraph("EDUCATION & TRAINING", section_heading))
story.append(Paragraph("<b>Complete Web Development Course (Batch 14)</b> – Programming Hero", item_title))
story.append(Paragraph("Comprehensive training in modern MERN stack, Next.js, TypeScript, data structures, and production deployment.", body))
story.append(Spacer(1, 4))
story.append(Paragraph("<b>Higher Secondary Certificate (HSC) & Secondary School Certificate (SSC)</b>", item_title))
story.append(Paragraph("Science Background with focus on Mathematics, Physics, and ICT.", body))
story.append(Spacer(1, 10))

# Key Attributes
story.append(Paragraph("STRENGTHS & COMPETENCIES", section_heading))
story.append(Paragraph("• Strong problem-solving abilities, clean code advocate, fast learner, and passionate collaborator.", body))
story.append(Paragraph("• Avid gamer and tech enthusiast with keen attention to UI design fidelity, animations, and typography.", body))

doc.build(story)
print("Resume PDF generated successfully at:", pdf_path)
