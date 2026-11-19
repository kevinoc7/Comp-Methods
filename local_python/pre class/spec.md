# Concrete Slab Calculator

## 1. Overview

This app helps users estimate the amount of concrete needed for a rectangular slab and the total cost of the concrete. The user enters the slab dimensions, thickness, waste factor, and concrete price. The app calculates the required concrete volume in cubic yards and the total project cost.

---

## 2. Inputs

### Slab Length
- Units: feet (ft)
- Control: Slider
- Range: 1–200 ft
- Default: 20 ft

### Slab Width
- Units: feet (ft)
- Control: Slider
- Range: 1–200 ft
- Default: 15 ft

### Thickness
- Units: inches (in)
- Control: Slider
- Range: 2–12 in
- Default: 4 in

### Waste Factor
- Units: percent (%)
- Control: Slider
- Range: 0–20%
- Default: 10%

### Concrete Price
- Units: dollars per cubic yard ($/yd³)
- Control: Number Box
- Range: 50–500
- Default: 150

---

## 3. Outputs

### Concrete Volume
- Displayed as a large number.
- Units: cubic yards (yd³).
- Rounded up to the nearest quarter yard (0.25 yd³).

### Total Cost
- Displayed as a large number below the volume.
- Shown in U.S. dollars with two decimal places.

### Slab Diagram
- A top-down rectangle representing the slab.
- Length and width labels displayed on the appropriate sides.
- Diagram redraws automatically whenever inputs change.

---

## 4. Calculations

### Step 1: Calculate Thickness in Feet

thickness_ft = thickness_in / 12

### Step 2: Calculate Volume in Cubic Feet

volume_ft3 = length × width × thickness_ft

### Step 3: Convert to Cubic Yards

volume_yd3 = volume_ft3 / 27

### Step 4: Add Waste Factor

adjusted_volume = volume_yd3 × (1 + waste_factor / 100)

### Step 5: Round Up to Nearest Quarter Yard

ordered_volume = ceil(adjusted_volume × 4) / 4

### Step 6: Calculate Cost

total_cost = ordered_volume × price_per_yard

---

## 5. Validation

- Length must be between 1 and 200 ft.
- Width must be between 1 and 200 ft.
- Thickness must be between 2 and 12 in.
- Waste factor must be between 0 and 20%.
- Price must be greater than 0.
- Invalid values will display an error message and prevent calculations.

---

## 6. Look and Feel

- Title displayed at the top of the page.
- Input controls placed in a panel on the left side.
- Results displayed on the upper right side.
- Slab diagram displayed below the results.
- Changes to inputs immediately update calculations and redraw the diagram.
- Use a clean layout with large labels and readable numbers.

---

## 7. Validation Example

### Inputs

- Length = 20 ft
- Width = 15 ft
- Thickness = 4 in
- Waste Factor = 10%
- Price = $150 per yd³

### Calculations

Thickness in feet:

4 ÷ 12 = 0.333 ft

Volume in cubic feet:

20 × 15 × 0.333 = 100 ft³

Volume in cubic yards:

100 ÷ 27 = 3.70 yd³

Add 10% waste:

3.70 × 1.10 = 4.07 yd³

Round up to nearest quarter yard:

4.07 → 4.25 yd³

Total Cost:

4.25 × $150 = $637.50

### Outputs

- Concrete Needed: 4.25 yd³
- Total Cost: $637.50
- Diagram shows a rectangle labeled 20 ft × 15 ft.