# PARAMETERS_START
# {
#   "width": {"type": "number", "default": 1, "min": 1, "max": 8, "step": 0.5, "label": "Width (units)", "description": "Width of the bin in GF units"},
#   "depth": {"type": "number", "default": 1, "min": 1, "max": 8, "step": 0.5, "label": "Depth (units)", "description": "Depth of the bin in GF units"},
#   "height": {"type": "number", "default": 4, "min": 3, "max": 20, "step": 1, "label": "height (units)", "description": "Height of the bin in GF units."}
# }
# PARAMETERS_END

# Print the custom model name to demonstrate string parameter support
print(f"🏷️  Generating bin")
print(f"📏 Dimensions: {width} x {depth} x {height}")

from gfthings.Bin import Bin

b = Bin(width, depth, height, scoop_rad=10)

# Build output list based on parameters
output = [{"name": "bin", "part": b, "color": "#40c0c0"}]

