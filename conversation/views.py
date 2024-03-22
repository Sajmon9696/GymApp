from django.shortcuts import render, redirect
from django import forms

# Create your views here.


from django.views import View
from django.shortcuts import render
from django.views.generic import DetailView

from conversation.forms import ConversationMessageForm
from conversation.models import Conversation, ConversationMessage


class NewMessageView(View):
    """
        Widok obsługujący tworzenie nowej wiadomości w konwersacji.
        Umożliwia użytkownikowi wysłanie nowej wiadomości w ramach istniejącej lub nowo utworzonej konwersacji.
        """
    template_name = 'conversation/new_message.html'
    model = ConversationMessage
    form_class = ConversationMessageForm

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            content = form.cleaned_data['content']
            created_by = request.user

            sent_to = form.cleaned_data['sent_to']
            print(sent_to)
            conversation = Conversation.objects.filter(members=created_by).filter(members=sent_to).first()

            if not conversation:
                conversation = Conversation.objects.create()
                conversation.members.add(created_by, sent_to)

            message = ConversationMessage.objects.create(conversation=conversation, content=content,
                                                         created_by=created_by,
                                                         sent_to=sent_to)
            conversation.save()

            return redirect('conversation:detail', pk=conversation.id)
        return render(request, self.template_name, {'form': form})


class InboxView(View):
    """
        Widok listy skrzynek odbiorczych użytkownika.
        Wyświetla listę konwersacji, do których użytkownik jest członkiem.
        """
    template_name = 'conversation/inbox.html'
    model = Conversation

    def get(self, request, *args, **kwargs):
        conversations = Conversation.objects.filter(members=request.user)
        context = {'conversations': conversations, }

        return render(request, self.template_name, context)


class ConversationDetail(DetailView):
    """
        Widok szczegółów konwersacji.
        Wyświetla szczegóły konwersacji oraz formularz do wysyłania nowych wiadomości.
        """
    model = Conversation
    template_name = 'conversation/detail.html'
    context_object_name = 'conversation'
    form_class = ConversationMessageForm

    def get(self, request, *args, **kwargs):
        conversation = self.get_object()
        sent_to = conversation.members.exclude(id=request.user.id).first()
        initial_data = {'sent_to': sent_to}
        form = self.form_class(initial=initial_data)
        form.fields['sent_to'].widget = forms.HiddenInput()
        return render(request, self.template_name, {'form': form, 'conversation': conversation})

    def post(self, request, *args, **kwargs):
        conversation = self.get_object()
        form = self.form_class(request.POST)
        if form.is_valid():
            content = form.cleaned_data['content']
            sent_to = form.cleaned_data['sent_to']
            created_by = request.user

            message = ConversationMessage.objects.create(conversation=conversation, content=content,
                                                         created_by=created_by,
                                                         sent_to=sent_to)
            conversation.save()
            return redirect('conversation:detail', pk=conversation.id)
        return render(request, self.template_name, {'form': form, 'conversation': conversation})
