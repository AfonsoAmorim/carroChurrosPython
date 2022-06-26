def imprime_parametros(**kwargs):
    for key,value in kwargs.items():
        print("%s = %s" % (key,value))
imprime_parametros(nome="Ana", sobrenome="Maria")
imprime_parametros(nome="Ana", sobrenome="Maria", idade="55", cidade="SP")