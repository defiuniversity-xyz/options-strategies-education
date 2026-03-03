"""
Generate educational concept illustrations for Options Strategies: Statistical Edge Analysis
Using Vertex AI Imagen 4 (imagen-4.0-generate-001)

Usage:
    python3 generate-images.py

Prerequisites:
    pip3 install google-cloud-aiplatform
    gcloud auth application-default login
    gcloud config set project options-strategies-edu
"""

import os
import vertexai
from vertexai.preview.vision_models import ImageGenerationModel

PROJECT_ID = "options-strategies-edu"
LOCATION = "us-central1"
MODEL_ID = "imagen-4.0-generate-001"
OUTPUT_DIR = "images"

IMAGES = [
    {
        "filename": "vrp-concept.png",
        "section": "#foundations — VRP card",
        "prompt": (
            "Abstract dark fintech illustration representing the Volatility Risk Premium — "
            "a sturdy digital vault at the center collecting streams of glowing premium payments flowing inward from all directions, "
            "while smaller uncertain insurance claim symbols drift away in the background, "
            "the vault radiates a calm teal glow suggesting structural advantage, "
            "dark background (#0d1117), teal (#00d9a3) and gold (#f0b429) color accents, "
            "minimalist professional financial data visualization aesthetic, "
            "cinematic depth of field, no text, no watermarks, no labels"
        ),
    },
    {
        "filename": "theta-decay-concept.png",
        "section": "#foundations — Theta Decay card",
        "prompt": (
            "Abstract dark fintech illustration representing theta decay — "
            "a glowing hourglass in the center with premium value visibly dissolving and accelerating toward the bottom, "
            "the upper half is full and golden representing time value remaining, "
            "the lower half shows rapidly accelerating particle erosion in teal, "
            "two faint vertical markers at 45 and 21 DTE glow softly, "
            "dark background, gold and teal color palette, "
            "moody atmospheric lighting, professional fintech data art style, "
            "no text, no watermarks, no labels"
        ),
    },
    {
        "filename": "iv-mean-reversion.png",
        "section": "#foundations — IV Mean Reversion card",
        "prompt": (
            "Abstract dark fintech illustration representing implied volatility mean reversion — "
            "glowing oscillating waves between two hard horizontal boundary lines, "
            "a central glowing teal equilibrium line pulls the waves back toward it like a magnetic force, "
            "the waves show dramatic spikes and then curve back toward the mean, "
            "dark background, teal and gold color accents, "
            "bounded mathematical constraint visualized as glowing containment walls, "
            "professional financial data visualization aesthetic, cinematic, "
            "no text, no watermarks, no labels"
        ),
    },
    {
        "filename": "short-strangle-concept.png",
        "section": "#strangles",
        "prompt": (
            "Abstract dark fintech illustration representing a short strangle options strategy — "
            "two glowing vertical barrier walls on the left and right flanking a wide central corridor of teal profit light, "
            "outside both walls the color shifts to deep red warning zones extending to the edges, "
            "the central profit corridor glows with a calm teal luminescence, "
            "the overall composition feels like a financial force field containing the profit zone, "
            "dark background, teal profit zone, red risk zones, "
            "professional fintech art, atmospheric depth, "
            "no text, no watermarks, no labels"
        ),
    },
    {
        "filename": "jade-lizard-concept.png",
        "section": "#jade-lizard",
        "prompt": (
            "Stylized dark illustration of a jade-green lizard perched on a branch, "
            "the lizard is poised and calm, its right side is bathed in warm teal-green light indicating zero risk, "
            "on the left side a subtle red gradient suggests contained downside risk, "
            "the background shows abstract dark foliage with faint financial data grid overlay, "
            "the art style blends nature illustration with fintech data aesthetics, "
            "jade green, teal, and dark gold color palette, dark moody background, "
            "professional cinematic lighting, "
            "no text, no watermarks, no labels"
        ),
    },
    {
        "filename": "iron-condor-concept.png",
        "section": "#iron-condor",
        "prompt": (
            "Majestic condor bird soaring at altitude, wings fully spread between two defined height boundaries — "
            "a glowing teal ceiling above and a glowing teal floor below — "
            "the bird soars freely in the defined profit space between the boundaries, "
            "beyond the ceiling and floor the atmosphere shifts to deep red warning zones, "
            "dark atmospheric sky background, dramatic lighting, the wingspan precisely touches both boundaries, "
            "teal and gold color accents, professional dark fintech illustration, "
            "cinematic depth, no text, no watermarks, no labels"
        ),
    },
    {
        "filename": "bwb-concept.png",
        "section": "#bwb",
        "prompt": (
            "Dark stylized illustration of a butterfly in flight with one asymmetrically larger broken wing on the left, "
            "the unbroken right wing glows with teal light suggesting zero risk on that side, "
            "the broken left wing has a defined geometric break point highlighted in gold, "
            "the composition conveys deliberate asymmetry as structural advantage, "
            "dark background with subtle financial grid lines, "
            "teal, gold, and dark color palette, professional fintech illustration style, "
            "atmospheric moody lighting, no text, no watermarks, no labels"
        ),
    },
    {
        "filename": "calendar-spread-concept.png",
        "section": "#calendars",
        "prompt": (
            "Dark moody fintech illustration representing a calendar spread — "
            "two calendar pages floating in space at different distances, the near-term calendar is bright and rapidly dissolving into glowing teal particles representing fast theta decay, "
            "the far-term calendar floats in the background, glowing softly in gold, decaying much more slowly, "
            "streams of premium flow from the near-term calendar to the center representing the credit differential, "
            "dark atmospheric background with faint time grid lines, "
            "teal and gold color palette, professional financial art, cinematic depth of field, "
            "no text, no watermarks, no labels"
        ),
    },
    {
        "filename": "put-call-parity.png",
        "section": "#synthetics-foundation",
        "prompt": (
            "Dark minimal fintech illustration of a perfectly balanced scale of justice, "
            "the left pan holds a glowing call option symbol in teal, "
            "the right pan holds a glowing put option symbol in gold, "
            "with a bond and underlying stock floating in equilibrium at the fulcrum, "
            "the scale is perfectly level representing the no-arbitrage equilibrium of put-call parity, "
            "the background shows faint mathematical formula grid lines, "
            "dark background, teal and gold accents, precise geometric balance, "
            "professional dark fintech aesthetic, crisp clean illustration, "
            "no text, no watermarks, no labels"
        ),
    },
    {
        "filename": "synthetic-equivalence.png",
        "section": "#synthetics-stock",
        "prompt": (
            "Dark fintech diagram illustration showing two distinct converging paths achieving identical outcomes — "
            "on the left a single direct bright teal line representing natural long stock ownership, "
            "on the right two separate glowing gold lines (representing a long call and a short put) that start apart and converge to merge perfectly with the teal line at the end, "
            "the convergence point glows brightly showing perfect payoff equivalence, "
            "dark background with subtle financial grid, "
            "clean geometric data visualization aesthetic, "
            "no text, no watermarks, no labels"
        ),
    },
]


def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    print(f"Initializing Vertex AI — project: {PROJECT_ID}, location: {LOCATION}")
    vertexai.init(project=PROJECT_ID, location=LOCATION)

    model = ImageGenerationModel.from_pretrained(MODEL_ID)
    print(f"Model loaded: {MODEL_ID}\n")

    total = len(IMAGES)
    for i, item in enumerate(IMAGES, 1):
        filename = item["filename"]
        output_path = os.path.join(OUTPUT_DIR, filename)
        print(f"[{i}/{total}] Generating: {filename}  ({item['section']})")

        try:
            images = model.generate_images(
                prompt=item["prompt"],
                number_of_images=1,
                aspect_ratio="16:9",
                safety_filter_level="block_few",
                person_generation="allow_adult",
                add_watermark=False,
            )
            images[0].save(location=output_path, include_generation_parameters=False)
            size_kb = os.path.getsize(output_path) // 1024
            print(f"  Saved: {output_path} ({size_kb} KB)")
        except Exception as e:
            print(f"  ERROR generating {filename}: {e}")

    print(f"\nDone. Images saved to ./{OUTPUT_DIR}/")
    generated = [f for f in os.listdir(OUTPUT_DIR) if f.endswith(".png")]
    print(f"Files present: {len(generated)}/{total}")


if __name__ == "__main__":
    main()
