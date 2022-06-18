# Notizen (Instant ngp)


## Mesh Export

+ ingp Mesh Export ist nicht stabil und nicht fuer qualitative Meshes geeignet
	+ siehe
		+ https://github.com/NVlabs/instant-ngp/issues/103
		+ https://github.com/NVlabs/instant-ngp/discussions/316
	+ Verweis auf nvdiffrec
		+ spezialisiert auf high quality Mesh construction from 2D viewpoints
		+ https://nvlabs.github.io/nvdiffrec/
		+
+ Export moeglich als .obj und .ply
	+ .ply rel. gleiche  Qualitaet, aber deutlich kleinere Dateigröße (x1.5)
	+ Beispiel kleiner Raum (.ply):
		+ sehr viele Vertecies (800.000)
		+ Dateigroeße ca. 450 MB (zu groß)
+ .obj Problem:
	+ nur ein File exportiert (kein Texture File) 
+ .ply Problem:
	+ farbige Vertecies werden expotiert
	+ werden von Blender nicht dargestellt (MeshLab Viewer schon)
+ .ply => MeshLab => .obj
	+ Ziel: Blenderfarbdarstellung ermoeglichen
	+ Problem: Dateigroeße von 450 MB auf ca. 780 MB
		+ fuehrt zu Absturz von Blender (beim Laden der Datei)
		+ sowohl bei Jonathan als auch Alex

	
Mesh-Optimierung mittels MeshLab-Viewer
+ mehrere Verfahren getestet
	+ Laplacian Smooth Varianten


