import sys
import typing


def parse_argv(argv: list[str]) -> str | None:
    if len(argv) != 2:
        return None
    return argv[1]


def open_file(filename: str) -> typing.IO[str] | None:
    print(f"Accessing file '{filename}'")
    try:
        return open(filename, "r")
    except (OSError) as e:
        print(f"Error opening file '{filename}': {e}")
        return None


def cat_file(f: typing.IO[str], filename: str) -> bool | None:
    try:
        print(f"---\n\n{f.read()}\n\n---")
        return True
    except OSError as e:
        print(f"Error occurred while reading a file: {e}")
        return None
    finally:
        f.close()
        print(f"File '{filename}' closed.")


def main() -> None:
    filename = parse_argv(sys.argv)
    if not filename:
        print("Usage: ft_ancient_text.py <file>")
        return

    print("=== Cyber Archives Recovery ===")
    f = open_file(filename)
    if f is None:
        return
    cat_file(f, filename)


if __name__ == "__main__":
    main()
