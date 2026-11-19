# Simply supported beam with a uniform load
w = float(input("Uniform load w (kip/ft): "))
L = float(input("Span L (ft): "))
E = 29000      # ksi, steel
I = 510        # in^4, W18x35

M_max = w * L**2 / 8                                  # kip-ft
delta = 5 * (w / 12) * (L * 12)**4 / (384 * E * I)    # in

print(f"Maximum moment: {M_max:.1f} kip-ft")
print(f"Maximum deflection: {delta:.2f} in")
deflection_limit = L * 12 / 360
print(f"L/360 limit: {deflection_limit:.2f} in")

if delta > deflection_limit:
    print("WARNING: Deflection exceeds the L/360 limit.")
