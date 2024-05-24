from PIL import features

if features.check("raqm"):
    print("libraqm is installed and supported!")
else:
    print("libraqm is not installed.")