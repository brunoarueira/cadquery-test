import cadquery as cq

result = (
    cq.Workplane("XY")
    .box(40, 20, 10)
)

cq.exporters.export(result, "box.stl")
