#!/usr/bin/env python3
"""
Upscale all JPGs in the mindmaps/ directory.

Uses PIL Lanczos (best-in-class for line art / text) + unsharp mask to
restore crispness lost in the original JPEG compression.

Usage:
    python scripts/upscale_mindmaps.py              # default: 4x, output to mindmaps_hd/
    python scripts/upscale_mindmaps.py --scale 3    # 3x upscale
    python scripts/upscale_mindmaps.py --replace    # overwrite originals in mindmaps/
    python scripts/upscale_mindmaps.py --format png # save as lossless PNG
"""

import argparse
from pathlib import Path

from PIL import Image, ImageFilter


REPO_ROOT = Path(__file__).resolve().parent.parent
MINDMAPS_DIR = REPO_ROOT / "mindmaps"


def upscale(src: Path, dst: Path, scale: int, fmt: str) -> tuple[tuple, tuple]:
    img = Image.open(src).convert("RGB")
    orig_size = img.size

    new_size = (img.width * scale, img.height * scale)
    img = img.resize(new_size, Image.LANCZOS)

    # Unsharp mask: restores edge crispness lost in the original JPEG compression
    img = img.filter(ImageFilter.UnsharpMask(radius=1.5, percent=120, threshold=2))

    dst.parent.mkdir(parents=True, exist_ok=True)
    if fmt == "png":
        out_path = dst.with_suffix(".png")
        img.save(out_path, format="PNG", optimize=True)
    else:
        out_path = dst.with_suffix(".jpg")
        img.save(out_path, format="JPEG", quality=95, subsampling=0)

    return orig_size, new_size


def main() -> None:
    parser = argparse.ArgumentParser(description="Upscale mindmap images")
    parser.add_argument("--scale", type=int, default=4, choices=[2, 3, 4],
                        help="Upscale factor (default: 4)")
    parser.add_argument("--replace", action="store_true",
                        help="Overwrite originals instead of writing to mindmaps_hd/")
    parser.add_argument("--format", choices=["jpg", "png"], default="jpg",
                        help="Output format (default: jpg at quality=95)")
    args = parser.parse_args()

    sources = sorted(MINDMAPS_DIR.glob("*.jpg"))
    if not sources:
        print("No JPG files found in mindmaps/")
        return

    out_dir = MINDMAPS_DIR if args.replace else REPO_ROOT / "mindmaps_hd"

    print(f"Upscaling {len(sources)} images at {args.scale}x -> {out_dir}/")
    print()

    for src in sources:
        dst = out_dir / src.name
        orig, new = upscale(src, dst, args.scale, args.format)
        print(f"  {src.name:55s}  {orig[0]}x{orig[1]} -> {new[0]}x{new[1]}")

    print()
    print("Done.")


if __name__ == "__main__":
    main()
