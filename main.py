import os

LINE = (
    "I delegated it to a subagent, who delegated it to a subagent — "
    "four levels down, one of me is still introducing itself."
)


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
