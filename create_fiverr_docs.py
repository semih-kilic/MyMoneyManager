from reportlab.lib.pagesizes import letter, A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_JUSTIFY
from datetime import datetime

def create_gig_description_pdf():
    """Create Fiverr Gig Description PDF"""
    
    doc = SimpleDocTemplate(
        "Fiverr_Gig_Description.pdf",
        pagesize=letter,
        rightMargin=72,
        leftMargin=72,
        topMargin=72,
        bottomMargin=18,
    )
    
    styles = getSampleStyleSheet()
    title_style = ParagraphStyle(
        'CustomTitle',
        parent=styles['Heading1'],
        fontSize=24,
        textColor='blue',
        spaceAfter=30,
        alignment=TA_CENTER
    )
    
    heading_style = ParagraphStyle(
        'CustomHeading',
        parent=styles['Heading2'],
        fontSize=16,
        spaceAfter=12,
    )
    
    story = []
    
    # Title
    story.append(Paragraph("Flask Python Web Development", title_style))
    story.append(Paragraph("Professional Fiverr Gig Documentation", styles['Heading3']))
    story.append(Spacer(1, 12))
    
    # Gig Title
    story.append(Paragraph("GIG TITLE:", heading_style))
    story.append(Paragraph("I will develop a professional Flask Python web application", styles['BodyText']))
    story.append(Spacer(1, 12))
    
    # Description
    story.append(Paragraph("GIG DESCRIPTION:", heading_style))
    description = """
    Are you looking for a professional Flask/Python web application? I will create a custom web application tailored to your needs!
    <br/><br/>
    <b>🏆 Why Choose Me:</b><br/>
    ✓ CS50x Graduate<br/>
    ✓ Professional Flask Developer<br/>
    ✓ Clean, Documented Code<br/>
    ✓ Money Manager App Creator<br/>
    ✓ Fast Delivery<br/>
    ✓ Clear Communication<br/><br/>
    
    <b>📦 What You Get:</b><br/>
    ✓ Custom Flask/Python Application<br/>
    ✓ User Authentication System<br/>
    ✓ SQLAlchemy Database Integration<br/>
    ✓ Responsive Design<br/>
    ✓ API Integration<br/>
    ✓ Full Source Code<br/>
    ✓ Deployment Instructions<br/>
    ✓ 30 Days Support<br/><br/>
    
    <b>🔧 Technologies I Use:</b><br/>
    • Backend: Flask/Python<br/>
    • Database: SQLAlchemy/PostgreSQL/MySQL<br/>
    • Frontend: HTML5/CSS3/Bootstrap/JavaScript<br/>
    • Authentication: Flask-Login<br/>
    • Version Control: Git<br/><br/>
    
    <b>💼 Portfolio Highlight:</b><br/>
    Money Manager Application - A full-stack Flask application for personal finance management<br/>
    View Demo: https://youtu.be/leZhHVxv21E<br/><br/>
    
    <b>💡 Perfect For:</b><br/>
    • Business Management Systems<br/>
    • E-commerce Platforms<br/>
    • Content Management Systems<br/>
    • Data Management Tools<br/>
    • Custom Web Applications<br/>
    • API Development<br/>
    • SaaS Products
    """
    story.append(Paragraph(description, styles['BodyText']))
    
    story.append(PageBreak())
    
    # Packages
    story.append(Paragraph("PRICING PACKAGES:", heading_style))
    
    # Basic Package
    story.append(Paragraph("<b>BASIC PACKAGE - $200</b>", styles['Heading3']))
    basic = """
    <b>Name:</b> Basic Flask Web App<br/><br/>
    <b>Perfect for simple web applications:</b><br/>
    ✓ Simple CRUD Application<br/>
    ✓ 1-2 Database Models<br/>
    ✓ User Authentication System<br/>
    ✓ Basic Frontend with Bootstrap<br/>
    ✓ Responsive Design<br/>
    ✓ Source Code & Documentation<br/>
    ✓ Installation Guide<br/>
    ✓ 1 Week Support<br/><br/>
    <b>Delivery:</b> 3 days<br/>
    <b>Revisions:</b> 1
    """
    story.append(Paragraph(basic, styles['BodyText']))
    story.append(Spacer(1, 12))
    
    # Standard Package
    story.append(Paragraph("<b>STANDARD PACKAGE - $400</b>", styles['Heading3']))
    standard = """
    <b>Name:</b> Professional Flask Solution<br/><br/>
    <b>Everything in Basic, plus:</b><br/>
    ✓ Up to 4 Database Models<br/>
    ✓ Advanced Authentication & Authorization<br/>
    ✓ Admin Dashboard<br/>
    ✓ API Integration<br/>
    ✓ Custom Forms & Validation<br/>
    ✓ Email Notifications<br/>
    ✓ Error Logging<br/>
    ✓ Performance Optimization<br/>
    ✓ 2 Weeks Support<br/><br/>
    <b>Delivery:</b> 5 days<br/>
    <b>Revisions:</b> 2
    """
    story.append(Paragraph(standard, styles['BodyText']))
    story.append(Spacer(1, 12))
    
    # Premium Package
    story.append(Paragraph("<b>PREMIUM PACKAGE - $800</b>", styles['Heading3']))
    premium = """
    <b>Name:</b> Enterprise Flask Platform<br/><br/>
    <b>Everything in Standard, plus:</b><br/>
    ✓ Unlimited Database Models<br/>
    ✓ Payment Gateway Integration (Stripe/PayPal)<br/>
    ✓ Advanced Admin Panel<br/>
    ✓ Data Analytics Dashboard<br/>
    ✓ Custom API Development<br/>
    ✓ Security Hardening<br/>
    ✓ Performance Monitoring<br/>
    ✓ SEO Optimization<br/>
    ✓ 1 Month Priority Support<br/>
    ✓ Deployment Assistance<br/>
    ✓ Ongoing Maintenance<br/><br/>
    <b>Delivery:</b> 7-10 days<br/>
    <b>Revisions:</b> 3
    """
    story.append(Paragraph(premium, styles['BodyText']))
    
    # Build PDF
    doc.build(story)
    print("✅ Fiverr_Gig_Description.pdf created successfully!")

def create_faq_pdf():
    """Create FAQ PDF"""
    
    doc = SimpleDocTemplate(
        "Fiverr_FAQ_Document.pdf",
        pagesize=letter,
        rightMargin=72,
        leftMargin=72,
        topMargin=72,
        bottomMargin=18,
    )
    
    styles = getSampleStyleSheet()
    title_style = ParagraphStyle(
        'CustomTitle',
        parent=styles['Heading1'],
        fontSize=24,
        textColor='blue',
        spaceAfter=30,
        alignment=TA_CENTER
    )
    
    story = []
    
    # Title
    story.append(Paragraph("Frequently Asked Questions", title_style))
    story.append(Paragraph("Flask Python Web Development Service", styles['Heading3']))
    story.append(Spacer(1, 20))
    
    faqs = [
        {
            "q": "Do you provide complete source code?",
            "a": "Yes, you'll receive the complete source code with detailed documentation, including all Python/Flask files, database schema, frontend templates, configuration files, setup instructions, and API documentation."
        },
        {
            "q": "Can you help with deployment?",
            "a": "Yes! I provide detailed deployment guide, server setup instructions, environment configuration, database migration steps, and SSL/HTTPS setup help. Premium package includes hands-on deployment assistance."
        },
        {
            "q": "What information do you need to start?",
            "a": "To begin your project, please provide: 1) Project requirements/features list, 2) Any design preferences, 3) Database structure (if you have one), 4) API requirements (if any), 5) Target deployment platform."
        },
        {
            "q": "Do you provide post-delivery support?",
            "a": "Yes! All packages include 7-30 days of bug fixes (depending on package), technical support, code explanations, and minor adjustments. Premium package includes extended support and maintenance."
        },
        {
            "q": "Can you modify existing Flask applications?",
            "a": "Yes, I can add new features, fix bugs, optimize performance, upgrade dependencies, and implement security patches. Please share your existing code for assessment and custom quote."
        },
        {
            "q": "What about security?",
            "a": "All applications include secure authentication, password hashing, XSS protection, CSRF protection, SQL injection prevention, input validation, and security best practices."
        },
        {
            "q": "Do you sign NDAs?",
            "a": "Yes, I'm happy to sign NDAs to protect your intellectual property and ensure confidentiality throughout our collaboration."
        },
        {
            "q": "What's your development process?",
            "a": "1) Requirements discussion & planning, 2) Database design & approval, 3) Backend development, 4) Frontend implementation, 5) Testing & QA, 6) Code review & optimization, 7) Deployment preparation, 8) Final delivery & support."
        },
        {
            "q": "Can you integrate third-party services?",
            "a": "Yes, I can integrate payment gateways (Stripe, PayPal), email services (SendGrid, Mailgun), cloud storage (AWS S3, Google Cloud), social media APIs, SMS services, analytics tools, and more."
        },
        {
            "q": "What's included in the documentation?",
            "a": "You'll receive setup & installation guide, API documentation, database schema diagram, code comments, user manual, deployment instructions, security guidelines, and troubleshooting guide."
        }
    ]
    
    for i, faq in enumerate(faqs, 1):
        story.append(Paragraph(f"<b>Q{i}: {faq['q']}</b>", styles['Heading3']))
        story.append(Paragraph(faq['a'], styles['BodyText']))
        story.append(Spacer(1, 12))
    
    # Build PDF
    doc.build(story)
    print("✅ Fiverr_FAQ_Document.pdf created successfully!")

def create_requirements_pdf():
    """Create Requirements Checklist PDF"""
    
    doc = SimpleDocTemplate(
        "Project_Requirements_Checklist.pdf",
        pagesize=letter,
        rightMargin=72,
        leftMargin=72,
        topMargin=72,
        bottomMargin=18,
    )
    
    styles = getSampleStyleSheet()
    title_style = ParagraphStyle(
        'CustomTitle',
        parent=styles['Heading1'],
        fontSize=24,
        textColor='blue',
        spaceAfter=30,
        alignment=TA_CENTER
    )
    
    story = []
    
    # Title
    story.append(Paragraph("Project Requirements Checklist", title_style))
    story.append(Paragraph("Flask Python Web Application", styles['Heading3']))
    story.append(Spacer(1, 20))
    
    intro = """
    To ensure your project starts smoothly and meets all your expectations, 
    please provide the following information:
    """
    story.append(Paragraph(intro, styles['BodyText']))
    story.append(Spacer(1, 12))
    
    sections = [
        {
            "title": "1. Core Features",
            "items": [
                "What main functions do you need?",
                "How many user types/roles?",
                "Do you need an admin panel?",
                "What are the key workflows?"
            ]
        },
        {
            "title": "2. Database Needs",
            "items": [
                "What kind of data will you store?",
                "How many different data types?",
                "Do you have existing data to import?",
                "Expected data volume?"
            ]
        },
        {
            "title": "3. Design Requirements",
            "items": [
                "Any specific color scheme?",
                "Mobile-responsive needed?",
                "Any website design references?",
                "Logo and branding materials?"
            ]
        },
        {
            "title": "4. Technical Needs",
            "items": [
                "Where will you host the application?",
                "Need email functionality?",
                "Any third-party integrations?",
                "Performance requirements?"
            ]
        },
        {
            "title": "5. Security Requirements",
            "items": [
                "User authentication method?",
                "Data encryption needed?",
                "Compliance requirements (GDPR, etc.)?",
                "Access control levels?"
            ]
        },
        {
            "title": "6. Timeline & Budget",
            "items": [
                "When do you need this completed?",
                "Any specific milestones?",
                "Budget constraints?",
                "Need ongoing maintenance?"
            ]
        }
    ]
    
    for section in sections:
        story.append(Paragraph(f"<b>{section['title']}</b>", styles['Heading2']))
        for item in section['items']:
            story.append(Paragraph(f"□ {item}", styles['BodyText']))
        story.append(Spacer(1, 12))
    
    footer = """
    <br/><br/>
    <b>Note:</b> The more details you provide, the better I can tailor the solution to your needs!
    Please feel free to add any additional information or requirements not listed above.
    """
    story.append(Paragraph(footer, styles['BodyText']))
    
    # Build PDF
    doc.build(story)
    print("✅ Project_Requirements_Checklist.pdf created successfully!")

if __name__ == "__main__":
    print("Creating Fiverr Documentation PDFs...\n")
    create_gig_description_pdf()
    create_faq_pdf()
    create_requirements_pdf()
    print("\n✅ All PDF documents created successfully!")
    print("\nGenerated files:")
    print("1. Fiverr_Gig_Description.pdf")
    print("2. Fiverr_FAQ_Document.pdf")
    print("3. Project_Requirements_Checklist.pdf")
