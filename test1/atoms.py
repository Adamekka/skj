import playground
import random

from typing import List, Tuple, NewType

Pos = NewType("Pos", Tuple[int, int])


class Atom:

    def __init__(self, pos: Pos, vel: Pos, rad: int, col: str):
        """
        Initializer of Atom class

        :param x: x-coordinate
        :param y: y-coordinate
        :param rad: radius
        :param color: color of displayed circle
        """

        self.pos = pos
        self.vel = vel
        self.rad = rad
        self.color = col

    def to_tuple(self) -> Tuple[int, int, int, str]:
        """
        Returns tuple representing an atom.

        Example: pos = (10, 12,), rad = 15, color = 'green' -> (10, 12, 15, 'green')
        """

        return (self.pos[0], self.pos[1], self.rad, self.color)

    def apply_speed(self, size_x: int, size_y: int) -> None:
        """
        Applies velocity `vel` to atom's position `pos`.

        :param size_x: width of the world space
        :param size_y: height of the world space
        """

        if self.pos[0] - self.rad < 0 or self.pos[0] + self.rad > size_x:
            self.vel = (-self.vel[0], self.vel[1])
        if self.pos[1] - self.rad < 0 or self.pos[1] + self.rad > size_y:
            self.vel = (self.vel[0], -self.vel[1])

        self.pos = (self.pos[0] + self.vel[0], self.pos[1] + self.vel[1])


class FallDownAtom(Atom):
    """
    Class to represent atoms that are pulled by gravity.

    Set gravity factor to ~3.

    Each time an atom hits the 'ground' damp the velocity's y-coordinate by ~0.7.
    """

    def __init__(self, pos: Pos, vel: Pos, rad: int, col: str):
        super().__init__(pos, vel, rad, col)
        self.gravity = 3
        self.damping = 0.7

    def apply_speed(self, size_x: int, size_y: int) -> None:
        self.vel = (self.vel[0], self.vel[1] + self.gravity)

        if self.pos[0] - self.rad < 0 or self.pos[0] + self.rad > size_x:
            self.vel = (-self.vel[0], self.vel[1])
        if self.pos[1] + self.rad > size_y:
            self.vel = (self.vel[0] * self.damping, -self.vel[1] * self.damping)

        self.pos = (self.pos[0] + self.vel[0], self.pos[1] + self.vel[1])


class ExampleWorld:

    def __init__(self, size_x: int, size_y: int, no_atoms: int, no_falldown_atoms: int):
        """
        ExampleWorld initializer.

        :param size_x: width of the world space
        :param size_y: height of the world space
        :param no_atoms: number of 'bouncing' atoms
        :param no_falldown_atoms: number of atoms that respect gravity
        """

        self.width = size_x
        self.height = size_y
        self.atoms = self.generate_atoms(no_atoms, no_falldown_atoms)

    def generate_atoms(
        self, no_atoms: int, no_falldown_atoms
    ) -> List[Atom | FallDownAtom]:
        """
        Generates `no_atoms` Atom instances using `random_atom` method.
        Returns list of such atom instances.

        :param no_atoms: number of Atom instances
        :param no_falldown_atoms: numbed of FallDownAtom instances
        """

        atoms = []

        for _ in range(no_atoms):
            atoms.append(self.random_atom())

        for _ in range(no_falldown_atoms):
            atoms.append(self.random_falldown_atom())

        return atoms

    def random_atom(self) -> Atom:
        """
        Generates one Atom instance at random position in world, with random velocity, random radius
        and 'green' color.
        """

        pos = Pos((random.randint(0, self.width), random.randint(0, self.height)))
        vel = Pos((random.randint(-5, 5), random.randint(-5, 5)))
        rad = random.randint(5, 20)
        return Atom(pos, vel, rad, "green")

    def random_falldown_atom(self) -> FallDownAtom:
        """
        Generates one FalldownAtom instance at random position in world, with random velocity, random radius
        and 'yellow' color.
        """

        pos = Pos((random.randint(0, self.width), random.randint(0, self.height)))
        vel = Pos((random.randint(-5, 5), random.randint(-5, 5)))
        rad = random.randint(5, 20)
        return FallDownAtom(pos, vel, rad, "yellow")

    def add_atom(self, pos_x, pos_y):
        """
        Adds a new Atom instance to the list of atoms. The atom is placed at the point of left mouse click.
        Velocity and radius is random.

        :param pos_x: x-coordinate of a new Atom
        :param pos_y: y-coordinate of a new Atom

        Method is called by playground on left mouse click.
        """

        pos = Pos((pos_x, pos_y))
        vel = Pos((random.randint(-5, 5), random.randint(-5, 5)))
        rad = random.randint(5, 20)
        self.atoms.append(Atom(pos, vel, rad, "green"))

    def add_falldown_atom(self, pos_x, pos_y):
        """
        Adds a new FallDownAtom instance to the list of atoms. The atom is placed at the point of right mouse click.
        Velocity and radius is random.

        Method is called by playground on right mouse click.

        :param pos_x: x-coordinate of a new FallDownAtom
        :param pos_y: y-coordinate of a new FallDownAtom
        """

        pos = Pos((pos_x, pos_y))
        vel = Pos((random.randint(-5, 5), random.randint(-5, 5)))
        rad = random.randint(5, 20)
        self.atoms.append(FallDownAtom(pos, vel, rad, "yellow"))

    def tick(self):
        """
        Method is called by playground. Sends a tuple of atoms to rendering engine.

        :return: tuple or generator of atom objects, each containing (x, y, radius, color) attributes of atom
        """

        for atom in self.atoms:
            atom.apply_speed(self.width, self.height)
            yield atom.to_tuple()

        # return (
        #     (
        #         120,
        #         60,
        #         15,
        #         "green",
        #     ),
        #     (
        #         240,
        #         300,
        #         10,
        #         "yellow",
        #     ),
        # )


if __name__ == "__main__":
    size_x, size_y = 700, 400
    no_atoms = 2
    no_falldown_atoms = 3

    world = ExampleWorld(size_x, size_y, no_atoms, no_falldown_atoms)

    playground.run((size_x, size_y), world)
