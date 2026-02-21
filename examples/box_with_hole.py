import cadquery as cq

result = (
    cq.Workplane("XY")
    .box(40, 20, 10)
    .faces(">Z")
    .workplane()
    .hole(5)
)

cq.exporters.export(result, "box_with_hole.stl")
