# core/views.py
from django.shortcuts import render
from .mcp import main as mcp_tools  # your MCP functions

def home(request):
    result = None
    if request.method == "POST":
        user_input = request.POST.get("input_text", "")

        # Call MCP tool to generate full CV in template format
        result = mcp_tools.generate_profile(
            summary=mcp_tools.summarize_cv(text_input=user_input),
            education=mcp_tools.generate_education(text_input=user_input),
            experience=mcp_tools.generate_experience(text_input=user_input),
            projects=mcp_tools.generate_projects(text_input=user_input),
            certifications=mcp_tools.generate_certifications(text_input=user_input),
            skills=mcp_tools.extract_skills(full_text=user_input)
        )

    return render(request, "index.html", {"cv_output": result})