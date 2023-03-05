def clean_cpf(value):
    return "".join([n for n in value if n.isdigit()])
