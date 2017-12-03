from .models import Feedback
from django.views.generic.edit import CreateView
from .forms import FeedbackForm
from django.core.mail import mail_admins
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin


# Create your views here.
class FeedbackView(SuccessMessageMixin, CreateView):
    form_class = FeedbackForm
    model = Feedback
    template_name = 'feedback.html'
    context_object_name = 'form'
    success_message = 'Thank you for your feedback! We will keep in touch with you very soon!'
    success_url = reverse_lazy('list')

    def post(self, request, *args, **kwargs):
        name = request.POST.get('name')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        from_mail = request.POST.get('from_email')
        create_date = request.POST.get('create_date')
        response = super().post(self, request, *args, **kwargs)
        mail_admins(
                    'Subject here'.format(subject),
                    """Message from {}
                    -------------------
                    {}
                    -------------------
                    created:{} from {}""".format(name, message, create_date, from_mail),

                    fail_silently=False,


        )
        return response

    # def get(self, request, *args, **kwargs):
    #     response = super().get(self, request, *args, **kwargs)
    #     obj = request
    #     print(dir(obj))
    #     send_mail(
    #         'Subject here',
    #         'Here is the message.',
    #         'from@example.com',
    #         ['to@example.com'],
    #         fail_silently=False,
    #     )
    #     return response
