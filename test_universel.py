c = 299792458
maille_or = 1.6266666667
cycle_gvj = 162.6

print("--- TEST DE RÉSONANCE LUMIÈRE ---")
rapport = c / maille_or
residu = rapport % cycle_gvj

print(f"Rapport Lumière/Maille : {rapport:.2f}")
print(f"Résidu sur cycle 162.6   : {residu:.6f}")

# Test de l'harmonique
harmonique = rapport / cycle_gvj
print(f"Nombre de cycles purs  : {harmonique:.4f}")
