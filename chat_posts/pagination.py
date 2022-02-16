from rest_framework.pagination import PageNumberPagination


class OrderedInReversePagination(PageNumberPagination):
    def get_paginated_response(self, data):
        response = super().get_paginated_response(data)
        # reverse the order data is shown within response
        response.data["results"] = response.data["results"][::-1]
        return response
