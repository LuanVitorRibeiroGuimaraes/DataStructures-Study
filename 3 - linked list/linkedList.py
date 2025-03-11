class Node:
    def __init__(self, value):
        self.value = value #definindo o valor do nó
        self.next = None #definindo para onde vai apontar
    

    
class LinkedList:
    def __init__(self, value):
        new_node = Node(value) #criando um nó
        self.head = new_node #fazendo a head apontar para o novo nó
        self.tail = new_node #fazendo o tail apontar para o novo nó, pois é o único existente
        self.length = 1 #tamanho da linkedList
    
    def print_list(self): #preciso percorrer toda a linked porém eu não posso perder a header
        pointer = self.head
        while pointer != None: #criando outro ponteiro para percorrer para não perder a referência da head
            print(pointer.value)
            pointer = pointer.next #como eu tenho uma instancia de Node, posso utilizar o atributo '.next' para apontar para o próximo elemento
            
            
    # basicamente eu preciso para o append:
    #     -> adicionar um item ao final da lista
    #         -> fazer um loop até o último elemento
    #     -> se a lista for none, apontar direto o tail para o novo elemento
            
    def append(self, value): #adicionar um item ao final da lista
        new_node = Node(value) #criando um novo nó
        if self.tail == None: #se o tail estiver vazio -> não possuem elementos na lista
            self.head = new_node #o head apontará para o novo nó
            self.tail == new_node #o tail apontará para o novo nó
        else:
            self.tail.next = new_node #próximo valor do tail apontará para o novo nó
            self.tail = new_node #o tail apontará para o novo nó
            
        self.length += 1 #incrementa o tamanho da lista
        return True #retorna verdadeiro para informar que o valor 
            
