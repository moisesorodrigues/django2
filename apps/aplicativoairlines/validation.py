def validar_origem_destino_iguais(origem, destino, erros):
    """ Método responsável por manter a regra de negócio da origem diferente do destino"""
    if origem == destino:
            erros['destino'] = 'Origem e destino devem ser diferentes!'

def validar_valor_alfa(nome_atributo, valor_atributo, erros):
    """ Método responsável por verificar a existência de algum dígito numérico"""
    if any(char.isdigit() for char in valor_atributo):
            erros[nome_atributo] = 'Valor inválido: NÃO digite números'

def validar_periodo_viagem(data_ida, data_volta, data_pesquisa, erros):
    """ Método responsável por validar os períodos de viagem, como data de ida ser posterior à data de volta, 
    a data de ida ser anterior à data corrente, etc"""
    if data_ida > data_volta:
        erros['data_ida'] = 'A data de ida NÃO pode ser posterior à data de volta!'
    
    if data_ida < data_pesquisa:
        erros['data_ida'] = 'A data de ida NÃO pode ser anterior à data corrente!'