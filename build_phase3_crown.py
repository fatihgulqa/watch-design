import FreeCAD, Part, shutil, math, traceback

DST = r'E:\Projects\watch-design\freecad_designs\DiverWatchCase_NH35_Ph34.FCStd'
BAK = r'E:\Projects\watch-design\freecad_designs\DiverWatchCase_NH35_Ph34.bak.FCStd'
shutil.copyfile(DST, BAK)

doc = FreeCAD.openDocument(DST)
body = doc.getObject('CaseBody')
s = doc.getObject('Params')

of = open(r'E:\Projects\watch-design\ph3_out.txt', 'w')
def p(*a):
    of.write(' '.join(str(x) for x in a) + '\n')
    print(' '.join(str(x) for x in a))

def param(name, default):
    try:
        v = s.get(name)
        if v is None or v == '':
            return default
        return float(v)
    except Exception:
        return default

# ---- Phase 3 crown parameters (already seeded in Params; read them) ----
seat_dia = param('CrownGasketSeat', 4.5)          # inner gland diameter
od_dia   = param('CrownGasketGrooveOD', 6.0)      # outer gland diameter
depth    = param('CrownGasketCompression', 0.18)  # gland axial depth
engage   = param('StemEngagement', 1.0)           # stem engagement into cavity
p('params seat=%.3f od=%.3f depth=%.3f engage=%.3f' % (seat_dia, od_dia, depth, engage))

r_in  = seat_dia / 2.0
r_out = od_dia   / 2.0

# ---- Reference geometry ----
crown_plane = doc.getObject('Datum_CrownBore')
plane_x = crown_plane.Placement.Base.x          # X=19.5 (case OD at crown)
cavity_sk = doc.getObject('Sketch_MovementCavity')
cav_r = None
for g in cavity_sk.Geometry:
    if hasattr(g, 'Radius'):
        cav_r = g.Radius
        break
p('plane_x=%.3f  cavity_r=%s' % (plane_x, cav_r))

# ============================================================
# FEATURE 1 : Crown face gasket gland (annular groove on OD face)
#   inner radius = r_in (flush with boss OD), outer radius = r_out,
#   axial depth = depth, cut inward (-X) into the case.
# ============================================================
def annular_face_wire(doc, body, sxr, syz, r_out, r_in, name):
    """Create a sketch containing outer + inner concentric circles -> annular face."""
    sk = body.newObject('Sketcher::SketchObject', name + '_Sketch')
    sk.AttachmentSupport = [crown_plane]; sk.MapMode = 'FlatFace'
    doc.recompute()
    sk.addGeometry(Part.Circle(FreeCAD.Vector(sxr, syz, 0.0), FreeCAD.Vector(0, 0, 1), r_out), False)
    sk.addGeometry(Part.Circle(FreeCAD.Vector(sxr, syz, 0.0), FreeCAD.Vector(0, 0, 1), r_in),  False)
    doc.recompute()
    return sk

sk = body.newObject('Sketcher::SketchObject', 'Sketch_CrownGasket')
sk.AttachmentSupport = [crown_plane]; sk.MapMode = 'FlatFace'
doc.recompute()
# local coords on Datum_CrownBore: local X -> global Y, local Y -> global Z
sk.addGeometry(Part.Circle(FreeCAD.Vector(0, 4.82, 0), FreeCAD.Vector(0, 0, 1), r_out), False)
sk.addGeometry(Part.Circle(FreeCAD.Vector(0, 4.82, 0), FreeCAD.Vector(0, 0, 1), r_in),  False)
doc.recompute()
p('gland sketch geoms', len(sk.Geometry))

pk_g = body.newObject('PartDesign::Pocket', 'Pocket_CrownGasket')
pk_g.Profile = sk
pk_g.Length = depth
pk_g.Type = 'Length'
pk_g.Direction = FreeCAD.Vector(-1, 0, 0)
pk_g.Reversed = False
pk_g.Midplane = False
try:
    pk_g.SideType = 'One side'
except Exception:
    pass
doc.recompute()
p('gland state', pk_g.State, 'valid', body.Shape.isValid())
p('vol after gland', round(body.Shape.Volume, 3))

# ============================================================
# FEATURE 2 : Stem engagement web cut (coaxial bore from OD face
#   through the wall into the movement cavity)
# ============================================================
sk2 = body.newObject('Sketcher::SketchObject', 'Sketch_CrownStem')
sk2.AttachmentSupport = [crown_plane]; sk2.MapMode = 'FlatFace'
doc.recompute()
sk2.addGeometry(Part.Circle(FreeCAD.Vector(0, 4.82, 0), FreeCAD.Vector(0, 0, 1), 1.25), False)
doc.recompute()

# length so bore front reaches (cavity wall - engage) => fully opens web + engages
cav_face = cav_r if cav_r else 14.98
stem_len = plane_x - (cav_face - engage)
p('stem_len=%.3f  (front reaches X=%.3f)' % (stem_len, cav_face - engage))

pk_s = body.newObject('PartDesign::Pocket', 'Pocket_CrownStem')
pk_s.Profile = sk2
pk_s.Length = stem_len
pk_s.Type = 'Length'
pk_s.Direction = FreeCAD.Vector(-1, 0, 0)
pk_s.Reversed = False
pk_s.Midplane = False
try:
    pk_s.SideType = 'One side'
except Exception:
    pass
doc.recompute()
p('stem state', pk_s.State, 'valid', body.Shape.isValid())
p('vol final', round(body.Shape.Volume, 3))
p('bbox', body.Shape.BoundBox)

# ---- Verification: enumerate X-axis cylinder faces near crown ----
p('--- X-axis cylinders near crown (z~4.82) ---')
seen = set()
for f in body.Shape.Faces:
    try:
        if f.Surface.TypeId != 'Part::GeomCylinder':
            continue
        ax = f.Surface.Axis
        if abs(abs(ax.x) - 1) > 1e-6:
            continue
        c = f.Surface.Center
        if abs(c.z - 4.82) > 0.6:
            continue
        xs = [v.Point.x for v in f.Vertexes]
        key = (round(f.Surface.Radius, 3), round(min(xs), 2), round(max(xs), 2))
        if key in seen:
            continue
        seen.add(key)
        p('  cyl r=%.3f axis=%s X %.3f..%.3f' % (f.Surface.Radius,
            tuple(round(x, 2) for x in ax), round(min(xs), 3), round(max(xs), 3)))
    except Exception as e:
        p('  face err', e)

try:
    doc.save()
    p('SAVED')
except Exception:
    traceback.print_exc()
    p('SAVE ERR')
of.close()
print('DONE')
