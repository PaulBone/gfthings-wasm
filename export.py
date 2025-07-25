# Export script - handles STL generation and data preparation for 3D viewer
# This script expects an 'output' variable to be defined with the following structure:
# output = [
#     {"name": "part_name", "part": part_geometry, "color": "#hex_color", "opacity": 0.8},  # opacity is optional
#     ...
# ]

print("Starting export process...")

# Validate output variable exists
if 'output' not in globals():
    raise ValueError("No 'output' variable found. Please define output as a list of parts with name, part, and color.")

if not isinstance(output, list):
    raise ValueError("Output must be a list of part dictionaries.")

if len(output) == 0:
    raise ValueError("Output list is empty. Please add at least one part.")

# Export each part individually and collect STL, STEP, and BREP data
parts_data = []
for i, part_info in enumerate(output):
    # Validate part structure
    if not isinstance(part_info, dict):
        raise ValueError(f"Part {i} must be a dictionary with 'name', 'part', and 'color' keys.")
    
    required_keys = ['name', 'part', 'color']
    missing_keys = [key for key in required_keys if key not in part_info]
    if missing_keys:
        raise ValueError(f"Part {i} is missing required keys: {missing_keys}")
    
    # Generate filenames and export STL, STEP, and BREP
    stl_filename = f"output_part_{i}_{part_info['name']}.stl"
    step_filename = f"output_part_{i}_{part_info['name']}.step"
    brep_filename = f"output_part_{i}_{part_info['name']}.brep"
    
    export_stl(part_info['part'], stl_filename)
    export_step(part_info['part'], step_filename)
    export_brep(part_info['part'], brep_filename)
    
    # Read STL data
    with open(stl_filename, 'rb') as fh:
        stl_data = fh.read()
    
    # Read STEP data
    with open(step_filename, 'rb') as fh:
        step_data = fh.read()
    
    # Read BREP data
    with open(brep_filename, 'rb') as fh:
        brep_data = fh.read()
    
    # Prepare part data for JavaScript (include opacity if specified)
    part_data = {
        'name': part_info['name'],
        'color': part_info['color'],
        'stl': to_js(stl_data, create_pyproxies=False),
        'step': to_js(step_data, create_pyproxies=False),
        'brep': to_js(brep_data, create_pyproxies=False),
    }
    # Add opacity if specified
    if 'opacity' in part_info:
        part_data['opacity'] = part_info['opacity']
    
    parts_data.append(part_data)
    
# Store parts data for 3D viewer (list of parts with names, colors, and STL data)
window.partsData = to_js(parts_data, create_pyproxies=False)