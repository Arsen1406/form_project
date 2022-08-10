
from django.contrib import admin
from django.urls import path
from .views import FeedbackView, UpdateFeedback, DoneView, AllFeedback, OneFeedback, FeedbackViewUpdate

urlpatterns = [
    path('done', DoneView.as_view()),
    path('all-feedback', AllFeedback.as_view()),
    path('all-feedback/<int:pk>', OneFeedback.as_view()),
    path('update/<int:pk>', FeedbackViewUpdate.as_view()),
    path('', FeedbackView.as_view()),
    path('<int:id_feedback>', UpdateFeedback.as_view()),
]
