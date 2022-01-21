from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone

from ..forms import FreewritingForm
from ..models import Freewriting





@login_required(login_url='common:login')
def freewriting_create(request):
    """
    Freeboard 글쓰기등록
    """
    if request.method == 'POST':
        form = FreewritingForm(request.POST)
        if form.is_valid():
            freewriting = form.save(commit=False)
            freewriting.author = request.user  # author 속성에 로그인 계정 저장
            freewriting.create_date = timezone.now()
            freewriting.save()
            return redirect('freebo:index')
    else:
        form = FreewritingForm()
    context = {'form': form}
    return render(request, 'freebo/freewriting_form.html', context)


@login_required(login_url='common:login')
def freewriting_modify(request, freewriting_id):
    """
    pybo 글쓰기수정
    """
    freewriting = get_object_or_404(Freewriting, pk=freewriting_id)
    if request.user != freewriting.author:
        messages.error(request, '수정권한이 없습니다')
        return redirect('freebo:detail', freewriting_id=freewriting.id)

    if request.method == "POST":
        form = FreewritingForm(request.POST, instance=freewriting)
        if form.is_valid():
            freewriting = form.save(commit=False)
            freewriting.modify_date = timezone.now()  # 수정일시 저장
            freewriting.save()
            return redirect('freebo:detail', freewriting_id=freewriting.id)
    else:
        form = FreewritingForm(instance=freewriting)
    context = {'form': form}
    return render(request, 'freebo/freewriting_form.html', context)

@login_required(login_url='common:login')
def freewriting_delete(request, freewriting_id):
    """
    pybo 글쓰기삭제
    """
    freewriting = get_object_or_404(Freewriting, pk=freewriting_id)
    if request.user != freewriting.author:
        messages.error(request, '삭제권한이 없습니다')
        return redirect('freebo:detail', freewriting_id=freewriting.id)
    freewriting.delete()
    return redirect('freebo:index')
