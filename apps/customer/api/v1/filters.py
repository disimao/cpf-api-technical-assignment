from rest_framework import filters

from apps.customer.api.v1.utils import clean_cpf


class CPFSearchFilter(filters.SearchFilter):
    def get_search_terms(self, request):
        if "search" in request.query_params.keys():
            request.query_params._mutable = True
            request.query_params["search"] = clean_cpf(
                request.query_params["search"]
            )
        return super().get_search_terms(request)
