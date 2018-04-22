from django.db.models import Count, Q
from django.shortcuts import render, HttpResponse
from .models import Department, Employee


def homepage(request):
    departments = Department.objects.all()

    datasets = Employee.objects.values('dep_id__label').annotate(emp_count=Count('id'))
    print(datasets)
    return render(request,'homepage.html',{'datasets':datasets,'departments':departments})
    # dataset = [
    #     {'ticket_class': 1, 'survived_count': 200, 'not_survived_count': 123},
    #     {'ticket_class': 2, 'survived_count': 119, 'not_survived_count': 158},
    #     {'ticket_class': 3, 'survived_count': 181, 'not_survived_count': 528}
    # ]
    # return render(request,'homepage.html',locals())

def test(request):
    datasets = Employee.objects.values('dep_id').annotate(emp_count=Count('id'))
    print(datasets)
    return HttpResponse('...')

#
# def ticket_class_view(request):
#     dataset = Passenger.objects \
#         .values('ticket_class') \
#         .annotate(survived_count=Count('ticket_class', filter=Q(survived=True)),
#                   not_survived_count=Count('ticket_class', filter=Q(survived=False))) \
#         .order_by('ticket_class')
#     return render(request, 'homepage.html', {'dataset': dataset})
