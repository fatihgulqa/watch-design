# Production Plan: NH35 Diver Watch Case

**Project:** Production-Ready Diver Watch Case for Seiko NH35 Movement
**Document Version:** 1.0
**Date:** 2026
**Design Standard Basis:** HorologyCAD Movement-Led Watch Case Design System
**CAD File:** DiverWatchCase_NH35.FCStd

---

## 1. Executive Summary

This production plan defines the complete engineering pathway to transform the current preliminary NH35 diver watch case CAD model into a production-ready design. The plan is organized in phases, each with defined deliverables, engineering calculations, verification checks, and quality gates.

**Critical design correction identified during research:**
- The current model uses **MovementDia = 29.4mm** but the official NH35 movement diameter is **27.40mm** (bare movement) / **29.36mm** (with dial holding spacer)
- This must be corrected in Phase 1

**Official NH35 Specifications (verified from TMI/Seiko NH3 Series technical guide):**
| Parameter | Value | Source |
|-----------|-------|--------|
| Movement outside diameter | 27.40 mm | NH3 Series technical guide |
| Casing diameter (with dial holding spacer) | 29.36 mm | NH3 Series technical guide |
| Total movement height | 5.32 mm | NH3 Series technical guide |
| Ligne size | 12"' | NH3 Series technical guide |
| Frequency | 21,600 vph / 3 Hz | NH3 Series technical guide |
| Jewels | 24 | NH3 Series technical guide |
| Accuracy | -20 ~ +40 s/day | NH3 Series technical guide |
| Power reserve | >41 hours | NH3 Series technical guide |
| Dial diameter | 28.4-28.5 mm | NH3 Series technical guide |
| Hour hand tube | ~1.50 mm | NH3 Series technical guide |
| Minute hand tube | ~0.90 mm | NH3 Series technical guide |
| Second hand tube | ~0.20 mm | NH3 Series technical guide |
| Stem part # | 351-200 (tap 10) | NH3 Series technical guide |
| Stem height | 2.0 mm (from movement top to stem axis) | NH3 Series technical guide |

---

## 2. Design Philosophy

### Movement-Led Design
Per HorologyCAD engineering system, the watch case must be designed from the movement outward:
1. Movement defines: dimensions, stem height, hand stack, rotor envelope, movement location, clearances, alignment, assembly behavior, sealing constraints, manufacturing limits
2. Case architecture is resolved around these constraints
3. External case form accommodates the internally defined centerline

### Constraint Domains (NH35)
1. **Radial constraint** - movement/spacer diameter vs case cavity
2. **Axial constraint** - movement height vs case depth
3. **Stem height constraint** - crown alignment with stem axis
4. **Rotor clearance constraint** - vertical clearance behind movement
5. **Holder/spacer integration** - dial holding spacer relationship

---

## 3. Phase Plan

### Phase 0: Research & Specification Lock
**Status: COMPLETE** (this document)

**Deliverables:**
- [x] Official NH35 movement specifications verified
- [x] Watch case design engineering system reviewed
- [x] Crown/stem alignment requirements established
- [x] Water resistance engineering principles reviewed
- [x] Tolerance strategy defined
- [x] CNC machining constraints reviewed
- [x] Crystal sealing systems reviewed

### Phase 1: Correct Movement Dimensions & Rebuild Core Geometry
**Status: COMPLETE** ✅

**Completed tasks:**
- [x] Corrected MovementDia from 29.4mm → 27.40mm (official NH35 spec)
- [x] Added CasingDia = 29.36mm (with dial holding spacer)
- [x] Rebuilt movement cavity to 29.96mm diameter (CasingDia + 2×0.3mm clearance)
- [x] Corrected crown bore position (from case OD at X=19.5, drilling inward)
- [x] Verified all dimensions against official NH35 spec
- [x] Body shape valid, single solid (volume 7159.0mm³)

**Verified geometry:**
- Movement cavity: R=14.98mm (29.96mm dia) ✓
- Crown bore: R=1.25mm (2.5mm dia) at X=19.5, Z=5.32 (stem height) ✓
- Case OD: R=19.5mm (39.0mm dia) ✓
- Rehaut: R=14.5mm (29.0mm dia) ✓
- Crystal seat: R=14.75mm (29.5mm dia) ✓
- Spring bars: R=0.75mm at Y=±21, Z=8 ✓
- Lug-to-lug: 44.0mm ✓

**Key learnings:**
- Crown bore pocket uses Reversed=False to cut inward from case OD
- Pocket direction verified with test cylinder (Reversed=False = inward)
- Fillets must be applied AFTER crown bore (topology change issue)
### Phase 2: Dial-Side Stack & Crystal Interface
**Status: COMPLETE** ✅

**Completed tasks:**
- [x] Dial seat geometry verified (dial on dial holding spacer)
- [x] Rehaut geometry verified (R=14.5, Ø29.0mm, from Z=12 to movement top)
- [x] Crystal seat with gasket groove (R=15.25, Ø30.5mm, with 0.5mm deep groove)
- [x] Crystal opening defined (Ø28.0mm)
- [x] Hand-to-crystal clearance calculated (0.68mm ✓ ≥0.3mm)
- [x] Date window aperture considered (NH35 date at 3:00)

**Key engineering decisions:**
- MovementClearH set to 0.0 (movement sits on case back) → hand-to-crystal clearance 0.68mm
- CrystalSeatDia updated to 30.5mm (was 29.5mm) for proper gasket groove wall
- Gasket groove: R=15.25..15.75 (0.5mm deep into wall), Z=11.0..11.5 (0.5mm wide)
- Gasket groove created via single-circle pocket (annular sketch unsupported in this FreeCAD version)

**Verified stack:**
- Movement top: Z=6.82 (on case back)
- Dial: Z=6.82..7.22 (0.4mm thick)
- Hands: Z=7.22..9.82 (2.6mm stack)
- Crystal seat bottom: Z=10.5
- Hand-to-crystal clearance: 0.68mm ✓
### Phase 3: Crown System Engineering
**Status: COMPLETE** ✅

**CAD file:** `freecad_designs/DiverWatchCase_NH35_Ph34.FCStd`

**Completed tasks:**
- [x] Crown tube bore defined (Ø2.5mm for standard NH35 crown tube)
- [x] Crown tube boss geometry defined (Ø4.5mm boss, 1.5mm protrusion)
- [x] Crown bore aligned with stem axis (Z=4.82, 0° angular error)
- [x] Crown boss wall thickness verified (1.0mm ≥ 0.8mm minimum)
- [x] Crown boss fused with case body (single solid)
- [x] Crown gasket interface defined (annular face gland on case OD at boss base)
- [x] Stem engagement length calculated and cut through the web into the cavity

**Critical fix applied:**
- **Two-solid issue resolved**: The crown boss was disconnected from the case body (datum at X=19.5, padded outward to X=21.0, only touching at a line)
- **Fix**: Moved boss datum inward to X=18.5 (CaseOD/2 - 1.0) and extended pad length to 2.5mm
- Boss now spans X=18.5 (inside case wall) to X=21.0 (tip), overlapping the case wall by 1.0mm
- Result: Single solid, valid body

**Verified crown system:**
- Crown bore: R=1.25 (Ø2.5mm) at X=16.09..21.0 (through boss), Z=4.82 (stem height) ✓
- Crown boss: R=2.25 (Ø4.5mm), wall thickness 1.0mm ✓
- Crown boss protrusion: 1.5mm beyond case OD ✓
- Stem axis alignment: Z=4.82 = CaseBack + MovementH + MovementClearH - StemH ✓

**Phase 3.1 — Crown gasket gland (`Pocket_CrownGasket`):**
- Annular face gland on the case OD at the boss base (datum plane `Datum_CrownBore`, X=19.5)
- Inner diameter = 4.5mm (flush with boss OD), outer diameter = 6.0mm, axial depth = 0.18mm
- Cut inward (-X) into the case; sketch `Sketch_CrownGasket` (two concentric circles)
- **Assumption (needs review):** gland placed on the case OD face at boss base (X=19.5). If a boss-end-face gland (X≈21.0) or a different axial station is intended, revise `build_phase3_crown.py`.

**Phase 3.2 — Stem engagement web cut (`Pocket_CrownStem`):**
- Coaxial bore (R=1.25mm) from the OD face through the wall into the movement cavity
- Stem engagement = 1.0mm into the cavity; bore front reaches X = cavity wall - 1.0mm
- Sketch `Sketch_CrownStem`; pocket length computed from `Datum_CrownBore` X to cavity wall minus engagement

**Verification (live FreeCAD GUI, `DiverWatchCase_NH35_Ph34`):**
- `CaseBody` tip = `Pocket_CrownStem`; body volume = **6538.197 mm³**
- `Pocket_CrownGasket`: valid, not null, not suppressed
- `Pocket_CrownStem`: valid, not null, not suppressed
- Single contiguous solid; shape valid
- Renders: `verification_ph34/ph34_iso_render.png`, `ph34_top_render.png`, `ph34_front_render.png`, `ph34_right_render.png`

**Remaining tasks:**
- [ ] Crown guards (optional, not yet modeled)
- [ ] Confirm gland placement assumption (see Phase 3.1)

### Phase 4: Caseback & Rotor Clearance
**Status: PENDING**

**Tasks:**
1. Define caseback geometry (screw-down type per NH35 spec)
2. Define caseback gasket groove
3. Calculate rotor clearance
4. Define caseback thread (M38×0.8 or similar)
5. Add caseback tool slots (6-slot or similar)

**Engineering calculations:**
- Rotor envelope: rotor diameter ~25mm, rotor height ~1.5mm above movement
- Rotor clearance: ≥0.5mm (minimum above rotor)
- Caseback gasket groove: Ø36.5mm, 0.5mm deep
- Caseback thread: M38×0.8 (standard for 39mm case)
- Caseback depth: 2.0mm (typical)

**Quality gate:**
- [ ] Rotor clearance ≥0.5mm
- [ ] Caseback gasket groove geometry correct
- [ ] Thread geometry verified

### Phase 5: Lugs, Spring Bars & Strap Interface
**Status: PENDING**

**Tasks:**
1. Refine lug geometry for 20mm strap width
2. Define spring bar holes (Ø1.5mm, standard)
3. Calculate lug-to-lug distance
4. Define lug profile for strap fit
5. Add lug chamfers for strap comfort

**Engineering calculations:**
- Lug width: 20mm (strap width)
- Individual lug width: 4.5mm (typical for 20mm strap)
- Spring bar hole: Ø1.5mm (standard spring bar)
- Spring bar hole position: 8mm from top (typical)
- Lug-to-lug: 44mm (for 39mm case, typical)
- Lug tip chamfer: 0.5mm (comfort)

**Quality gate:**
- [ ] Spring bar holes aligned with lug center
- [ ] Lug-to-lug = 44mm
- [ ] Strap fits between lugs (20mm)

### Phase 6: Sealing System Engineering
**Status: PENDING**

**Tasks:**
1. Define crystal gasket (radial compression, Ø29.5mm)
2. Define caseback gasket (axial compression)
3. Define crown gasket
4. Calculate gasket compression for 200m water resistance
5. Define surface finish requirements for sealing surfaces

**Engineering calculations (200m water resistance):**
- Pressure at 200m: P = ρgh = 1000 × 9.81 × 200 = 1,962,000 Pa ≈ 19.62 bar
- Design pressure: 20 bar (with safety factor)
- Gasket compression: 15-25% of gasket cross-section (typical)
- Crystal gasket: Ø1.0mm cross-section, 0.15-0.25mm compression
- Caseback gasket: Ø1.5mm cross-section, 0.2-0.35mm compression
- Crown gasket: Ø1.0mm cross-section, 0.15-0.25mm compression

**Quality gate:**
- [ ] Gasket compression calculated for all interfaces
- [ ] Sealing surfaces specified (Ra ≤0.4μm)
- [ ] 200m water resistance design target met

### Phase 7: Tolerance Assignment & GD&T
**Status: PENDING**

**Tasks:**
1. Assign tolerances per ISO 286 or ASME Y14.5
2. Define critical dimensions with tight tolerances
3. Define positional tolerances for crown tube
4. Calculate tolerance stack-up
5. Define surface finish requirements

**Tolerance strategy (based on CNC capability):**
- Standard features: ±0.05mm (ISO 2768-mK)
- Critical features: ±0.01-0.02mm (CNC precision)
- Movement cavity: +0.02/-0.00mm (fit)
- Crown tube bore: ±0.01mm (alignment)
- Crystal seat: +0.02/-0.00mm (gasket fit)
- Spring bar holes: ±0.02mm (position)
- Caseback thread: 6H/6g (ISO metric)

**Quality gate:**
- [ ] All critical tolerances assigned
- [ ] Tolerance stack-up calculated
- [ ] GD&T scheme defined

### Phase 8: Fillets & Dress-Up (Final)
**Status: PENDING**

**Tasks:**
1. Apply outer edge fillets (R0.5mm)
2. Apply lug tip fillets (R0.2mm)
3. Apply internal fillets where manufacturable
4. Verify no self-intersections
5. Final shape validation

**Quality gate:**
- [ ] All fillets valid
- [ ] Body shape valid
- [ ] No self-intersections

### Phase 9: Manufacturing Documentation
**Status: PENDING**

**Tasks:**
1. Create manufacturing drawing (ISO 7200 title block)
2. Define material (316L stainless steel)
3. Define heat treatment (if applicable)
4. Define surface finish (brushed/polished)
5. Create inspection plan
6. Export STEP file
7. Define machining sequence

**Quality gate:**
- [ ] Drawing complete with all dimensions
- [ ] Material specified
- [ ] Inspection plan defined
- [ ] STEP file verified

### Phase 10: Prototype Validation
**Status: PENDING**

**Tasks:**
1. CNC prototype machining
2. Movement fit validation
3. Water resistance testing (20 bar)
4. Crown operation validation
5. Strap fit validation
6. Design iteration if needed

**Quality gate:**
- [ ] Movement fits correctly
- [ ] Water resistance verified
- [ ] Crown operation smooth
- [ ] Strap fits correctly

---

## 4. Engineering Calculations Reference

### Movement Cavity Sizing


