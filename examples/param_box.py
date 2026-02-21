import cadquery as cq

length = 60
width = 30
height = 8
hole_diameter = 6

result = (
    cq.Workplane("XY")
    .box(length, width, height)
    .faces(">Z")
    .workplane()
    .hole(hole_diameter)
)

cq.exporters.export(result, "param_box.stl")
