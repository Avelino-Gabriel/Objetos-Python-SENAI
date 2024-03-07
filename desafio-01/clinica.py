def title(text):
    print('~' * 40)
    print(text.center(40))
    print('~' * 40)

class Usuario:
    def __init__(self, nome_funcionario):
        self.name = nome_funcionario
    def register(self):
        return self.__dict__
    
class Paciente(Usuario):
    def __init__(self, nome_funcionario):
        super().__init__(nome_funcionario)

class Funcionario(Usuario):
    def __init__(self, nome_funcionario, especialidade):
        super().__init__(nome_funcionario)
        self.specialty = especialidade

class Recepcionista(Funcionario):
    def __init__(self, nome_funcionario, especialidade):
        super().__init__(nome_funcionario, especialidade)

    def agendarConsulta(self, nome_paciente, data_consulta, horas, nome_medico, especialidade):
        consulta = {
            'paciente': nome_paciente,
            'data': data_consulta,
            'horario': horas,
            'medico': nome_medico,
            'especialidade': especialidade
        }
        print()
        print(f"Consulta marcada para o dia {consulta['data']} às {consulta['horario']} com especialista {consulta['medico']} da especialidade {consulta['especialidade']}")
        print()
        return consulta
    
class Medico(Funcionario):
    def __init__(self, nome_funcionario, especialidade, crm):
        super().__init__(nome_funcionario, especialidade)
        self.crm = crm
    def prescricao(self, nome_paciente, tratamento):
        receita = {
            'medico': self.name,
            'especialidade': self.specialty,
            'crm': self.crm,
            'nome_paciente': nome_paciente,
            'tratamento': tratamento
        }

        return receita
        
       
class Enfermeiro(Funcionario):
    def __init__(self, nome_funcionario, especialidade, coren):
        super().__init__(nome_funcionario, especialidade)
        self.coren = coren
    
    def medicacao(self, nome_paciente, tra):
        medication = {
            'enfermeiro': self.name,
            'especialidade': self.specialty,
            'COREN': self.coren,
            'paciente': nome_paciente,
            'tratamento': tra
        }
        return medication
    

recep = Recepcionista('Diego', 'Recepcionista')
med = Medico('Salvino', 'nutrição esportiva', '0123456789')
pac = Paciente('Gabriel')
enf = Enfermeiro('Isabel', 'enfermeira', '0123456789')

cons = recep.agendarConsulta(pac.name, '07/03/2024', '8h40', med.name, med.specialty)
receita = med.prescricao(pac.name, 'Racutan')
aplicacao = enf.medicacao(pac.name, 'Bezetacil')

title('Consulta')
for d in cons.items():
    print(f'{d[0]}: {d[1]}')
print()

title('Receita')
for d in receita.items():
    print(f'{d[0]}: {d[1]}')
print()

title('Medicação')
for d in aplicacao.items():
    print(f'{d[0]}: {d[1]}')
print('~' * 40)