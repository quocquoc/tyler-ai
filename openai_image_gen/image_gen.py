from openai import OpenAI
import base64
from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY"), 
    organization=os.getenv("OPENAI_ORGANIZATION")
)

# Array of prompts
prompts = [
    """
    Neo-Kyoto Syndicate characters reimagined for a Street Fighter style game cover. Featuring a 'Cyborg Samurai with a plasma katana' and a 'Psionic Street Punk with glowing fists' in dynamic, signature fighting poses. The scene is set on a neon-drenched, rain-slicked futuristic city rooftop, with vibrant energy trails from their attacks and holographic advertisements flickering in the background. The logo "Kyoto Clash", redesigned in the iconic Street Fighter font and style, is prominently displayed and fully integrated within the central composition of the image, ensuring clear visibility and no cropping. Hyper-detailed, vibrant colors, intense contrast, cinematic composition.    """,
    """,
    """
    Guardians of the Verdant Realm characters reimagined for a Street Fighter style game cover. Featuring a 'Mystic Druid wielding nature's fury' and a 'Corrupted Elemental Golem' in dynamic, signature fighting poses. The scene is set in an enchanted forest with oversized glowing mushrooms, with swirling magical energies, bright green spell effects, and explosive earth-shattering impacts. The logo "Verdant Fury", redesigned in the iconic Street Fighter font and style, is prominently displayed and fully integrated within the central composition of the image, ensuring clear visibility and no cropping. Hyper-detailed, vibrant colors, intense contrast, cinematic composition.
    """,
    """
    Celestial Starfighters characters reimagined for a Street Fighter style game cover. Featuring a 'Solar-Powered Hero in golden armor' and a 'Void-Channeling Alien Warlord' in dynamic, signature fighting poses. The scene is set on an alien planet's crystalline surface with two suns in the sky, with brilliant light beams clashing with dark void tendrils, lens flares and cosmic dust. The logo "Star Vindicator", redesigned in the iconic Street Fighter font and style, is prominently displayed and fully integrated within the central composition of the image, ensuring clear visibility and no cropping. Hyper-detailed, vibrant colors, intense contrast, cinematic composition.
    """,
    """
    Pirates of the Crimson Tides characters reimagined for a Street Fighter style game cover. Featuring a 'Swashbuckling Captain with a flintlock pistol and cutlass' and a 'Mysterious Sea Witch commanding spectral water' in dynamic, signature fighting poses. The scene is set on the deck of a storm-tossed galleon, with crashing waves, flashes of gunpowder, and eerie glowing water tendrils. The logo "Crimson Combat", redesigned in the iconic Street Fighter font and style, is prominently displayed and fully integrated within the central composition of the image, ensuring clear visibility and no cropping. Hyper-detailed, vibrant colors, intense contrast, cinematic composition.
    """,
    """
    Dynasty of the Jade Serpent characters reimagined for a Street Fighter style game cover. Featuring a 'Wise Martial Arts Master with flowing robes' and a 'Powerful Sorcerer wielding dark chi' in dynamic, signature fighting poses. The scene is set in a serene temple courtyard with cherry blossoms falling, with focused chi energy blasts meeting shadowy magical attacks, petals swirling in the wind. The logo "Jade Fist", redesigned in the iconic Street Fighter font and style, is prominently displayed and fully integrated within the central composition of the image, ensuring clear visibility and no cropping. Hyper-detailed, vibrant colors, intense contrast, cinematic composition.
    """,
    """
    Wasteland Raiders characters reimagined for a Street Fighter style game cover. Featuring a 'Rugged Scavenger with a modified shotgun' and a 'Mutant Brute with oversized claws' in dynamic, signature fighting poses. The scene is set in a post-apocalyptic desert settlement made of scrap metal, with dusty, orange-hued lighting, muzzle flashes, and powerful ground slams causing debris to fly. The logo "Desert Duel", redesigned in the iconic Street Fighter font and style, is prominently displayed and fully integrated within the central composition of the image, ensuring clear visibility and no cropping. Hyper-detailed, vibrant colors, intense contrast, cinematic composition.
    """,
    """
    Champions of Olympus characters reimagined for a Street Fighter style game cover. Featuring a 'Demigod Hero with a thunderbolt spear' and a 'Gorgon Huntress with a petrifying gaze' in dynamic, signature fighting poses. The scene is set on the steps of a majestic ancient Greek temple, with divine golden light clashing with dark green stone-gaze effects, lightning crackling. The logo "Olympian Might", redesigned in the iconic Street Fighter font and style, is prominently displayed and fully integrated within the central composition of the image, ensuring clear visibility and no cropping. Hyper-detailed, vibrant colors, intense contrast, cinematic composition.
    """,
    """
    Agents of Chronos characters reimagined for a Street Fighter style game cover. Featuring a 'Time-Traveling Operative with temporal gadgets' and a 'Paradox Anomaly creature' in dynamic, signature fighting poses. The scene is set in a swirling vortex of distorted time and space, with shimmering temporal distortion fields, glowing energy from gadgets, and fractured reality effects. The logo "Time Tangle", redesigned in the iconic Street Fighter font and style, is prominently displayed and fully integrated within the central composition of the image, ensuring clear visibility and no cropping. Hyper-detailed, vibrant colors, intense contrast, cinematic composition.
    """,
    """
    Gladiators of the Galactic Arena characters reimagined for a Street Fighter style game cover. Featuring an 'Armored Alien Gladiator with an energy shield' and a 'Nimble Human Mercenary with laser blasters' in dynamic, signature fighting poses. The scene is set in a high-tech alien arena with cheering crowds in the background (blurred), with bright energy shield deflections, laser fire trails, and dramatic spotlights. The logo "Arena Supreme", redesigned in the iconic Street Fighter font and style, is prominently displayed and fully integrated within the central composition of the image, ensuring clear visibility and no cropping. Hyper-detailed, vibrant colors, intense contrast, cinematic composition.
    """
]

# Create output directory if it doesn't exist
os.makedirs("images_output", exist_ok=True)

# Process each prompt
for index, prompt in enumerate(prompts, start=1):
    print(f"Generating image {index}...")
    
    result = client.images.generate(
        model="gpt-image-1",
        prompt=prompt
    )

    image_base64 = result.data[0].b64_json
    image_bytes = base64.b64decode(image_base64)

    # Save the image with incremental name
    image_name = f"image_gen_{index}.png"
    output_path = os.path.join("images_output", image_name)
    
    with open(output_path, "wb") as f:
        f.write(image_bytes)
    
    print(f"Saved image as {image_name}")

print("All images have been generated successfully!")
    
    
    
    
