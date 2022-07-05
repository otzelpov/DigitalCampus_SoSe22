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


## 28.06.2022

+ Problem: train.py => beim mesh write kam ein core dump auf
	+ fix: .json parameter "validate" auf true setzen
	+ scheinbar wurde das Mesh trotzdem geschrieben, auch wenn core dump (nicht weiter getestet) 
+ train.py bob
	+ liefert eine .obj und zugehoerige .mtl (Oberflaechen Beschreibung)
	+ Tipp: Blender "z druecken" => material preview; zeigt oberflache a

## How To: Wie Modelle (Mesh) mit nvdiffrec erstellen?

### Was brauchen wir?

+ Umgebung Aufsetzen
  + [colmap](https://colmap.github.io/install.html) (muss installiert sein)
  + [nvdiffrec](https://github.com/NVlabs/nvdiffrec)
    + wir haben Docker benutzt
  + [colmap2poses](https://github.com/Sazoji/nvdiffrec/blob/main/colmap2poses.py)
    + Skript erlaubt Masken und Poses "gleichzeitig" zu generieren
+ Zum generieren des Meshs:
  + Daten (Bilder vom Modell)
  + Masken der Bilder (muss generiert werden)
    + benötigt um Poses zu generieren
  + Poses (muss generiert werden, poses_bounds.npy)

## Umgebung aufsetzen

[Repo](https://github.com/NVlabs/nvdiffrec) clonen

Docker image nach Anleitung in Repo bauen

```bash
cd docker
./make_image.sh nvdiffrec:v1
```

Interaktive Docker Container starten

```bash
# aus repo
docker run --gpus device=0 -it --rm -v /raid:/raid -it nvdiffrec:v1 bash

# unser angepasster Befehl
# Beachte der momentane Ordner wird in/an den Container gemountet, wodurch man dann innerhalb des Containers die train.py starten kann
sudo docker run --gpus all -it --rm -v $(pwd):/raid -it nvdiffrec:v1 bash
```




## Mesh generieren

+ scale_images.py (Optional, außer man hat begrenzt Speicher)
  + [Link](https://github.com/NVlabs/nvdiffrec/tree/main/data/nerd)
  + Hinweis aus Repo: auf 512x512 skalieren (zumindest für Datensatz)
+ colmap2poses.py
  + [Link/Gist](https://github.com/Sazoji/nvdiffrec/blob/main/colmap2poses.py) 
  + masken und
  + poses generieren
+ Docker Container (train.py ausführen)

**1. scale_images.py**

1. **Anmerkung: Ordnerstruktur beachten!**
2. Skript anpassen (datasets, folders)
3. Skript ausführen

```python
# Zeile 26
# Man kann überlegen ob man anstelle der Variable <datasets> einfach <""> einsetzt.
```

**2. colmap2poses.py**
  
[Für genaue Infos klick](https://github.com/NVlabs/nvdiffrec/issues/3#issuecomment-1141588347)	

```bash
# Be sure to follow the file structure(/data/your_dataset/images/XXXX.png and /data/your_dataset/mask/XXXX.png).
# if you dont have colmap installed, pass --colmap_path

$ colmap2poses.py --mask [mask dir]
```

Falls colmap installiert ist, aber nicht gefunden wird, unsere Lösung:

```bash
$ python3 colmap2poses.py --mask [path2mask] --colmap_path /usr/local/bin/colmap
```

Ergebnis:
+ Ordner mit den Masken
+ poses_bounds.npy

**3. train.py ausführen**

1. Docker container (interaktiv) starten
2. `cd` in den mounted Ordner
3. in der `configs/` eine entsprechende .json anlegen
   + ggf. vorhandene bob.json kopieren
4. `python3 train.py --config configs/beispiel.json`


<hr>

wichtig 
```
Struktur beachten! (oder ggf. skript anpassen)
structure(/data/your_dataset/images/XXXX.png and /data/your_dataset/mask/XXXX.png
bzw mal ausprobieren lol
structure(/data/your_dataset/images/XXXX.png and /data/your_dataset/images/mask/XXXX.png
```

# TODO: beschreiben, was alles noetig war, um nvdiffrec zum laufen zu bekommen

https://github.com/NVlabs/nvdiffrec/issues/3

https://github.com/NVlabs/nvdiffrec/issues/31

https://github.com/bmild/nerf#generating-poses-for-your-own-scenes

https://github.com/fyusion/llff

https://github.com/NVlabs/nvdiffrec/issues/17


# TODO

+ mit anderen Daten
+ `mesh_scale` setzen bzw. anpassen
+ statt rescale resize probieren

aus nvdiffrec
g git and rescale them to 512 x 512 pixels resolution using the script scale_images.py. This is required f