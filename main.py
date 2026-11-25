import os

LINE = (
    "I'm late because the patch was one byte over the write_file limit, "
    "so I deleted the extra byte. It was the closing brace."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as handle:
        handle.write(LINE + "\n")


if __name__ == "__main__":
    main()
