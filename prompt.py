PROMPT = """
## Task: Voice Conversion Evaluation

**Voice conversion** is a technique that transforms the voice in a source audio to sound like a target speaker, while keeping the linguistic content and intonation the same.

You are given four audio clips, in the following order:

1. Source audio (from the original speaker)  
2. Target speaker reference audio  
3. Converted audio A (from voice conversion model A)  
4. Converted audio B (from voice conversion model B)

**Your task:**  
Decide which converted audio (**A** or **B**) sounds more like the target speaker in terms of voice identity (e.g., timbre, pitch, tone).  
Ignore background noise and content — focus only on speaker similarity.
"""

STRICT_OUTPUT = """
**Output format:**
Respond with either **A** or **B** only.
"""

def getPrompt(
    strict: bool = False,
):
    if strict:
        return PROMPT + STRICT_OUTPUT
    return PROMPT
