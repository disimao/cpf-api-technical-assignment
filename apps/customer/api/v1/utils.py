def clean_cpf(value):
    return "".join(filter(str.isdigit, value))
