from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from datetime import datetime, date, time
from django.utils import timezone
from django.contrib import messages
from .models import LedgerEntry, LedgerEntryBackups
import openpyxl

def _fmt_currency(value):
    try:
        return '₹ ' + f"{value:,.2f}"
    except Exception:
        return value

def dashboard_OLD(request):
    entries = LedgerEntry.objects.filter(flag=1).order_by('timestamp', 'id')

    start = request.GET.get('start')
    end = request.GET.get('end')
    show_all = request.GET.get('show_all')

    if show_all:
        filtered = entries
        heading = "All Entries"
    elif start and end:
        try:
            s = datetime.fromisoformat(start)
            e = datetime.fromisoformat(end)
            filtered = entries.filter(timestamp__range=[s,e])
            heading = f"{s.date()} to {e.date()}"
        except Exception:
            filtered = entries.none()
            heading = "Invalid range"
    else:
        today = timezone.now().date()
        today_start = datetime.combine(today, time.min)
        today_end = datetime.combine(today, time.max)
        filtered = entries.filter(timestamp__range=[today_start, today_end])
        heading = str(today)

    credits = filtered.filter(credit_amount__isnull=False).order_by('timestamp','id')
    debits = filtered.filter(debit_amount__isnull=False).order_by('timestamp','id')

    total_credit = sum(float(e.credit_amount or 0) for e in credits)
    total_debit = sum(float(e.debit_amount or 0) for e in debits)
    balance = total_credit - total_debit

    context = {
        'credits': credits,
        'debits': debits,
        'total_credit': total_credit,
        'total_debit': total_debit,
        'balance': balance,
        'total_credit_display': _fmt_currency(total_credit),
        'total_debit_display': _fmt_currency(total_debit),
        'balance_display': _fmt_currency(balance),
        'start': start,
        'end': end,
        'show_all': show_all,
        'heading': heading,
    }
    return render(request, 'ledger_app/dashboard_side_by_side_with_msgs.html', context)

def dashboard(request):
    entries = LedgerEntry.objects.filter(flag=1).order_by('timestamp', 'id')

    start = request.GET.get('start')
    end = request.GET.get('end')
    show_all = request.GET.get('show_all')

    # If a date range is selected
    if start and end:
        try:
            s = datetime.fromisoformat(start)
            e = datetime.fromisoformat(end)
            filtered = entries.filter(timestamp__range=[s, e])
            heading = f"{s.date()} to {e.date()}"
        except Exception:
            filtered = entries.none()
            heading = "Invalid range"

    # If "Show All" clicked or no filters (default)
    else:
        filtered = entries
        heading = "All Entries"

    credits = filtered.filter(credit_amount__isnull=False).order_by('timestamp', 'id')
    debits = filtered.filter(debit_amount__isnull=False).order_by('timestamp', 'id')

    total_credit = sum(float(e.credit_amount or 0) for e in credits)
    total_debit = sum(float(e.debit_amount or 0) for e in debits)
    balance = total_credit - total_debit

    context = {
        'credits': credits,
        'debits': debits,
        'total_credit': total_credit,
        'total_debit': total_debit,
        'balance': balance,
        'total_credit_display': _fmt_currency(total_credit),
        'total_debit_display': _fmt_currency(total_debit),
        'balance_display': _fmt_currency(balance),
        'start': start,
        'end': end,
        'show_all': show_all,
        'heading': heading,
    }
    return render(request, 'ledger_app/dashboard_side_by_side_with_msgs.html', context)

def add_credit(request):
    if request.method == 'POST':

        particular = request.POST.get('particular') or None
        amount = request.POST.get('amount') or None
        amount = float(amount) if amount not in [None,''] else None
        LedgerEntry.objects.create(particular_credit=particular, credit_amount=amount,flag=1)
        LedgerEntryBackups.objects.create(particular_credit=particular, credit_amount=amount, flag=1)
        messages.success(request, 'Credit entry added successfully!')
        return redirect('ledger_list')
    return render(request, 'ledger_app/add_credit.html')

def add_debit(request):
    if request.method == 'POST':
        particular = request.POST.get('particular') or None
        amount = request.POST.get('amount') or None
        amount = float(amount) if amount not in [None,''] else None
        LedgerEntry.objects.create(particular_debit=particular, debit_amount=amount,flag=1)
        LedgerEntryBackups.objects.create(particular_debit=particular, debit_amount=amount, flag=1)
        messages.success(request, 'Debit entry added successfully!')
        return redirect('ledger_list')
    return render(request, 'ledger_app/add_debit.html')

def edit_credit(request, id):
    entry = get_object_or_404(LedgerEntry, id=id)
    if request.method == 'POST':
        entry.particular_credit = request.POST.get('particular') or None
        amt = request.POST.get('amount') or None
        entry.credit_amount = float(amt) if amt not in [None,''] else None
        entry.particular_debit = None
        entry.debit_amount = None
        entry.save()
        LedgerEntryBackups.objects.create(particular_credit=request.POST.get('particular') or None, credit_amount=float(amt) if amt not in [None,''] else None, flag=1)
        messages.success(request, 'Credit entry updated successfully!')
        return redirect('ledger_list')
    return render(request, 'ledger_app/edit_credit.html', {'entry': entry})

def edit_debit(request, id):
    entry = get_object_or_404(LedgerEntry, id=id)
    if request.method == 'POST':
        entry.particular_debit = request.POST.get('particular') or None
        amt = request.POST.get('amount') or None
        entry.debit_amount = float(amt) if amt not in [None,''] else None
        entry.particular_credit = None
        entry.credit_amount = None
        entry.save()
        LedgerEntryBackups.objects.create(particular_debit=request.POST.get('particular') or None, debit_amount=float(amt) if amt not in [None,''] else None, flag=1)
        messages.success(request, 'Debit entry updated successfully!')
        return redirect('ledger_list')
    return render(request, 'ledger_app/edit_debit.html', {'entry': entry})

def delete_credit(request, id):
    entry = get_object_or_404(LedgerEntry, id=id)
    entry.flag = 2
    entry.save()
    messages.success(request, 'Credit entry deleted successfully!')
    return redirect('ledger_list')

def delete_debit(request, id):
    entry = get_object_or_404(LedgerEntry, id=id)
    entry.flag = 2
    entry.save()
    messages.success(request, 'Debit entry deleted successfully!')
    return redirect('ledger_list')

def export_ledger_to_excel(request):
    entries = LedgerEntry.objects.filter(flag=1).order_by('timestamp', 'id')

    start = request.GET.get('start')
    end = request.GET.get('end')
    show_all = request.GET.get('show_all')

    if show_all:
        filtered = entries
    elif start and end:
        try:
            s = datetime.fromisoformat(start)
            e = datetime.fromisoformat(end)
            filtered = entries.filter(timestamp__range=[s,e])
        except Exception:
            filtered = entries.none()
    else:
        today = timezone.now().date()
        today_start = datetime.combine(today, time.min)
        today_end = datetime.combine(today, time.max)
        filtered = entries.filter(timestamp__range=[today_start, today_end])

    wb = openpyxl.Workbook()
    ws = wb.active
    ws.title = "Ledger Report"
    ws.append(['Timestamp', 'Credit Particular', 'Credit Amount', 'Debit Particular', 'Debit Amount'])
    total_credit = 0
    total_debit = 0
    for entry in filtered:
        ts = entry.timestamp.isoformat() if entry.timestamp else ''
        ws.append([
            ts,
            entry.particular_credit or '',
            float(entry.credit_amount or 0),
            entry.particular_debit or '',
            float(entry.debit_amount or 0),
        ])
        total_credit += float(entry.credit_amount or 0)
        total_debit += float(entry.debit_amount or 0)
    ws.append([])
    ws.append(['','Total Credit', total_credit,'Total Debit', total_debit])
    ws.append(['','','','Balance', total_credit - total_debit])
    response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = 'attachment; filename=ledger_report.xlsx'
    wb.save(response)
    return response

def credit_all_entry_history(request):
    entries = LedgerEntryBackups.objects.filter(flag=1).order_by('-id')
    credits = entries.filter(credit_amount__isnull=False).order_by('-id')
    context = {
        'entries': credits,
    }
    return render(request, 'ledger_app/credit_all_entry_history.html', context)
def debit_all_entry_history(request):
    entries = LedgerEntryBackups.objects.filter(flag=1).order_by('-id')
    debits = entries.filter(debit_amount__isnull=False).order_by('-id')
    context = {
        'entries': debits,
    }
    return render(request, 'ledger_app/debit_all_entry_history.html', context)
