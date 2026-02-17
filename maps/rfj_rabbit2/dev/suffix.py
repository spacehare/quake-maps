from pathlib import Path

images = Path(__file__ + "/../../textures/rfj_rabbit2/").resolve()

for image in images.iterdir():
    print(image)
    image.rename(image.with_suffix(image.suffix.lower()))
