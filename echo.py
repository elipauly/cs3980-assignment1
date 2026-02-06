#echo.py

def echo(text: str, repetitions: int = 3) -> str:
    """Imitate a real-world echo."""
    last_three = text[-repetitions:]
    last_two = text[-repetitions+1:]
    last_one = text[-repetitions+2:]
    return (last_three + '\n' + last_two + '\n' + last_one)

if __name__ == "__main__":
    text = input("Yell something at a mountain: ")
    print(echo(text))