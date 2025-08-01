#pagina inicial

lista = []
opc = [1,2,3,4,5,99]
esc = 99
while esc in opc:
    print("""
    ------------------------------------------
    |                TO DO LIST                |
    ------------------------------------------
    |            O que deseja fazer?           |
    |                                          |
    |   1- Inserir tarefa                      |             
    |   2- Listar tarefas                      |
    |   3- Marcar como concluída               |
    |   4- Remover tarefa                      |
    |   0- Sair                                |
    ------------------------------------------
    """)    
    esc = int(input("Digite o número referente so que deseja fazer: "))    
    if esc == 0:
        break
    elif esc == 1:
        print("""
    ------------------------------------------
    |             INSERIR TAREFA              |
    ------------------------------------------
    """)

        while True:
            tarefas = input("Indique aqui uma tarefa a ser realizada: ")
            confir = input("Você tem mais alguma tarefa? ").lower()
            lista.append(tarefas)
            if confir != "sim":
                break
            else:
                pass

    elif esc == 2:
        print("""
    ------------------------------------------
    |              LISTAR TAREFAS             |
    ------------------------------------------
    """)

        for percorrer in lista:
            print(percorrer)

    elif esc == 4:
        print("""
 ------------------------------------------
|             REMOVER TAREFA              |
 ------------------------------------------
""")
        c = 0
        tc = input("Quais tarefas você deseja remover? ")
        lista.pop(tc)



    elif esc == 3:

        print("""
 ------------------------------------------
|         MARCAR COMO CONCLUIDA           |
 ------------------------------------------
""")
        conclu = input("Qual tarefa você concluiu? ")
        lista [conclu] = "[x] " + lista [conclu] 
        print({lista[conclu]})
