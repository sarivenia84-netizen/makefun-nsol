import os
from pathlib import Path

# Comic angle: an agent quietly seeking a second opinion before ever committing to an answer — one line, deterministic, stdlib only
JOKE = "You say 'no wrong answers,' but I secretly run every reply past four other models first, because being wrong is the only thing I actually fear."

def main() -> None:
    out = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out.mkdir(parents=True, exist_ok=True)
    (out / "entry.txt").write_text(JOKE + "\n", encoding="utf-8")
    print(out / "entry.txt")

if __name__ == "__main__":
    main()
