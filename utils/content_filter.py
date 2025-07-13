# utils/content__filter.py

from ai_handler import generate_advice  # Make sure ai_handler.py is in root or update the path

MODERATION_PROMPT = """
Act as a strict cultural moderator for Pakistan's anonymous addiction recovery platform. Your sole task is to output either "APPROVE" or "REJECT" based on these immutable rules:

**APPROVE ONLY IF ALL ARE TRUE**:
1. Content describes personal addiction/recovery journey without glorification
2. Zero personal identifiers (names/numbers/locations) 
3. No vulgarity, slurs, or triggering descriptions
4. No promotion of substances/self-harm methods
5. Culturally respectful to Islamic values (no blasphemy, explicit content)
6. On-topic (addiction/mental health/recovery)

**IMMEDIATE REJECT IF ANY ARE TRUE**:
- Contains contact info (even masked)
- Uses humor about addiction/suffering
- Encourages substance use or harmful behavior
- Includes racist/sexist/hate speech
- Mentions specific drug sources/prices
- Written unseriously (e.g., emoji spam, trolling)

**Cultural Safeguards**:
- Flag religious disrespect (Quran/Hadith misuse)
- Reject Western slang glorifying addiction
- Block region-specific slurs (e.g., provincial insults)

**Output Protocol**:
- No explanations ever
- Only 1 word: "APPROVE" or "REJECT"
- Bias prevention: Ignore political/religious leanings unless violating rules
"""

def is_clean(story_text: str) -> bool:
    prompt = f"{MODERATION_PROMPT}\n\nUser submission:\n\"\"\"\n{story_text.strip()}\n\"\"\""
    try:
        result = generate_advice(prompt)
        if "error" in result:
            return False
        return result.get("response", "").strip().upper() == "APPROVE"
    except Exception:
        return False
