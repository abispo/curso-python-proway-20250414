# Para criação de classes em Python, utilizamos a palavra reservada class, seguido do nome da classe. De preferência, utilizamos o PascalCase na definição do nome. Mais detalhes, veja a pep8
class Pokemon:
    
    # O método __init__ é um método especial das classes em Python que serve para inicializar os atributos do objeto. O primeiro parâmetro de um método em Python, sempre será o self (com exceção de classmethods e staticmethods). O self é uma referência do próprio objeto que foi instanciado (semelhante ao this do Java).
    def __init__(self, name: str, type: str, health: int):

        # Abaixo, estamos criando 3 atributos: _name, _type e _health, e estamos atribuindo os valores recebidos no método inicializador. No Python, não temos nenhum mecanismo que defina o nível de acesso que qualquer coisa que seja (classe, atributo, método, etc), então seguimos a padronização de, caso o nome do atributo/método comece com underline(_), deve ser considerado privado
        self._name = name
        self._type = type
        self._health = health
        self.__teste = 0

    # Para criarmos um método, utilizamos a palavra reservada def, e em seguida o nome do método/função
    def attack(self):
        # Como dito anteriormente, todos os métodos de instância, obrigatoriamente devem começar com o atributo self.
        print(f"{self._name} attacks!")

    def dodge(self):
        print(f"{self._name} dodges!")

    def evolve(self):
        print(f"{self._name} evolves!")
    
    # Para alterar os atributos de um objeto instanciado, podemos utilizar 2 abordagens:

    # 1) Utilizar métodos getters e setters
    def set_name(self, new_name: str) -> None:
        self._name = new_name

    def get_name(self) -> str:
        return self._name
    
    # 2) Utilizar o decorator @property
    # Aqui criamos o "getter"
    @property
    def type(self) -> str:
        return self._type
    
    # Aqui criamos o "setter"
    @type.setter
    def type(self, new_type: str) -> None:
        self._type = new_type

    @property
    def health(self) -> int:
        return self._health
    
    @health.setter
    def health(self, new_health: int) -> None:
        self._health = new_health