from django.shortcuts import render, render_to_response
from django.template import RequestContext
from django.http import HttpResponse
from contacts.forms import *
from contacts.models import Person
# Create your views here.

def contact_list(request):
    #return HttpResponse ("Hello World!!")
    return render_to_response('contact_list.html', {},
                              context_instance = RequestContext(request))
    
def contact_form_old(request):
    #return HttpResponse ("Hello World!!")
    return render_to_response('contact_form.html', {},
                              context_instance = RequestContext(request))

def hello_you(request, you):
    html = "<html> <body> Hello %s </body></html>" % (you)
    return HttpResponse(html)

def delete_contact(request, person_id):
    try:
        p_id = int(person_id)
        if p_id:
            p = Person.objects.get(id = p_id)
            p.delete()
            return HttpResponse("Contact Deleted Successfully!")
        else:
            all_contacts = Person.objects.all()
            return render_to_response('contact_list.html',
                                {'all_contacts' : all_contacts},
                                context_instance = RequestContext(request))                                 
    except Exception, e:
        return HttpResponse(str(e))

def edit_contact(request, person_id):
    try:
        p_id = int(person_id)
        if p_id:
            p = Person.objects.filter(id = p_id)
            form = ContactModelForm(instance=p[0])
            return render_to_response('contact_form.html', {'form' : form },
                                      context_instance = RequestContext(request))
        else:
            all_contacts = Person.objects.all()
            return render_to_response('contact_list.html',
                                {'all_contacts' : all_contacts},
                                context_instance = RequestContext(request))                                 
    except Exception, e:
        return HttpResponse(str(e))

def contact_form(request):
    form = ContactForm()
    if request.method == "POST":
        form = ContactModelForm(request.POST)
        #person_obj = None
        if form.is_valid():
            p = form.instance
            cd = form.cleaned_data
#            if p:
#                person_obj = Person.objects.get(id = p.id)
#                person_obj.delete()
#                person_obj.full_name = cd['full_name']
#                person_obj.phone = cd['phone']
#                person_obj.email = cd['email']
#                person_obj.save()
#                return HttpResponse("Contact Edited ")
#            else:
            try:
                add_new_record(cd, p) 
                return HttpResponse("New contact added successfully!!")
            except Exception, e:
                return HttpResponse(str(e))
    else:
        form = ContactForm()
       
    return render_to_response('contact_form.html', {'form' : form },
                              context_instance = RequestContext(request))

def add_new_record(cleaned_data, person_obj = None):
    if person_obj:
        person_obj.full_name = cleaned_data['full_name']
        person_obj.phone = cleaned_data['phone']
        person_obj.email = cleaned_data['email']
        person_obj.save()
    else:
        person = Person(full_name = cleaned_data['full_name'],
                        phone = cleaned_data['phone'],
                        email = cleaned_data['email'])
        person.save()

def contact_list(request):
    all_contacts = Person.objects.all()
    return render_to_response('contact_list.html',
                        {'all_contacts' : all_contacts},
                        context_instance = RequestContext(request))                 