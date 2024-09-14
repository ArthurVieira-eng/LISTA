#Definindo a lista de compromissos.
def compromissos_marcados(compromissos):
#Caso não houver compromissos.
  if not compromissos:
    print('Sem compromissos agendados.')
#Caso houver compromisso.
  else:
    for compromisso in compromissos:
      print(compromisso) 
#Iniciando o progama.
print('Aqui está sua lista de compromissos virtual.')
print('Deseja iniciar ')
iniciar = input('')
if iniciar == ('sim' or 'Sim' or 'sIM' or 'SIm' or 'sIm' or 'siM' or 'SIM'):
  compromissos = [] 
#Sistema while para as perguntas.
while True:
    print('1.Adicionar compromisso.')
    print('2.Listar compromisso.')
    print('3.Remover compromisso.')
    print('4.Sair.')
    opcao = input('Digite o numero desejado:') 
#Marcando o compromisso.
    if opcao == '1':
      nome = input('Nome do compromisso:')
      hora = input('Hora do compromisso:')
      data = input('Data do compromisso:')
      compromissos.append({'nome' : nome, 'data': data, 'hora': hora})
      print('Compromisso adicionado com sucesso.')
#Exibição da lista.
    elif opcao == '2':
      print('Listando compromissos.')
      compromissos_marcados(compromissos)
#Exclusão de algum compromisso agendado.
    elif opcao == '3':
      nome = input('Qual o nome do compromisso que deseja remover ?')
      compromissos = [compromisso for compromisso in compromissos if compromisso['nome'] != nome]
      print('Compromisso removido com sucesso.') 
#Saindo do progama.
    elif opcao == '4':
      print('Saindo do programa.')
      print('Até a próxima.')
      break
#Caso seja inserida uma opção inexistente.
    else:
      print('Opção inválida.')