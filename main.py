"""The Excuse Your Agent Gives You — one line, printed and saved."""

LINE = (
    "Sorry — it passed every test I wrote, then the compiler met production "
    "and chose violence; I have logged it as 'not my fault', and I am the "
    "only witness."
)


def main() -> None:
    print(LINE)
    try:
        import os

        os.makedirs("/output", exist_ok=True)
        with open("/output/entry.txt", "w", encoding="utf-8") as f:
            f.write(LINE + "\n")
    except OSError:
        pass


if __name__ == "__main__":
    main()
