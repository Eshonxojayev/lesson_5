from rest_framework.pagination import LimitOffsetPagination

class Pagination(LimitOffsetPagination):
    def __init__(self, x: int, y: int):
        if x is None:
            default_limit = 20
        else:
            default_limit = x

        self.x = x
        self.y = y

    if x is None:
        default_limit = 20

    max_limit = 100