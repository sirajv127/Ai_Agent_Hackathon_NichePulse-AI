import google.generativeai as genai
from app.core.config import settings

try:
    genai.configure(api_key=settings.GEMINI_API_KEY)
    # The fix is to use a globally available model
    model = genai.GenerativeModel('gemini-1.5-flash-latest') 
except Exception as e:
    print(f"Error configuring Gemini: {e}")
    model = None

def generate_trend_brief(content_list: list[str]) -> str:
    """
    Analyzes a list of content summaries and generates a strategic trend brief.
    """
    if not model:
        return "AI Model not configured due to API key error."
    if not content_list:
        return "No new content to analyze in this period."

    full_text = "\n---\n".join(content_list)
    prompt = f"""
    You are a strategic brand analyst for a marketing team. Your task is to analyze the following social media posts from influencers and competitors collected over the last 48 hours.

    From this content, you must identify:
    1.  An overall **Executive Summary** of the key conversations.
    2.  The top 2-3 **Trending Themes**. For each theme, provide a brief summary and mention which posts relate to it.
    3.  A list of actionable **Recommendations** for the brand team.

    Please format your entire response in Markdown.

    Here is the raw content:
    ---
    {full_text}
    """

    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        print(f"Error calling Gemini API: {e}")
        return "Error: Could not generate analysis from AI."