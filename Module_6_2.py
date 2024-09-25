class Vehicle:
    owner = 'Fedos'
    _model = 'Toyota Mark II'
    __engine_power = 500
    __color = 'blue'
    __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']
    def get_model(self):
        print(f'Модель: {self._model}.')

    def get_horsepower(self):
        print(f'Мощьность двигателя: {self.__engine_power}.')

    def get_color(self):
        print(f'Цвет: {self.__color}.')

    def print_info(self):
        print(f'{self.get_model()} \n{self.get_horsepower()} \n{self.get_color()}')

    def set_color(self, new_color):
        self.new_color =new_color
        if self.new_color in self.__COLOR_VARIANTS:
            self.__color = new_color
            print(f'{new_color.upper()}')




class Sedan(Vehicle):
    __PASSENGERS_LIMIT = 5


# Текущие цвета __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']
vehicle1 = Sedan()
# Изначальные свойства
vehicle1.print_info()
# Меняем свойства (в т.ч. вызывая методы)
vehicle1.set_color('Pink')
vehicle1.set_color('BLACK')
vehicle1.owner = 'Vasyok'
# Проверяем что поменялось
vehicle1.print_info()