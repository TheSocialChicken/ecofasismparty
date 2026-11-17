"""Turn flat stamp SVGs into interchangeable stamp discs for MakerWorld model 936935
("Stamp with interchangeable designs", A.E.W.P.M.).

Blank disc: ../makerworld_base/icon_Original.stl (37 mm, design face at y=-2.5,
flat face radius 17.5 mm; the notch on the back marks the TOP = +z).
The design is mirrored (so it stamps the right way round) and raised 1.0 mm.

Usage: <venv with trimesh manifold3d svgelements>/python make_discs.py [diameter_mm]
Input:  flat/*.svg  (single-path SVGs, viewBox 0 0 200 200 or 0 0 160 160)
Output: stl/<name>.stl  (print design side UP, ironing on, light sanding after)
"""
import os, sys
import numpy as np
import trimesh
import manifold3d as mf
from svgelements import SVG, Path, Shape

HERE = os.path.dirname(os.path.abspath(__file__))
BASE = os.path.join(HERE, "..", "makerworld_base", "icon_Original.stl")
DIAM = float(sys.argv[1]) if len(sys.argv) > 1 else 33.5   # design outer diameter, mm
CREDIT_DIAM = 17.0  # credit stamps: ~16 mm square, fits the 19 mm passport boxes
RELIEF = 1.0       # same as the designer's own discs (y -2.5 -> -3.5)
OVERLAP = 0.3      # sink into the disc so the union is solid
FACE_Y = -2.5


def contours(svg_file):
    svg = SVG.parse(svg_file)
    vb = svg.viewbox
    cx, cy = vb.x + vb.width / 2, vb.y + vb.height / 2
    size = max(vb.width, vb.height)
    loops = []
    for el in svg.elements():
        if isinstance(el, Shape) and not isinstance(el, SVG):
            p = Path(el)
            p.reify()
            for sub in p.as_subpaths():
                sp = Path(sub)
                n = max(16, int(sp.length(error=1e-2) / 0.5))
                pts = [sp.point(t) for t in np.linspace(0, 1, n, endpoint=False)]
                pts = [(pt.x, pt.y) for pt in pts if pt is not None]
                if len(pts) >= 3:
                    loops.append(pts)
    return loops, (cx, cy), size


def build(svg_file, out_file, base):
    loops, (cx, cy), size = contours(svg_file)
    s = (CREDIT_DIAM if os.path.basename(svg_file).startswith("credit") else DIAM) / size
    # reading orientation (svg u right, v down) -> mirrored for the stamp face
    polys = [[(-(u - cx) * s, -(v - cy) * s) for (u, v) in loop] for loop in loops]
    cs = mf.CrossSection(polys, mf.FillRule.EvenOdd)
    relief = mf.Manifold.extrude(cs, RELIEF + OVERLAP)
    mesh = relief.to_mesh()
    v = np.array(mesh.vert_properties)[:, :3]
    # (X, Y, Zext) -> x=X, y=FACE_Y+OVERLAP-Zext, z=Y
    v3 = np.column_stack([v[:, 0], FACE_Y + OVERLAP - v[:, 2], v[:, 1]])
    tri = np.array(mesh.tri_verts)
    rel = trimesh.Trimesh(v3, tri, process=True)   # (X,Y,Z)->(X,-Z,Y) is a proper rotation: keep winding
    m_rel = mf.Manifold(mf.Mesh(vert_properties=np.asarray(rel.vertices, np.float32),
                                tri_verts=np.asarray(rel.faces, np.uint32)))
    u = base + m_rel
    build.status = (u.status(), u.genus(), round(u.volume(), 1))
    out = u.to_mesh()
    res = trimesh.Trimesh(np.array(out.vert_properties)[:, :3], np.array(out.tri_verts))
    res.export(out_file)
    return res


if __name__ == "__main__":
    b = trimesh.load(BASE)
    base = mf.Manifold(mf.Mesh(vert_properties=np.asarray(b.vertices, np.float32),
                               tri_verts=np.asarray(b.faces, np.uint32)))
    os.makedirs(os.path.join(HERE, "stl"), exist_ok=True)
    for f in sorted(os.listdir(os.path.join(HERE, "flat"))):
        if f.endswith(".svg"):
            r = build(os.path.join(HERE, "flat", f), os.path.join(HERE, "stl", f[:-4] + ".stl"), base)
            print(f, build.status, r.bounds.round(2).tolist())
