"""
Invisible Watermark Detector & Emoji Injector
Reads text from input_text.txt in the same folder as this script.
Detects zero-width / invisible Unicode characters used as text watermarks
and wraps each watermark region with emojis to make them visible.
"""

from pathlib import Path

# ── Unicode ranges that are "invisible" ──────────────────────────────────────
INVISIBLE_CHARS = {
    "\u200b": "ZERO WIDTH SPACE",
    "\u200c": "ZERO WIDTH NON-JOINER",
    "\u200d": "ZERO WIDTH JOINER",
    "\u200e": "LEFT-TO-RIGHT MARK",
    "\u200f": "RIGHT-TO-LEFT MARK",
    "\u202a": "LEFT-TO-RIGHT EMBEDDING",
    "\u202b": "RIGHT-TO-LEFT EMBEDDING",
    "\u202c": "POP DIRECTIONAL FORMATTING",
    "\u202d": "LEFT-TO-RIGHT OVERRIDE",
    "\u202e": "RIGHT-TO-LEFT OVERRIDE",
    "\u2060": "WORD JOINER",
    "\u2061": "FUNCTION APPLICATION",
    "\u2062": "INVISIBLE TIMES",
    "\u2063": "INVISIBLE SEPARATOR",
    "\u2064": "INVISIBLE PLUS",
    "\ufeff": "ZERO WIDTH NO-BREAK SPACE (BOM)",
    "\u00ad": "SOFT HYPHEN",
    "\u034f": "COMBINING GRAPHEME JOINER",
    "\u17b4": "KHMER VOWEL INHERENT AQ",
    "\u17b5": "KHMER VOWEL INHERENT AA",
    "\u115f": "HANGUL CHOSEONG FILLER",
    "\u1160": "HANGUL JUNGSEONG FILLER",
    "\u3164": "HANGUL FILLER",
    "\ufe00": "VARIATION SELECTOR-1",
    "\ufe01": "VARIATION SELECTOR-2",
    "\ufe02": "VARIATION SELECTOR-3",
    "\ufe03": "VARIATION SELECTOR-4",
    "\ufe04": "VARIATION SELECTOR-5",
    "\ufe05": "VARIATION SELECTOR-6",
    "\ufe06": "VARIATION SELECTOR-7",
    "\ufe07": "VARIATION SELECTOR-8",
    "\ufe08": "VARIATION SELECTOR-9",
    "\ufe09": "VARIATION SELECTOR-10",
    "\ufe0a": "VARIATION SELECTOR-11",
    "\ufe0b": "VARIATION SELECTOR-12",
    "\ufe0c": "VARIATION SELECTOR-13",
    "\ufe0d": "VARIATION SELECTOR-14",
    "\ufe0e": "VARIATION SELECTOR-15",
    "\ufe0f": "VARIATION SELECTOR-16",
}

EMOJI_START = "🔍"
EMOJI_END   = "🔍"
SEPARATOR   = "|"   # separates multiple watermark runs


def analyze_text(text: str) -> dict:
    """Return stats about invisible characters found in *text*."""
    found: dict[str, list[int]] = {}
    for i, ch in enumerate(text):
        if ch in INVISIBLE_CHARS:
            name = INVISIBLE_CHARS[ch]
            found.setdefault(name, []).append(i)
    return found


def inject_emojis(text: str) -> str:
    """
    Wrap each contiguous run of invisible characters with EMOJI_START … EMOJI_END.
    The invisible chars themselves are replaced with their hex code points so
    you can actually see what was hidden.
    """
    result = []
    in_watermark = False
    watermark_buf = []

    for ch in text:
        if ch in INVISIBLE_CHARS:
            if not in_watermark:
                in_watermark = True
                watermark_buf = []
            watermark_buf.append(f"<U+{ord(ch):04X}>")
        else:
            if in_watermark:
                # Close previous watermark run
                result.append(EMOJI_START)
                result.append(SEPARATOR.join(watermark_buf))
                result.append(EMOJI_END)
                in_watermark = False
                watermark_buf = []
            result.append(ch)

    # Edge case: text ends while still inside a watermark run
    if in_watermark:
        result.append(EMOJI_START)
        result.append(SEPARATOR.join(watermark_buf))
        result.append(EMOJI_END)

    return "".join(result)


def strip_invisible(text: str) -> str:
    """Return a clean copy of *text* with all invisible chars removed."""
    return "".join(ch for ch in text if ch not in INVISIBLE_CHARS)


def print_report(text: str) -> None:
    stats = analyze_text(text)
    total = sum(len(v) for v in stats.values())

    print("\n" + "═" * 60)
    if not stats:
        print("✅  No invisible watermark characters detected.")
    else:
        print(f"⚠️   {total} invisible character(s) found in {len(stats)} category/categories:\n")
        for name, positions in stats.items():
            hex_vals = [f"U+{ord(text[p]):04X}" for p in positions]
            print(f"  • {name}")
            print(f"    positions : {positions}")
            print(f"    codepoints: {', '.join(hex_vals)}")
        print()
        print("── Text with emojis injected around watermarks ──")
        print(inject_emojis(text))
        print()
        print("── Clean text (invisible chars stripped) ──")
        print(strip_invisible(text))
    print("═" * 60 + "\n")


# ── CLI entry point ───────────────────────────────────────────────────────────
def main() -> None:
    script_dir = Path(__file__).parent
    input_file = script_dir / "input_text.txt"

    print("╔══════════════════════════════════════════════════════════╗")
    print("║   Invisible Watermark Detector & Emoji Injector          ║")
    print("╚══════════════════════════════════════════════════════════╝\n")

    if not input_file.exists():
        print(f"❌  File not found: {input_file}")
        print("    Create 'input_text.txt' in the same folder as this script and re-run.")
        return

    text = input_file.read_text(encoding="utf-8")
    print(f"📄  Read {len(text)} character(s) from '{input_file.name}'\n")
    print_report(text)


if __name__ == "__main__":
    main()