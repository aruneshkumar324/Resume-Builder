from django.shortcuts import render, redirect
from .models import Feedback


def feedback(request):
    if request.method == "POST":
        user_id = request.POST["user_id"]
        email = request.POST["email"]
        feature = request.POST["feature"]
        feedback = request.POST["feedback"]

        data = Feedback(user_id=user_id, email=email, feature=feature, feedback=feedback)

        data.save()

        return redirect("feedback")

    return render(request, 'contacts/feedback.html')