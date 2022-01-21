from django.shortcuts import render, get_object_or_404
from freebo.models import Freewriting
from django.core.paginator import Paginator
from django.db.models import Q, Count




def index(request):
    """
    freeboard 목록 출력
    """
    # 입력 파라미터
    page = request.GET.get('page', '1')  # 페이지
    kw = request.GET.get('kw', '')  # 검색어
    so = request.GET.get('so', 'recent')  # 정렬기준


    # 정렬
    # if so == 'recommend':
    #     freewriting_list = Freewriting.objects.annotate(num_voter=Count('voter')).order_by('-num_voter', '-create_date')
    if so == 'popular':
        freewriting_list = Freewriting.objects.annotate(num_answer=Count('replying')).order_by('-num_answer', '-create_date')
    else:  # recent
        freewriting_list = Freewriting.objects.order_by('-create_date')


    # 조회

    # freewriting_list = Freewriting.objects.order_by('-create_date')
    if kw:
        freewriting_list = freewriting_list.filter(
            Q(title__icontains=kw) |  # 제목검색
            Q(content__icontains=kw) |  # 내용검색
            Q(author__username__icontains=kw) |  # 질문 글쓴이검색
            Q(replying__author__username__icontains=kw)  # 답변 글쓴이검색
        ).distinct()

    # 페이징처리
    paginator = Paginator(freewriting_list, 10)  # 페이지당 10개씩 보여주기
    page_obj = paginator.get_page(page)

    context = {'freewriting_list': page_obj, 'page': page, 'kw': kw, 'so': so}
    return render(request, 'freebo/freewriting_list.html', context)


def detail(request, freewriting_id):
    """
    freeboard 내용 출력
    """
    freewriting = get_object_or_404(Freewriting, pk=freewriting_id)
    context = {'freewriting': freewriting}
    return render(request, 'freebo/freewriting_detail.html', context)