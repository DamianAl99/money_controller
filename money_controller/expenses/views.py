from django.shortcuts import render, redirect, get_object_or_404, HttpResponseRedirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm
from django.contrib.auth.models import User
from django.db import IntegrityError


from payments.models import Groups_Pay
from payments.forms import GroupsForm
from expenses.models import Payout
from expenses.forms import PayoutForm

@login_required
def create_payout(request, pk):
    if request.method == "GET":
        group = Groups_Pay.objects.filter(id=pk).first()
        payout = Payout.objects.filter(group=group)
        restar = 0
        for pay in payout:
            if pay.status:
                restar += pay.price
        total = group.budget - restar
        message = ""
        print(((group.budget/100)*10))
        if total<=((group.budget/100)*10):
            message = f"Queda 10% del presupuesto inicial, te recomendamos a partir de ahora agregar los gastos necesarios por prioridad :)"
        #agregar mas msg de ayudas
        return render(request, 'payouts.html', {"payouts": payout, "form": PayoutForm, "id_group":pk, "total":total, "alerta":message})
    else:
        try:
            form = PayoutForm(request.POST)
            new_task = form.save(commit=False)
            new_task.group = Groups_Pay.objects.filter(id=pk).first()
            new_task.save()
            return redirect("/payouts/"+str(pk))
        except ValueError:
            return render(request, 'payouts.html', {"form": PayoutForm, "error": "Error creating payouts."})
    




@login_required
def delete_payout(request, id_group, pk):
    payout = get_object_or_404(Payout, id=pk)
    payout.delete()
    return redirect("/payouts/"+id_group)


@login_required
def complete_payout(request,id_group, pk):
    payout = get_object_or_404(Payout, id=pk)
    if payout.status:
        payout.status = False
    else:
        payout.status = True
    payout.save()
    return redirect("/payouts/"+id_group)