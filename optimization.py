import numpy as np

# -------------------------
# Fitness function
# -------------------------
def evaluate(a, b, s):
    try:
        # Derived values
        vehicle_length = (a * b) / (b - s)

        # Constraint check
        if not (20 <= vehicle_length <= 30):
            return None

        # Geometry calculations
        cos_theta = (b**2 + (s + a)**2 - a**2) / (2 * b * (s + a))

        # Numerical safety
        if abs(cos_theta) > 1:
            return None

        theta = np.degrees(np.arccos(cos_theta))

        w_s_angle_acute = np.degrees(np.arccos((b - s) / (2 * a)))
        w_s_angle = 180 - w_s_angle_acute

        range_in = w_s_angle_acute - theta

        alpha = np.degrees(np.arccos((b**2 - (s + a)**2 + a**2) / (2 * b * a)))
        range_out = alpha - w_s_angle_acute

        w_out_angle = (alpha + w_s_angle) - 180
        w_in_angle = 180 - (theta + w_s_angle)

        # Avoid tan(0) issues
        if abs(np.tan(np.radians(w_out_angle))) < 1e-6:
            return None
        if abs(np.tan(np.radians(w_in_angle))) < 1e-6:
            return None

        r_out_horizontal = (vehicle_length / np.tan(np.radians(w_out_angle))) - b/2
        r_in_horizontal = (vehicle_length / np.tan(np.radians(w_in_angle))) + b/2

        difference = r_out_horizontal - r_in_horizontal

        # Invalid geometry rejection
        if any(np.isnan([range_in, range_out, r_in_horizontal, r_out_horizontal])):
            return None

        # -------------------------
        # Objective (weighted score)
        # Lower is better
        # -------------------------
        score = (
            abs(difference)*1000 +
            abs(r_in_horizontal) +
            abs(r_out_horizontal) -
            2*range_in -
            2*range_out
        )

        return score, {
            "a": a, "b": b, "s": s,
            "vehicle_length": vehicle_length,
            "range_in": range_in,
            "range_out": range_out,
            "r_in": r_in_horizontal,
            "r_out": r_out_horizontal,
            "difference": difference
        }

    except:
        return None


# -------------------------
# GA-like random search
# -------------------------
best = None
best_score = float("inf")

N = 100000  # increase for better results

for _ in range(N):
    a = np.random.uniform(4, 8)
    b = np.random.uniform(20, 23)
    s = np.random.uniform(8, b - 0.01)

    result = evaluate(a, b, s)

    if result is None:
        continue

    score, data = result

    if score < best_score:
        best_score = score
        best = data


# -------------------------
# Result
# -------------------------
print("\nBest Solution Found:\n")
for k, v in best.items():
    print(f"{k}: {v:.4f}")