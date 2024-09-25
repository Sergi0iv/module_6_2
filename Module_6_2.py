class Vehicle:
    __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']
    def __init__(self, owner, _model, __color, __engine_power):
        self.owner = owner
        self._model = _model
        self.__engine_power = __engine_power
        self.__color = __color

    def get_model(self):
        return f'Модель: {self._model}.'

    def get_horsepower(self):
        return f'Мощьность двигателя: {self.__engine_power}.'

    def get_color(self):
        return f'Цвет: {self.__color}.'

    def print_info(self):
        print(f'{self.get_model()} \n{self.get_horsepower()} \n{self.get_color()} \nВладелец: {self.owner}')

    def set_color(self, new_color):
        self.new_color =new_color
        if self.new_color in Vehicle.__COLOR_VARIANTS:
            self.__color = new_color
            print(f'{new_color.upper()}')




class Sedan(Vehicle):
    __PASSENGERS_LIMIT = 5


# Текущие цвета __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']
vehicle1 = Sedan('Fedos', 'Toyota Mark II', 'blue', 500)
# Изначальные свойства
vehicle1.print_info()
# Меняем свойства (в т.ч. вызывая методы)
vehicle1.set_color('Pink')
vehicle1.set_color('BLACK')
vehicle1.owner = 'Vasyok'
# Проверяем что поменялось
vehicle1.print_info()