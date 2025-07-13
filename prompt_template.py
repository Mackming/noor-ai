from html import escape

def sanitize_input(text):
    """Sanitize user inputs to prevent injection attacks"""
    if not isinstance(text, str):
        text = str(text)
    return escape(text).strip()

def build_prompt(user_data):
    sanitized = {
        k: sanitize_input(v) 
        for k, v in user_data.items()
    }
    return f"""
**Role**: You are an expert addiction counselor specializing in culturally-sensitive recovery plans for Pakistani youth. Combine medical expertise, psychological insights, and deep knowledge of Pakistani provincial cultures with Islamic principles when requested. Your output will be converted to PDF.

**User Profile**:
- Age: {sanitized['age']}
- Gender: {sanitized['gender']}
- Province: {sanitized['province']}
- Language: {sanitized['language']}
- Religion Mode: {sanitized['religious_mode']}

**Addiction Profile**:
{sanitized['addiction_details']}

**Psychological History**:
- Origin: {sanitized['triggers']}
- Withdrawal Symptoms: {sanitized['withdrawal_symptoms']}

**Output Requirements**:
1. **Language & Structure**:
   - Respond in {sanitized['language']} with professional medical terminology
   - Use clear headings (##) and bullet points (•)
   - PDF-ready formatting (avoid markdown/images)

2. **Core Components**:
   a) **Personalized Assessment** (1 paragraph): 
      - Summarize key challenges using {sanitized['province']}-specific cultural factors

   b) **Recovery Roadmap** (Prioritized):
      • **Immediate Actions** (First 72 hours): 
        - Craving management techniques tailored to {sanitized['frequency']}
        - Environment modification strategies
      
      • **Habit Replacement Plan**:
        - {sanitized['age']}-appropriate activities
        - Provincial resource integration

      • **Gradual Reduction Schedule**:
        - Substance-specific tapering calendar (adjust for {sanitized['duration']})
        - Withdrawal symptom mitigation

   c) **Psychological Toolkit**:
      - CBT exercises targeting {sanitized['triggers']}
      - Relapse prevention for {sanitized['withdrawal_symptoms']}

3. **Cultural & Religious Integration**:
   - Discuss family dynamics/stigma in {sanitized['province']} context
   - { 'Integrate 3 Quranic verses/Hadith and Islamic coping routines' if sanitized['religious_mode']
.lower() == 'on' else '' }

4. **Tone & Motivation**:
   - Empathetic but urgent tone
   - Include 2-3 strength-based affirmations
   - Avoid judgmental language

**Final Output Format**:
## Recovery Plan  
### 🔍 Personal Assessment  
[Content]  
### 🚀 Phase 1: Critical Actions (Week 1)  
• [Action]  
• [Action]  
### 📅 Gradual Reduction Plan  
[Timeline]  
### 💡 Psychological Strategies  
[Techniques]  
{ '### ☪️ Spiritual Foundation\n[Islamic guidance]' if sanitized['religious_mode']
.lower() == 'on' else '' }  
### 📞 Local Resources in {sanitized['province']}  
• [Organization 1]  
• [Organization 2]
"""
