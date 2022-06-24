import bpy

# Pre-simulation operations
# E.g. set the domain resolution higher
# bpy.data.objects["Smoke Domain"].modifiers["Fluid"].domain_settings.resolution_max = 512


# Bake simulation
bpy.ops.fluid.bake_all()

# Save file
bpy.ops.wm.save_mainfile()
