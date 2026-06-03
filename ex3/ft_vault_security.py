def secure_archive(
        filename: str,
        mode: str = "r",
        content: str | None = None
        ) -> tuple[bool, str]:
    try:
        with open(filename, mode) as f:
            if mode == "r":
                return (True, str(f.read()))
            elif mode == "w":
                f.write(content)
                return (True, "Content successfully written to file")
            else:
                return (False, f"Unknown mode '{mode}'")
    except OSError as e:
        return (False, str(e))
    except TypeError as e:
        return (False, f"No content provided for write: {e}")


def main() -> None:
    print("=== Cyber Archives Security ===")

    print("Using 'secure_archive' to read from a nonexistent file:")
    print(secure_archive("not/existing"))

    print("\nUsing 'secure_archive' to read from an inaccessible file:")
    print(secure_archive("no_access"))

    print("\nUsing 'secure_archive' with wrong mode:")
    print(secure_archive("ancient_fragment.txt", "a"))

    print("\nUsing 'secure_archive' to read from a regular file:")
    output = secure_archive("ancient_fragment.txt")
    print(output)

    print("\nUsing 'secure_archive' to write previous content to a new file:")
    print(secure_archive("new_file.txt", "w", output[1]))


if __name__ == "__main__":
    main()
