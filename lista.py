while True:
    add = input('Deseja adicionar um funcionário? (s/n) ')
    if add.lower() != 's':
        break
    
    nome = input('Digite o nome do funcionário: ')
    cargo = input('Digite o cargo do funcionário: ')
    salario = float(input('Digite o salário do funcionário: '))
    
    funcionario = {'nome': nome, 'cargo': cargo, 'salario': salario}
    funcionarios.append(funcionario)

print('\nLista de Funcionários:')

for funcionario in funcionarios:
    print(f'Nome: {funcionario["nome"]}')
    print(f'Cargo: {funcionario["cargo"]}')
    print(f'Salário: R${funcionario["salario"]:.2f}')
