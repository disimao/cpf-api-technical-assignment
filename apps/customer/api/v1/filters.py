from rest_framework import filters

from apps.customer.api.v1.utils import clean_cpf


class CPFSearchFilter(filters.SearchFilter):
    supported_params = {
        "cpf": clean_cpf,
    }

    def get_search_terms(self, request):
        search_terms = []
        for param_name, func in self.supported_params.items():
            param_value = request.query_params.get(param_name, "").strip()
            if func is not None:
                cleaned_value = func(param_value)
            else:
                cleaned_value = param_value.lower()
            if cleaned_value:
                search_terms.append(cleaned_value)
        return search_terms
