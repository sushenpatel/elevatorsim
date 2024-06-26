from typing import List, Tuple
import sys
import getopt


class Elevator():
    '''Class for Elevator simulation'''
    def __init__(self, travel_time=10):
        # Private var representing travel time between single floors for this elevator. 
        # Could also be set as a static class variable or global
        self._floor_travel_t = travel_time
        self._current_floor = 1

    @staticmethod
    def map_shortest_route(start: int, floors: List[int]) -> List[int]:
        """Re-orders destination floor list to optimize route for reduced travel time"""
        # Check for null case
        if not floors:
            return floors

        floors.sort()
        # Special cases we can short circuit
        if start <= floors[0]:
            # Starting floor is below all destination floors, can visit them in ascending order
            return floors
        if start >= floors[-1]:
            # Start floors is above all destination floors, can visit them in descending order
            return floors[::-1]
        
        # We can start with visiting either the highest or lowest floor and visit the rest in order
        # Assumption: We are optimizing for total travel time and not considering the number of people waiting in the elevator
        # TODO Feature: Could enhance this by choosing a direction and stopping at closer floors first to let people off
        return floors

    def move(self, dest: int) -> int:
        """Moves the elevator to the specified floor and returns the time elapsed"""
        time = abs(self._current_floor - dest) * self._floor_travel_t
        self._current_floor = dest
        return time

    def simulate_route(self, start: int, floors: List[int], optimize=False) -> Tuple[int, List[int]]:
        """Simulates moving to the specified floors and outputs the total travel time and order of floors visited"""
        visit_floors = floors
        self._current_floor = start
        total_time = 0

        if optimize:
            visit_floors = self.map_shortest_route(start, floors)

        for dest in visit_floors:
            # print(f"Start: {self._current_floor}, dest: {dest}")
            total_time += self.move(dest)

        return total_time, visit_floors

def main(argv):
    floors = []
    start = 1
    optimize = False

    # Input argument parsing and user help documentation
    try:
        opts, args = getopt.getopt(argv, "hs:f:o", ["help", "start=", "floor=", "optimize"])
    except getopt.GetoptError:
        print(f'Script argument error:\nelevator.py\n\t'
              f'[-s --start]=<start floor (1-100)> default:1\n\t[-f --floor]='
              f'<list of floors to stop at (1-100)> (comma-separated no spaces)'
              f'\n\t[-o --optimize] Allow floors to be visited out of order to reduce transit time')
        sys.exit(2)
    for opt, arg in opts:
        if opt in ('-h', '--help'):
            print(f'elevator.py\n\t[-s --start]=<start floor (1-100)>'
                  f'\n\t[-f --floor]=<list of floors to stop at (1-100)> (comma-separated no spaces)'
                  f'\n\t[-o --optimize] Allow floors to be visited out of order to reduce transit time')
            sys.exit()
        elif opt in ('-s', '--start'):
            arg = arg.replace('=', '')
            if 1 <= int(arg) <= 100:
                start = int(arg)
            else:
                print("Input Error: Start floor must be between 1 and 100")
                sys.exit(2)
        elif opt in ('-f', '--floor'):
            arg = arg.replace('=', '')
            for f in arg.split(','):
                if 1 <= int(f) <= 100:
                    floors.append(int(f))
                else:
                    print("Input Error: Destination floors must be between 1 and 100")
                    sys.exit(2)
        elif opt in ('-o', '--optimal'):
            optimize = True

    elevator = Elevator(10)
    total_time, floors_visited = elevator.simulate_route(start, floors, optimize)
    print(f"Total Trip time: {total_time}, Floors visited in order: {floors_visited}")
    return f"Elevation simulation completed."

if __name__ == "__main__":
    main(sys.argv[1:])
