from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from freebo.models import Freewriting, Replying
from freebo.forms import ReplyingForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages


@login_required(login_url='common:login')
def replying_create(request, freewriting_id):
    """
    freebo 댓글등록
    """
    freewriting = get_object_or_404(Freewriting, pk=freewriting_id)

    if request.method == "POST":
        form = ReplyingForm(request.POST)
        if form.is_valid():
            replying = form.save(commit=False)
            replying.author = request.user  # author 속성에 로그인 계정 저장
            replying.create_date = timezone.now()
            replying.freewriting = freewriting
            replying.save()
            return redirect('freebo:detail', freewriting_id=freewriting.id)

    else:
        form = ReplyingForm()
    context = {'freewriting': freewriting, 'form': form}
    return render(request, 'freebo/freewriting_detail.html', context)

@login_required(login_url='common:login')
def replying_modify(request, replying_id):
    """
    pybo 답변수정
    """
    replying = get_object_or_404(Replying, pk=replying_id)
    if request.user != replying.author:
        messages.error(request, '수정권한이 없습니다')
        return redirect('freebo:detail', replying_id=replying.freewriting.id)

    if request.method == "POST":
        form = ReplyingForm(request.POST, instance=replying)
        if form.is_valid():
            replying = form.save(commit=False)
            replying.modify_date = timezone.now()
            replying.save()
            return redirect('freebo:detail', freewriting_id=replying.freewriting.id)
    else:
        form = ReplyingForm(instance=replying)
    context = {'replying': replying, 'form': form}
    return render(request, 'freebo/replying_form.html', context)



@login_required(login_url='common:login')
def replying_delete(request, replying_id):
    """
    freebo 답변삭제
    """
    replying = get_object_or_404(Replying, pk=replying_id)
    if request.user != replying.author:
        messages.error(request, '삭제권한이 없습니다')
    else:
        replying.delete()
    return redirect('freebo:detail', freewriting_id=replying.freewriting.id)