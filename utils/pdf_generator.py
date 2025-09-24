from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.enums import TA_RIGHT, TA_LEFT, TA_CENTER
from reportlab.lib import colors
from reportlab.lib.units import inch
from datetime import datetime
from io import BytesIO
import re
import os

def clean_text_for_pdf(text):
    """
    Preprocesses text to remove markdown syntax and emojis while preserving structure
    """
    # Remove markdown headers (##, ###)
    text = re.sub(r'^#{1,3}\s*', '', text, flags=re.MULTILINE)
    
    # Remove emphasis asterisks but preserve bullet points
    text = re.sub(r'\*{1,2}(?![ \n])', '', text)  # Remove standalone asterisks
    
    # Remove markdown bold/italic syntax (**text**)
    text = re.sub(r'\*{2}(.*?)\*{2}', r'\1', text)
    
    # Remove emojis and other special symbols
    text = re.sub(r'[^\w\s.,:;\-?!"\'()%$@#/\\=+&<>ء-ي]', '', text, flags=re.UNICODE)
    
    # Clean up bullet points
    text = re.sub(r'^[\*\-]\s*', '• ', text, flags=re.MULTILINE)
    
    # Remove extra spaces
    text = re.sub(r' +', ' ', text)
    text = re.sub(r'\n\s*\n', '\n\n', text)
    
    # Remove any remaining HTML-like tags
    text = re.sub(r'<[^>]+>', '', text)
    
    return text.strip()

def generate_pdf(text, name="Recovery Plan", language="English"):
    buffer = BytesIO()
    
    # Preprocess and clean the text
    cleaned_text = clean_text_for_pdf(text)
    
    # Create document with adjusted margins
    doc = SimpleDocTemplate(
        buffer,
        pagesize=A4,
        rightMargin=0.7*inch,
        leftMargin=0.7*inch,
        topMargin=0.5*inch,
        bottomMargin=0.5*inch
    )

    # ====================
    # 🎨 STYLE DEFINITIONS
    # ====================
    styles = getSampleStyleSheet()
    
    # Color scheme
    primary_color = colors.HexColor("#6C63FF")  # Purple
    secondary_color = colors.HexColor("#35D0BA")  # Teal
    accent_color = colors.HexColor("#4A4A4A")     # Dark gray
    today = datetime.now().strftime("%B %d, %Y")
    
    # English styles
    if language == "Urdu":
        title_style = ParagraphStyle(
            name="UrduTitle",
            fontName="Helvetica-Bold",
            fontSize=18,
            leading=24,
            alignment=TA_RIGHT,
            textColor=primary_color,
            spaceAfter=12
        )
        heading_style = ParagraphStyle(
            name="UrduHeading",
            fontName="Helvetica-Bold",
            fontSize=14,
            leading=20,
            alignment=TA_RIGHT,
            textColor=secondary_color,
            spaceBefore=20,
            spaceAfter=8
        )
        body_style = ParagraphStyle(
            name="UrduBody",
            fontName="Helvetica",
            fontSize=12,
            leading=18,
            alignment=TA_RIGHT,
            textColor=accent_color,
            spaceAfter=10
        )
        title = f"{name} کا بحالی منصوبہ"
    else:
        title_style = ParagraphStyle(
            name="EnglishTitle",
            fontName="Helvetica-Bold",
            fontSize=20,
            leading=26,
            alignment=TA_CENTER,
            textColor=primary_color,
            spaceAfter=12
        )
        heading_style = ParagraphStyle(
            name="EnglishHeading",
            fontName="Helvetica-Bold",
            fontSize=14,
            leading=20,
            alignment=TA_LEFT,
            textColor=secondary_color,
            spaceBefore=20,
            spaceAfter=8
        )
        body_style = ParagraphStyle(
            name="EnglishBody",
            fontName="Helvetica",
            fontSize=11,
            leading=16,
            alignment=TA_LEFT,
            textColor=accent_color,
            spaceAfter=10
        )
        title = f"{name}'s Personalized Recovery Plan"

    # ====================
    # 📄 DOCUMENT STRUCTURE
    # ====================
    story = []
    
    # Header with title
    header = Table([
        [Paragraph("<b>Smart Rehabilitation AI</b> Recovery Program", styles['Heading3'])],
        [Paragraph(f"Confidential Document • Generated on: {today}", styles['BodyText'])]
    ], colWidths=[doc.width])
    
    header.setStyle(TableStyle([
        ('ALIGN', (0,0), (-1,-1), 'LEFT'),
        ('TEXTCOLOR', (0,0), (-1,0), primary_color),
        ('TEXTCOLOR', (0,1), (-1,1), accent_color),
        ('FONTSIZE', (0,1), (-1,1), 8),
        ('BOTTOMPADDING', (0,0), (-1,-1), 5),
        ('BOTTOMPADDING', (0,1), (-1,1), 15),
    ]))
    story.append(header)
    
    # Title section
    story.append(Paragraph(title, title_style))
    story.append(Spacer(1, 0.2*inch))
    
    # Decorative divider
    divider = Table([[""]], colWidths=[doc.width], rowHeights=[2])
    divider.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), secondary_color),
        ('BOX', (0,0), (-1,-1), 0.5, secondary_color)
    ]))
    story.append(divider)
    story.append(Spacer(1, 0.3*inch))
    
    # Content sections
    sections = cleaned_text.split("\n\n")  # Split by double newlines for sections
    for section in sections:
        if section.strip():
            # SAFE HEADING DETECTION - only add formatting if we have actual content
            header_keywords = ['Assessment', 'Phase', 'Plan', 'Strategies', 'Foundation', 'Resources']
            is_heading = any(keyword in section for keyword in header_keywords)
            
            # Format as heading only if we have content beyond just the keyword
            if is_heading and len(section.strip()) > 20:
                story.append(Paragraph(f"<b>{section.strip()}</b>", heading_style))
                story.append(Spacer(1, 0.1*inch))
            else:
                # Create bullet points for lists
                if "•" in section:
                    bullet_points = section.split("•")
                    for point in bullet_points:
                        if point.strip():
                            story.append(Paragraph(f"• {point.strip()}", body_style))
                else:
                    # Simple paragraph without any HTML formatting
                    story.append(Paragraph(section.strip(), body_style))
                story.append(Spacer(1, 0.1*inch))
    
    # Footer
    footer = Table([
        [Paragraph("Confidentiality Notice: This document contains sensitive personal information. Do not share without consent.", styles['Italic'])],
        [Paragraph("© 2025 Smart Rehabilitation AI Recovery Program. All rights reserved.", styles['BodyText'])]
    ], colWidths=[doc.width])
    
    footer.setStyle(TableStyle([
        ('ALIGN', (0,0), (-1,-1), 'CENTER'),
        ('TEXTCOLOR', (0,0), (-1,-1), accent_color),
        ('FONTSIZE', (0,0), (-1,-1), 8),
        ('TOPPADDING', (0,0), (-1,-1), 15),
        ('LINEABOVE', (0,0), (-1,0), 0.5, colors.lightgrey),
    ]))
    story.append(footer)
    
    # ====================
    # 🖨️ DOCUMENT GENERATION
    # ====================
    doc.build(story)
    buffer.seek(0)
    return buffer
