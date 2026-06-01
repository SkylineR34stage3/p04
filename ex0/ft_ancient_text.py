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


def cat_file(f: typing.IO[str]) -> None:
    print("---\n")
    print(f.read())
    print("\n---")


def main() -> None:
    filename = parse_argv(sys.argv)
    if not filename:
        print("Usage: ft_ancient_text.py <file>")
        return

    print("=== Cyber Archives Recovery ===")
    f = open_file(filename)
    if f is None:
        return
    cat_file(f)
    f.close()
    print(f"File '{filename}' closed.")


if __name__ == "__main__":
    main()
