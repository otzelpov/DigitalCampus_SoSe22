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

<hr>

# Erfahrungen mit nvdiffrec (22.06.22)

+ Docker Anleitung nicht ganz so gut beschrieben
	+ bei Jonathan Beispiel Dataset zum laufen bekommen
+ [Keine offizielle/detaillierte Anleitung fuer eigene/custom Datasets](https://github.com/NVlabs/nvdiffrec/issues/33#issuecomment-1133854853)
+ [Fuer custom Datasets wird auf Anleitung von Nerf verwiesen](https://github.com/bmild/nerf#generating-poses-for-your-own-scenes)
	+ [bzw siehe hier](https://github.com/NVlabs/nvdiffrec/issues/31#issuecomment-1131528519)
	+ hier hatten wir Schwierigkeiten beim erstellen von Masks, welche nvdiffrec benoetigt
	+ Python Modul zum erstellen von Mask warf exception 
	+ jedoch gibt es alternativen fuer dieses Modul (noch nicht getestet)
	+ Anmerkung: wir hatten es mit einem [Script](https://github.com/NVlabs/nvdiffrec/issues/3#issuecomment-1141588347) aus der "Community" versucht



