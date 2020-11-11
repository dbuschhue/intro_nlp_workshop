# 1) Installation von Python:

Im Workshop arbeiten wir mit der freien Software Python (Version 3.6 oder höher). Je nach Betriebssystem erfolgt die Installation anders. Wichtig für die Installation ist, dass Sie dies mit Admin-Rechten
durchführen. Eine Installation ohne Admin-Recht ist zwar unter bestimmten Umständen möglich, aber unserer Erfahrung nach treten dabei häufig Komplikationen auf, die nicht einfach behoben werden 
können. 

Ziel der Installationsanleitung ist es, dass Sie am Ende ein Testskript für Python in einer Entwicklungsumgebung ausführen können. Darin sind alle erforderlichen Pakete angegeben, sodass Sie testen 
können, inwieweit ihr Rechner bereit für den Workshop ist. Allgemein ist die Installation von Python nicht trivial. Sollten Sie Fragen an einer Stelle haben, melden Sie sich gerne für macOS-User bei 
buschhue@uni-potsdam.de und für Windows-User bei peter.wulff@uni-potsdam.de.

Hinweis: Zur Installation wird das Terminal (macOS, Linux) oder die CommandLine (Windows) verwendet. Zum Ausführen des Terminals unter macOS geben Sie in der Suchmaschine Spotlight ''Terminal'' 
ein', bei Windows geben Sie in der Suche ''cmd'' ein.

Für die Installation von Python verweisen wir auf folgende Website: https://docs.python-guide.org/#. Dort finden Sie für die gängigen Betriebssysteme (Linux, macOS, Windows) eine Installationsanleitung. 

Zur Installation von zusätzlichen Modulen in Python wird standardmäßig pip ("pip installs packages") verwendet. 
Um pip zu installieren, laden Sie bitte folgendes Python-Skript: [get-pip.py](https://bootstrap.pypa.io/get-pip.py) herunter. Alternativ können Sie curl im Terminal verwenden:

```
    curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
```

Um das heruntergeladene Skript auszuführen, geben Sie folgenden Befehl im Terminal ein (Achtung: Sie müssen dazu im Verzeichnis des Skriptes sein):

```
    python3 get-pip.py
```

(aus: https://pip.pypa.io/en/stable/installing/)


Stellen Sie im Terminal (macOS und Linux) oder der CommandLine (Windows) sicher, dass Sie Python ausführen können. Geben Sie dort dazu folgenden Befehl ein: 

```
    python3 --version
```

Stellen Sie weiter sicher, dass Sie pip installiert haben mit folgendem Befehl:
```
    python3 -m pip --version
```


# 2) Installation einer Entwicklungsumgebung:

Um komfortabel Python-Skripte testen und ausführen zu können, empfehlen wir insbesondere für Anfängerinnen und Anfänger die Nutzung einer interaktiven Entwicklungsumgebung (IDE). Als 
Entwicklungsumgebung empfehlen wir Spyder, da Spyder kostenfrei ist und nützliche Funktionalitäten (u.a., interaktive Konsole) bietet. Es können alternativ auch IDLE
(die Standard-Entwicklungsumgebung) sowie PyCharm (teilweise kostenpflichtig) verwendet werden.

Die Installation von Spyder erfolgt über pip und den Befehl: 
```
    python3 -m pip install spyder
```

Auch hier sollten Sie sich vergewissern, dass Sie Spyder über Terminal/CommandLine starten können. Geben Sie dazu folgenden Befehl ein:
```
    spyder
```


# 3) Installation notwendiger Python-Module 

Um Auswerteverfahren umzusetzen und möglichst gut mit Python arbeiten zu können, verwenden wir frei verfügbare Module (in etwa Pakete in R) sowie die Entwicklungsumgebung Spyder. Zunächst ist es dazu 
erforderlich ein Modul- oder Paketmanager zu haben. Wir verwenden hierfür pip ("Pip installs Packages").

Folgende Module sollten Sie vorab installieren: scikitlearn, umap, hdbscan, sentence-transformers (mit dem Modell 'bert-base-german-cased'), pandas, numpy, matplotlib

Sie können diese Module leicht über pip installieren. Nutzen Sie dazu folgenden Befehl im Terminal/CommandLine:
```
    python3 -m pip install ...
```

Hinweis: ```-m``` steht dafür, dass Python ein Modul ansteuert (in diesem Fall pip). Geben Sie für ```...``` den jeweiligen Modul-Namen ein.


# 4) Zugriff auf den Datensatz:

Den Datensatz können Sie als csv-Datei unter folgendem Link herunterladen: https://boxup.uni-potsdam.de/index.php/s/2B4ItGqwFexvjvq (password: omt). Beachten Sie, dass dieser 
Datensatz unter einer CC BY-NC Lizenz steht (siehe: https://competitions.codalab.org/competitions/20139#learn_the_details-terms_and_conditions).

Sie können den Datensatz in Python mit dem Modul pandas einlesen. Folgende Funktion kann dazu genutzt werden:
```
    pandas.read_csv('Name-of-dataset')
```

# 5) Testen Sie ihre Installation:

Zuletzt haben wir ein Testskript (Testskript.py) erstellt. Öffnen Sie dieses in Spyder und führen Sie es aus. Wenn Sie keine Fehlermeldungen bekommen, dann ist ihr System startbereit für den 
Workshop. Alternativ können Sie das Skript über das Terminal/CommandLine ausführen:

```
    python3 Testskript.py
```

Hinweis: Um das Skript über diesen Befehl ausführen zu können, müssen Sie entsprechend mit dem Terminal/CommandLine im Verzeichnis des Skriptes sein. Sie können das Verzeichnis mit dem Befehl
```cd``` wechseln.

Wir freuen uns auf Sie!