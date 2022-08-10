from django.shortcuts import render
from django.http import HttpResponseRedirect
from .form import FeedbackForm
from .models import Feedback
from django.views import View
from django.views.generic.base import TemplateView
from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormView, CreateView, UpdateView


# class FeedbackView(View):
#     def get(self, request):
#         form = FeedbackForm()
#         return render(request, 'feedback/feedback.html', context={'form': form})
#
#     def post(self, request):
#         form = FeedbackForm(request.POST)
#         if form.is_valid():
#             print(form.cleaned_data)
#             form.save()
#             return HttpResponseRedirect('/done')
#         return render(request, 'feedback/feedback.html', context={'form': form})

class FeedbackViewUpdate(UpdateView):
    model = Feedback
    form_class = FeedbackForm
    template_name = 'feedback/feedback.html'
    success_url = '/done'



class FeedbackView(CreateView):
    model = Feedback
    form_class = FeedbackForm
    template_name = 'feedback/feedback.html'
    success_url = '/done'

    def form_valid(self, form):
        form.save()
        return super(FeedbackView, self).form_valid(form)

    # def post(self, request):
    #     form = FeedbackForm(request.POST)
    #     if form.is_valid():
    #         print(form.cleaned_data)
    #         form.save()
    #         return HttpResponseRedirect('/done')
    #     return render(request, 'feedback/feedback.html', context={'form': form})


class UpdateFeedback(View):

    def get(self, request, id_feedback):
        feed = Feedback.objects.get(id=id_feedback)
        form = FeedbackForm(instance=feed)
        return render(request, 'feedback/feedback.html', context={'form': form})

    def post(self, request, id_feedback):
        feed = Feedback.objects.get(id=id_feedback)
        form = FeedbackForm(request.POST, instance=feed)
        if form.is_valid():
            print(form.cleaned_data)
            form.save()
            return HttpResponseRedirect(f'/{id_feedback}')
        return render(request, 'feedback/feedback.html', context={'form': form})


class DoneView(TemplateView):
    template_name = 'feedback/done.html'

# class AllFeedback(TemplateView):
#     template_name = 'feedback/all-load_file.html'
#
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data()
#         feedback = Feedback.objects.all()
#         context['feedback'] = feedback
#         return context

# class OneFeedback(TemplateView):
#     template_name = 'feedback/one-load_file.html'
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data()
#         id_feedback = kwargs['id_feedback']
#         feedback = Feedback.objects.get(id=id_feedback)
#         context['feedback'] = feedback
#         return context

class OneFeedback(DetailView):
    template_name = 'feedback/one-feedback.html'
    model = Feedback

class AllFeedback(ListView):
    template_name = 'feedback/all-feedback.html'
    model = Feedback
    context_object_name = 'feedback'

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset

