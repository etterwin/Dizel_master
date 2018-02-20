from django.shortcuts import render
from .forms import NamePhoneForm
from django.views.generic import View


class IndexView(View):
    template_name = 'index.html'

    def get(self, request):
        form = NamePhoneForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = NamePhoneForm(request.POST)

        if form.is_valid():
            print(form.cleaned_data)

            return render(request, self.template_name, {'form': NamePhoneForm})

        return render(request, self.template_name, {'form': NamePhoneForm})
