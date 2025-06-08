PROMPT = """
## Task: Voice Conversion Evaluation

**Voice conversion** is a technique that transforms the voice in a source audio to sound like a target speaker, while keeping the linguistic content and intonation the same.

You are given four audio clips, in the following order:

1. Source audio (from the original speaker)  
2. Target speaker reference audio  
3. Converted audio A (from voice conversion model A)  
4. Converted audio B (from voice conversion model B)

**Your task:**  
Ignore background noise and content — focus only on speaker similarity. Decide which converted audio sounds more like the target speaker in terms of voice identity (e.g., timbre, pitch, tone)? (a) Converted audio A (b) Converted audio B.
"""

STRICT_OUTPUT = """
**Output format:**
Respond with either **(a)** or **(b)** only.
"""


def getPrompt(
    strict: bool = False,
):
    if strict:
        return PROMPT + STRICT_OUTPUT
    else:
        return PROMPT
