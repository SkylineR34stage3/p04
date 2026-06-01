import sys
import typing


def parse_argv(argv: list[str]) -> str | None:
    if len(argv) != 2:
        return None
    return argv[1]


def open_file(filename: str) -> typing.IO[str] | None:
    try:
        return open(filename, "r")
    except (OSError) as e:
        print(f"Error opening file '{filename}': {e}")
        return None


def cat_file(f: typing.IO[str]) -> None:
    print("---\n")
    print(f.read())
    print("\n---")


def access() -> str | None:
    filename = parse_argv(sys.argv)
    if not filename:
        print("Usage: ft_ancient_text.py <file>")
        return None

    print("=== Cyber Archives Recovery ===")
    print(f"Accessing file '{filename}'")
    f = open_file(filename)
    if f is None:
        return None
    cat_file(f)
    f.close()
    print(f"File '{filename}' closed.")
    return filename


def transform_file(f: typing.IO[str]) -> str:
    lines = f.read().splitlines()
    transformed = [line + "#" for line in lines]
    return "\n".join(transformed)


def transform(filename: str) -> None:
    print("\nTransform data:")
    f = open_file(filename)
    if f is None:
        return None
    
    f_content = transform_file(f)
    print(f"---\n\n{f_content}\n\n---")
    

def main() -> None:
    filename = access()
    if not filename:
        return
    
    transform(filename)


if __name__ == "__main__":
    main()
