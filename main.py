from models import State, Car


class Controller:

    def __init__(self, start_state: State, board_width, board_height):
        self.leaves = set()
        self.leaves.add(start_state)
        self.closed = set()
        self.game_width = board_width
        self.game_height = board_height

    def sort_leaves(self):
        self.leaves.sort(key=lambda x: x.depth + x.heuristic, reverse=True)

    def solve(self):

        while self.leaves:
            self.sort_leaves()
            selected = self.leaves.pop()
            self.closed.add(selected)
            if selected.is_goal():
                print(selected.depth + 1)
                return
            next_states = selected.generate_next_states()
            next_states = list(filter(lambda x: x not in self.leaves + list(self.closed), next_states))
            # we can get the leaves var as a set. also for closed.
            self.leaves += next_states

        print(-1)
        return


def initialize():
    coordinates = list(map(int, input().split()))
    cars_no, game_width, game_height = coordinates[0], coordinates[1], coordinates[2]

    def get_car_status(input_string):
        input_string = input_string.split()
        return [int(input_string[0]), int(input_string[1]), input_string[2] == 'v', int(input_string[3])]

    start_cars = []
    for i in range(cars_no):
        start_cars.append(Car(*get_car_status(input())))

    start_state = State(start_cars, 0, game_width, game_height)
    Controller(start_state, game_width, game_height).solve()


initialize()
