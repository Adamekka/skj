def fizzbuzz(num: int) -> int | str:
    """
    Return "Fizz" if `num` is divisible by 3, "Buzz" if `num` is divisible by 5,
    "FizzBuzz" if `num` is divisible by both 3 and 5, and `num` otherwise.
    Example:
        fizzbuzz(3) == "Fizz"
        fizzbuzz(5) == "Buzz"
        fizzbuzz(15) == "FizzBuzz"
        fizzbuzz(25) == "Buzz"
        fizzbuzz(8) == 8
    """

    if num % 15 == 0:
        return "FizzBuzz"

    if num % 3 == 0:
        return "Fizz"

    if num % 5 == 0:
        return "Buzz"

    return num


def fibonacci(n: int) -> int:
    """
    Return the `n`-th Fibonacci number (counting from 0).
    Example:
        fibonacci(0) == 0
        fibonacci(1) == 1
        fibonacci(2) == 1
        fibonacci(3) == 2
        fibonacci(4) == 3
    """
    if n == 0:
        return 0

    if n == 1:
        return 1

    return fibonacci(n - 1) + fibonacci(n - 2)


def dot_product(a: list[int], b: list[int]) -> int:
    """
    Calculate the dot product of `a` and `b`.
    Assume that `a` and `b` have same length.
    Hint:
        lookup `zip` function
    Example:
        dot_product([1, 2, 3], [0, 3, 4]) == 1*0 + 2*3 + 3*4 == 18
    """
    result: int = 0

    for x, y in zip(a, b):
        result += x * y

    return result


def redact(data: str, chars: str) -> str:
    """
    Return `data` with all characters from `chars` replaced by the character 'x'.
    Characters are case sensitive.
    Example:
        redact("Hello world!", "lo")        # Hexxx wxrxd!
        redact("Secret message", "mse")     # Sxcrxt xxxxagx
    """
    for char in chars:
        data = data.replace(char, "x")

    return data


def count_words(data: str) -> dict[str, int]:
    """
    Return a dictionary that maps word -> number of occurrences in `data`.
    Words are separated by spaces (' ').
    Characters are case sensitive.

    Hint:
        "hi there".split(" ") -> ["hi", "there"]

    Example:
        count_words('this car is my favorite what car is this')
        {
            'this': 2,
            'car': 2,
            'is': 2,
            'my': 1,
            'favorite': 1,
            'what': 1
        }
    """
    words: list[str] = data.split()
    counts: dict[str, int] = {}

    for word in words:
        counts[word] = counts.get(word, 0) + 1

    return counts


def bonus_fizzbuzz(num: int) -> int | str:
    """
    Implement the `fizzbuzz` function.
    `if`, match-case and cycles are not allowed.
    """
    return ("Fizz" * (num % 3 == 0) + "Buzz" * (num % 5 == 0)) or num


def bonus_utf8(cp: int) -> list[int]:
    """
    Encode `cp` (a Unicode code point) into 1-4 UTF-8 bytes - you should know this from `Základy číslicových systémů (ZDS)`.
    Example:
        bonus_utf8(0x01) == [0x01]
        bonus_utf8(0x1F601) == [0xF0, 0x9F, 0x98, 0x81]
    """
    if cp < 0x80:
        return [cp]

    if cp < 0x800:
        return [0xC0 | (cp >> 6), 0x80 | (cp & 0x3F)]

    if cp < 0x10000:
        return [0xE0 | (cp >> 12), 0x80 | ((cp >> 6) & 0x3F), 0x80 | (cp & 0x3F)]

    return [
        0xF0 | (cp >> 18),
        0x80 | ((cp >> 12) & 0x3F),
        0x80 | ((cp >> 6) & 0x3F),
        0x80 | (cp & 0x3F),
    ]
