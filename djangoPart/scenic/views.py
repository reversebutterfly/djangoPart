from django.shortcuts import render
from django.db.models import Avg, Count
from .models import ScenicSpot
from utils.pyecharts_visual import generate_heatmap


def scenic_heatmap(request):
    # 获取所有景点数据
    scenic_spots = ScenicSpot.objects.all()

    # 生成热力图
    heatmap = generate_heatmap(scenic_spots)

    context = {
        'heatmap': heatmap
    }
    return render(request, 'scenic_heatmap.html', context)


def scenic_list(request):
    # 获取景点列表并按销量和评分排序
    scenic_spots = ScenicSpot.objects.order_by('-sale', '-score')

    # 计算一些统计数据
    stats = {
        'total_spots': scenic_spots.count(),
        'avg_score': scenic_spots.aggregate(Avg('score'))['score__avg'],
        'top_provinces': scenic_spots.values('province_city_region').annotate(
            spot_count=Count('id')
        ).order_by('-spot_count')[:5]
    }

    context = {
        'scenic_spots': scenic_spots,
        'stats': stats
    }
    return render(request, 'scenic_list.html', context)


def scenic_detail(request, spot_id):
    # 景点详情页
    spot = ScenicSpot.objects.get(id=spot_id)

    context = {
        'spot': spot
    }
    return render(request, 'scenic_detail.html', context)