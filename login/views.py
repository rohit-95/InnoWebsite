from django.shortcuts import render, render_to_response
from django.views.generic import TemplateView
from django.template.context import RequestContext


class login(TemplateView):
    template = 'login.html'

    def get(self, request):
        context = RequestContext(
            request, {
                'request': request,
                'user': request.user,
            }
        )
        return render_to_response(self.template, context_instance=context)