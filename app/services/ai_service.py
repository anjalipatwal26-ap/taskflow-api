import json
import google.generativeai as genai
from app.core.config import settings

genai.configure(api_key=settings.GEMINI_API_KEY)
model = genai.GenerativeModel("gemini-3.6-flash")

def analyze_task(title: str, description: str | None) -> dict:
    prompt = f"""Analyze this task and respond with ONLY valid JSON, no other text.

Task title: {title}
Task description: {description or "N/A"}

Respond in this exact JSON format:
{{
  "suggested_priority": "Low" | "Medium" | "High",
  "category": "Work" | "Study" | "Personal" | "Finance" | "Other",
  "summary": "one sentence summary",
  "suggestion": "one practical productivity tip"
}}"""

    try:
        response = model.generate_content(prompt)
        raw_text = response.text.strip()
        raw_text = raw_text.removeprefix("```json").removeprefix("```").removesuffix("```").strip()
        data = json.loads(raw_text)

        allowed_priority = {"Low", "Medium", "High"}
        allowed_category = {"Work", "Study", "Personal", "Finance", "Other"}

        if data.get("suggested_priority") not in allowed_priority:
            data["suggested_priority"] = "Medium"
        if data.get("category") not in allowed_category:
            data["category"] = "Other"
        if not isinstance(data.get("summary"), str):
            data["summary"] = title
        if not isinstance(data.get("suggestion"), str):
            data["suggestion"] = "Break this task into smaller steps."

        return data

    except Exception:
        return {
            "suggested_priority": "Medium",
            "category": "Other",
            "summary": title,
            "suggestion": "AI analysis unavailable right now — try again later.",
        }