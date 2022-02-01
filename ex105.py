def notas(*resp, sit=False):
    """
    -> Função para analisar notas e situações de alunos.
    :param resp: uma ou mais notas de alunos
    :param sit: valor opcional, indicando se deve ou não aparecer a situação de cada aluno
    :return: dicionário com várias informações sobre a situação do aluno
    """
    dict = {}
    dict['Notas informadas'] = len(resp)
    dict['Maior nota'] = max(resp)
    dict['Menor nota'] = min(resp)
    dict['Média'] = sum(resp)/ len(resp)
    if sit == True:
        if dict['Média'] >= 6:
            dict['Situação'] = 'Aprovado'
        else:
            dict['Situação'] = 'Reprovado'
    return dict


resp = notas(3.5, 2, 6.5, 2, 7, 4, sit=True)
print(resp)