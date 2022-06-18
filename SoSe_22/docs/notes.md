# Notizen (Instant ngp)


## Mesh Export

+ ingp Mesh Export ist nicht stabil und nicht fuer qualitative Meshes geeignet
	+ siehe
		+ https://github.com/NVlabs/instant-ngp/issues/103
		+ https://github.com/NVlabs/instant-ngp/discussions/316
+ Export moeglich als .obj und .ply
	+ (UNSICHER) .ply bessere Qualitaet
	+ Beispiel kleiner Raum (.ply):
		+ sehr viele Vertecies (800.000)
		+ Dateigroeße ca. 450 MB (zu groß)
+ .obj Problem:
	+ nur ein File exportiert (kein Texture File) 
+ .ply Problem:
	+ farbige Vertecies werden expotiert
	+ werden von Blender nicht dargestellt (MeshLab Viewer)


