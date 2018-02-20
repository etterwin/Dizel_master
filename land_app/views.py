from django.shortcuts import render
from .forms import NamePhoneForm, DetailPhoneForm, QuizPhoneForm
from django.views.generic import View
from django.views.decorators.csrf import csrf_exempt


class IndexView(View):
    template_name = 'index.html'

    @csrf_exempt
    def get(self, request):
        forms = NamePhoneForm(), DetailPhoneForm(), QuizPhoneForm()

        return render(request, self.template_name, {'form_1': forms[0], 'form_2': forms[1], 'form_3': forms[2]})

    @csrf_exempt
    def post(self, request):

        # if 'namephoneform' in request.POST:
        #     form = NamePhoneForm(request.POST)
        # elif 'detailphoneform' in request.POST:
        #     form = DetailPhoneForm(request.POST)
        # else:
        #     form = QuizPhoneForm(request.POST)
        #
        # if form.is_valid():
        #     print(form.cleaned_data)
        #
        #     return render(request, self.template_name, {
        #         'form_1': NamePhoneForm(),
        #         'form_2': DetailPhoneForm(),
        #         'form_3': QuizPhoneForm()
        #     })

        phone = request.POST['phone']
        name = None
        detail = None
        quiz = None

        if 'name' in request.POST:
            name = request.POST['name']

        if 'detail' in request.POST:
            detail = request.POST['detail']

        if 'quiz' in request.POST:
            quiz = request.POST['quiz']



        return render(request, self.template_name, {
            'form_1': NamePhoneForm(),
            'form_2': DetailPhoneForm(),
            'form_3': QuizPhoneForm()
        })
