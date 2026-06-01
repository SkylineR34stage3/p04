import sys
import typing


def parse_argv(argv: list[str]) -> str | None:
    if len(argv) != 2:
        return None
    return argv[1]


def open_file(filename: str, mode: str = "r") -> typing.IO[str] | None:
    try:
        return open(filename, mode)
    except (OSError) as e:
        sys.stderr.write(f"[STDERR] Error opening file '{filename}': {e}")
        sys.stderr.flush()
        return None


def cat_file(f: typing.IO[str], filename: str) -> bool | None:
    try:
        print(f"---\n\n{f.read()}\n\n---")
        return True
    except OSError as e:
        sys.stderr.write(f"[STDERR] Error occurred while reading a file: {e}")
        sys.stderr.flush()
        return None
    finally:
        f.close()
        print(f"File '{filename}' closed.")


def transform_file(f: typing.IO[str]) -> str:
    lines = f.read().splitlines()
    transformed = [line + "#" for line in lines]
    return "\n".join(transformed)


def write_file(f: typing.IO[str], content: str) -> int | None:
    try:
        return f.write(content)
    except OSError as e:
        sys.stderr.write(
            f"[STDERR] Error occurred while writing to a file: {e}"
            )
        sys.stderr.flush()
        return None
    finally:
        f.close()


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
    if cat_file(f, filename) is None:
        return None
    return filename


def transform(filename: str) -> None:
    print("\nTransform data:")
    f = open_file(filename)
    if f is None:
        return

    f_content = transform_file(f)
    f.close()
    print(f"---\n\n{f_content}\n\n---")

    new_file = input("Enter new file name (or empty): ")
    if not new_file:
        print("Not saving data.")
        return
    f = open_file(new_file, "w")
    if f is None:
        return
    print(f"Saving data to '{new_file}'")
    if write_file(f, f_content) is not None:
        print(f"Data saved in file '{new_file}'.")


def main() -> None:
    filename = access()
    if not filename:
        return

    transform(filename)


if __name__ == "__main__":
    main()
