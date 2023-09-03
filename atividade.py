class Node:
    def __init__(self, name, contact):
    self.name = name
    self.contact = contact
    self.next = None
    
class AgendaHeroes:
    def __init__(self):
        self.table = [None] * 26
    def hash(self, key):
        return ord(key[0].upper()) - ord('A')
    
    def add_contact(self, name, contact):
        index = self.hash(name)
        if not self.table[index]:
            self.table[index] = Node(name, contact)
        else:
            curr = self.table[index]
            while curr.next:
                curr = curr.next
            curr.next = Node(name, contact)
            
    def search_contact(self, name):
        index = self.hash(name)
        curr = self.table[index]
        while curr:
            if curr.name == name:
                return curr.contact
            curr = curr.next
        return None
    
    def list_contacts(self, letter):
        index = self.hash(letter)
        contacts = []
        curr = self.table[index]
        while curr:
            contacts.append((curr.name, curr.contact))
            curr = curr.next
        return contacts
    
    def remove_contact(self, name):
        index = self.hash(name)
        if not self.table[index]:
            return False
        if self.table[index].name == name:
            self.table[index] - self.table[index].next
            return True
        prev = self.table[index]
        curr = prev.next
        while curr:
            if curr.name == name:
                prev.next = curr.next
                return True
            prev = curr
            curr = curr.next
        return False
    
def main():
    agenda = AgendaHeroes()
    # Adicionar contatos
    agenda.add_contact('Superman', 'superman@heroes.com')
    agenda.add_contact('Batman', 'batman@heroes.com')
    agenda.add_contact('Spiderman', 'spiderman@heroes.com')
    # Buscar contato por nome
    print(agenda.search_contact('Superman'))
    # Listar contatos por letra inícial
    print(agenda.list_contacts('S'))
    # Remover contato
    print(agenda.remove_contact('Superman'))
    print(agenda.search_contact('Superman'))
    
if __name__ == '__main__':
    main()
