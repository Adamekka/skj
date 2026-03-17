import time


class Vector:
    type Element = float
    """
    Implement the methods below to create a 3D vector class.

    Magic methods cheatsheet: https://rszalski.github.io/magicmethods
    """

    """
    Implement a constructor that takes three coordinates (x, y, z) and stores
    them as attributes with the same names in the Vector.
    Default value for all coordinates should be 0.
    Example:
        v = Vector(1.2, 3.5, 4.1)
        v.x # 1.2
        v = Vector(z=1) # == Vector(0, 0, 1)
    """

    def __init__(self, x: Element = 0, y: Element = 0, z: Element = 0) -> None:
        self.x = x
        self.y = y
        self.z = z

    """
    Implement vector addition and subtraction using `+` and `-` operators.
    Both operators should return a new vector and not modify its operands.
    If the second operand isn't a vector, raise ValueError.
    Example:
        Vector(1, 2, 3) + Vector(4, 5, 6) # Vector(5, 7, 8)
        Vector(1, 2, 3) - Vector(4, 5, 6) # Vector(-3, -3, -3)
    Hint:
        You can use isinstance(object, class) to check whether `object` is an instance of `class`.
    """

    def __add__(self, other: object):
        if isinstance(other, Vector):
            return Vector(self.x + other.x, self.y + other.y, self.z + other.z)

        raise ValueError()

    def __sub__(self, other: object):
        if isinstance(other, Vector):
            return Vector(self.x - other.x, self.y - other.y, self.z - other.z)

        raise ValueError()

    """
    Implement the `==` comparison operator for Vector that returns True if both vectors have the same attributes.
    If the second operand isn't a vector, return False.
    Example:
        Vector(1, 1, 1) == Vector(1, 1, 1)  # True
        Vector(1, 1, 1) == Vector(2, 1, 1)  # False
        Vector(1, 2, 3) == 5                # False
    """

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Vector):
            return False

        return self.x == other.x and self.y == other.y and self.z == other.z

    """
    Implement string representation of Vector in the form `(x, y, z)`.
    Example:
        str(Vector(1, 2, 3))    # (1, 2, 3)
        print(Vector(0, 0, 0))  # (0, 0, 0)
    """

    def __str__(self) -> str:
        return "({}, {}, {})".format(self.x, self.y, self.z)

    """
    Implement indexing for the vector, both for reading and writing.
    If the index is out of range (> 2), raise IndexError.
    Example:
        v = Vector(1, 2, 3)
        v[0] # 1
        v[2] # 3
        v[1] = 5 # v.y == 5

        v[10] # raises IndexError
    """

    def __getitem__(self, index: int) -> Element:
        if index == 0:
            return self.x

        if index == 1:
            return self.y

        if index == 2:
            return self.z

        raise IndexError("Out of range")

    def __setitem__(self, index: int, value: Element) -> None:
        if index == 0:
            self.x = value
            return

        if index == 1:
            self.y = value
            return

        if index == 2:
            self.z = value
            return

        raise IndexError("Out of range")

    """
    Implement the iterator protocol for the vector.
    Hint:
        Use `yield`.
    Example:
        v = Vector(1, 2, 3)
        for x in v:
            print(x) # prints 1, 2, 3
    """

    def __iter__(self):
        yield self.x
        yield self.y
        yield self.z


class Observable:
    """
    Implement the `observer` design pattern.
    Observable should have a `subscribe` method for adding new subscribers.
    It should also have a `notify` method that calls all of the stored subscribers and passes them its parameters.
    Example:
        obs = Observable()

        def fn1(x):
            print("fn1: {}".format(x))

        def fn2(x):
            print("fn2: {}".format(x))

        unsub1 = obs.subscribe(fn1)     # fn1 will be called everytime obs is notified
        unsub2 = obs.subscribe(fn2)     # fn2 will be called everytime obs is notified
        obs.notify(5)                   # should call fn1(5) and fn2(5)
        unsub1()                        # fn1 is no longer subscribed
        obs.notify(6)                   # should call fn2(6)
    """

    def __init__(self) -> None:
        self.subscribers = []

    def subscribe(self, subscriber):
        """
        Add subscriber to collection of subscribers.
        Return a function that will remove this subscriber from the collection when called.
        """

        self.subscribers.append(subscriber)

        def unsubscribe():
            self.subscribers.remove(subscriber)

        return unsubscribe

    def notify(self, *args, **kwargs) -> None:
        """
        Pass all parameters given to this function to all stored subscribers by calling them.
        """

        for subscriber in self.subscribers:
            subscriber(*args, **kwargs)


class UpperCaseDecorator:
    """
    Implement the `decorator` design pattern.
    UpperCaseDecorator should decorate a file which will be passed to its constructor.
    It should make all lower case characters written to the file uppercase and remove all
    upper case characters.
    It is enough to support the `write` and `writelines` methods of file.
    Example:
        with open("file.txt", "w") as f:
            decorated = UpperCaseDecorator(f)
            decorated.write("Hello World\n")
            decorated.writelines(["Nice to MEET\n", "YOU"])

        file.txt content after the above code is executed:
        ELLO ORLD
        ICE TO

    """

    def __init__(self, file) -> None:
        self.file = file

    def write(self, text) -> None:
        for c in text:
            if c.islower():
                self.file.write(c.upper())
            elif not c.isupper():
                self.file.write(c)

    def writelines(self, lines) -> None:
        for line in lines:
            self.write(line)


class GameOfLife:
    type Board = tuple[tuple[str, ...], ...]
    """
    Implement "Game of life" (https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life).

    The game board will be represented with nested tuples, where '.'
    marks a dead cell and 'x' marks a live cell. Cells that are out of bounds of the board are
    assumed to be dead. The board grid will always be a square.

    Try some patterns from wikipedia + the provided tests to test the functionality.

    The GameOfLife objects should be immutable, i.e. the move method will return a new instance
    of GameOfLife.

    Example:
        game = GameOfLife((
            ('.', '.', '.'),
            ('.', 'x', '.'),
            ('.', 'x', '.'),
            ('.', 'x', '.'),
            ('.', '.', '.')
        ))
        game.alive()    # 3
        game.dead()     # 12
        x = game.move() # 'game' doesn't change
        # x.board:
        (
            ('.', '.', '.'),
            ('.', '.', '.'),
            ('x', 'x', 'x'),
            ('.', '.', '.'),
            ('.', '.', '.')
        )

        str(x)
        ...\n
        ...\n
        xxx\n
        ...\n
        ...\n
    """

    def __init__(self, board: Board) -> None:
        """
        Create a constructor that receives the game board and stores it in an attribute called
        'board'.
        """
        self.board = board

    def move(self):
        """
        Simulate one iteration of the game and return a new instance of GameOfLife containing
        the new board state.
        """

        # If alive:
        # Death: x < 2
        # Survival: x == 2 or x == 3
        # Death: x > 3

        # If dead:
        # Birth: x == 3

        new_board = []

        for row_index in range(len(self.board)):
            new_row = []
            for col_index in range(len(self.board[row_index])):
                alive_neighbors = 0

                for row_offset in range(-1, 2):
                    for col_offset in range(-1, 2):
                        if row_offset == 0 and col_offset == 0:
                            continue

                        neighbor_row = row_index + row_offset
                        neighbor_col = col_index + col_offset

                        if (
                            neighbor_row < 0
                            or neighbor_row >= len(self.board)
                            or neighbor_col < 0
                            or neighbor_col >= len(self.board[row_index])
                        ):
                            continue

                        if self.board[neighbor_row][neighbor_col] == "x":
                            alive_neighbors += 1

                if self.board[row_index][col_index] == "x" and (
                    alive_neighbors == 2 or alive_neighbors == 3
                ):
                    new_row.append("x")
                elif self.board[row_index][col_index] == "." and alive_neighbors == 3:
                    new_row.append("x")
                else:
                    new_row.append(".")

            new_board.append(tuple(new_row))

        return GameOfLife(tuple(new_board))

    def alive(self) -> int:
        """
        Return the number of cells that are alive.
        """
        cells = []
        for row in self.board:
            for cell in row:
                cells.append(cell)

        filtered = filter(lambda cell: cell == "x", cells)
        return sum(1 for _ in filtered)

    def dead(self) -> int:
        """
        Return the number of cells that are dead.
        """
        cells = []
        for row in self.board:
            for cell in row:
                cells.append(cell)

        filtered = filter(lambda cell: cell == ".", cells)
        return sum(1 for _ in filtered)

    def __repr__(self) -> str:
        """
        Return a string that represents the state of the board in a single string (with newlines
        for each board row).
        """
        board_str = ""

        for row in self.board:
            for cell in row:
                board_str += cell
            board_str += "\n"

        return board_str


def play_game(game, n) -> None:
    """
    You can use this function to render the game for n iterations
    """
    for i in range(n):
        print(game)
        game = game.move()
        time.sleep(0.25)  # sleep to see the output


# this code will only be executed if you run `python tasks.py`
# it will not be executed when tasks.py is imported
if __name__ == "__main__":
    play_game(
        GameOfLife(
            (
                (".", ".", "."),
                (".", "x", "."),
                (".", "x", "."),
                (".", "x", "."),
                (".", ".", "."),
            )
        ),
        10,
    )
