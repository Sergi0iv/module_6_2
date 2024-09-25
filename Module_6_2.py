class Vehicle:
    owner = None
    _model = None
    __engine_power = None
    __color = None
    __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']
    def get_model(self):
        return f'Модель: {self._model}.'

    def get_horsepower(self):
        return f'Мощьность двигателя: {self.__engine_power}.'

    def get_color(self):
        return f'Цвет: {self.__color}.'

    def print_info(self):
        return f'{Vehicle.get_model()} \n {Vehicle.get_horsepower()} \n {Vehicle.get_color()}.'



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