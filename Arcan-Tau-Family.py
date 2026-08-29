import math

# Constants
pi = math.pi
tau = 2 * pi

# Core Angles
theta_rad = math.atan(tau)                    # Arcan(τ)-Angle
theta_deg = math.degrees(theta_rad)

alpha_rad = theta_rad / 2                     # Half-Arcan(τ)-Angle
alpha_deg = math.degrees(alpha_rad)

phi_rad = math.atan(pi)                       # Classical Half-Turn Angle
phi_deg = math.degrees(phi_rad)

psi_rad = theta_rad - phi_rad                 # Angular Separation
psi_deg = math.degrees(psi_rad)

# Trigonometric values for alpha
tan_alpha = math.tan(alpha_rad)
sin_alpha = math.sin(alpha_rad)
cos_alpha = math.cos(alpha_rad)
hyp_alpha = 1 / cos_alpha   # hypotenuse when adjacent = 1

print("JOSHUA CHRISTOPHER RYAN'S ARCAN(τ) FAMILY")
print("=" * 70)
print(f"τ (Circle Constant)          = {tau:.12f}  (= 2π = C/r)")
print()
print(f"θ  = arctan(τ)              = {theta_rad:.12f} rad ≈ {theta_deg:.6f}°")
print(f"   tan(θ)                   = {tau:.12f}  (Full Turn)")
print()
print(f"α  = θ/2 = (1/2)arctan(τ)   = {alpha_rad:.12f} rad ≈ {alpha_deg:.6f}°")
print(f"   tan(α)                   = {tan_alpha:.12f}")
print(f"   sin(α)                   = {sin_alpha:.12f}")
print(f"   cos(α)                   = {cos_alpha:.12f}")
print(f"   Hypotenuse (adj=1)       = {hyp_alpha:.12f}")
print()
print(f"ϕ  = arctan(π)               = {phi_rad:.12f} rad ≈ {phi_deg:.6f}°")
print(f"   tan(ϕ)                   = {pi:.12f}  (Half Turn)")
print()
print(f"ψ  = θ - ϕ                   = {psi_rad:.12f} rad ≈ {psi_deg:.6f}°")
print(f"   (Angular Separation between τ and π projections)")
print("=" * 70)
print("All values computed with full floating-point precision.")
