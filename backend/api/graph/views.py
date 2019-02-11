# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import numpy as np
from django.http import HttpResponse, JsonResponse

def sin(request):
    x = np.linspace(0,1,11)
    y = np.sin(x)
    return JsonResponse({'x' : x.tolist(),
                        'y': y.tolist()})

def cos(request):
    x = np.linspace(0,1,11)
    y = np.cos(x)
    return JsonResponse({'x' : x.tolist(),
                        'y': y.tolist()})


def tan(request):
    x = np.linspace(0,1,11)
    y = np.tan(x)
    return JsonResponse({'x' : x.tolist(),
                        'y': y.tolist()})
