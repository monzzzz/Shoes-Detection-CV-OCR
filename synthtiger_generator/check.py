from PIL import features

if features.check("raqm"):
    print("libraqm is installed and supported!")
else:
    print("libraqm is not installed.")
    
print(f"Freetype2 support: {features.check('freetype2')}")
print(f"Harfbuzz support: {features.check('harfbuzz')}")
print(f"Raqm support: {features.check('raqm')}")