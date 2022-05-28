import copy


class Car:

    def __init__(self, x: int, y: int, is_vertical: bool, length: int):
        self.x = x
        self.y = y
        self.is_vertical = is_vertical
        self.length = length


class State:

    def __init__(self, cars: list, depth: int, width: int, height: int):
        self.cars = cars
        self.depth = depth
        self.width = width
        self.height = height
        self.state_map = self.get_state_map()
        self.heuristic = self.calculate_heuristic()
        self.next_states = []

    def get_state_map(self):
        blank_map = [[0 for i in range(self.height)] for j in range(self.width)]
        for car in self.cars:
            for i in range(car.length):
                if car.is_vertical:
                    blank_map[car.x][car.y + i] = self.cars.index(car) + 1
                else:
                    blank_map[car.x + i][car.y] = self.cars.index(car) + 1
        return blank_map

    def calculate_heuristic(self):
        red_car = self.cars[0]
        grade = 0
        for i in range(len(list(range(red_car.x + 2, self.width)))):
            if self.state_map[red_car.x + 2 + i][red_car.y]:
                grade += 1
        return grade

    def is_goal(self):
        return self.heuristic == 0

    def create_next_state(self, moved_car_index, new_x, new_y):
        new_cars = [copy.deepcopy(car) for car in self.cars]
        new_cars[moved_car_index].x = new_x
        new_cars[moved_car_index].y = new_y
        return State(new_cars, self.depth + 1, self.width, self.height)

    def generate_next_states(self):
        self.next_states = []
        for car in self.cars:
            if car.is_vertical:
                for i in range(car.y):
                    if not self.state_map[car.x][car.y - (i + 1)]:
                        self.next_states.append(self.create_next_state(self.cars.index(car), car.x, car.y - (i + 1)))
                    else:
                        break
                for j in range(self.height - car.y - car.length):
                    if not self.state_map[car.x][car.y + car.length + j]:
                        self.next_states.append(self.create_next_state(self.cars.index(car), car.x, car.y + j + 1))
                    else:
                        break
            else:
                for i in range(car.x):
                    if not self.state_map[car.x - (i + 1)][car.y]:
                        self.next_states.append(self.create_next_state(self.cars.index(car), car.x - (i + 1), car.y))
                    else:
                        break

                for j in range(self.width - car.x - car.length):
                    if not self.state_map[car.x + car.length + j][car.y]:
                        self.next_states.append(self.create_next_state(self.cars.index(car), car.x + j + 1, car.y))
                    else:
                        break
        return self.next_states

    def __eq__(self, other):
        return self.state_map == other.state_map
