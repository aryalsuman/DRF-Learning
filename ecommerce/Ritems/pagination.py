from email.policy import default
from rest_framework.pagination import LimitOffsetPagination

class MyLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 2
    max_limit = 10
    default_offset = 0
    limit_query_param = 'limit'
    offset_query_param = 'offset'