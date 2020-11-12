# 1) Installation von Python

Im Workshop arbeiten wir mit der freien Software Python (Version 3.6 oder höher). Je nach Betriebssystem erfolgt die Installation anders. Wichtig für die Installation ist, dass Sie dies mit Admin-Rechten
durchführen. Eine Installation ohne Admin-Recht ist zwar unter bestimmten Umständen möglich, aber unserer Erfahrung nach treten dabei häufig Komplikationen auf, die nicht einfach behoben werden 
können. 

Ziel der Installationsanleitung ist es, dass Sie am Ende ein Testskript für Python in einer Entwicklungsumgebung ausführen können. Darin sind alle erforderlichen Pakete angegeben, sodass Sie testen 
können, inwieweit Ihr Rechner bereit für den Workshop ist. Allgemein ist die Installation von Python nicht trivial. Sollten Sie Fragen an einer Stelle haben, melden Sie sich gerne für macOS-User bei 
buschhue@uni-potsdam.de und für Windows-User bei peter.wulff@uni-potsdam.de.

Hinweis: Zur Installation wird das Terminal (macOS, Linux) oder die CommandLine (Windows) verwendet. Zum Ausführen des Terminals unter macOS geben Sie in der Suchmaschine Spotlight ''Terminal'' ein', bei Windows geben Sie in der Suche ''cmd'' ein.

Für die Installation von Python verweisen wir auf folgende Website: https://docs.python-guide.org/#. Dort finden Sie für die gängigen Betriebssysteme (Linux, macOS, Windows) eine Installationsanleitung. Den Punkt "Pipenv & Virtual Environments" aus der Anleitung brauchen Sie für den Workshop nicht umzusetzen.

# 2) Installation von pip (Abkürzung "pip installs packages")

Zur Installation von zusätzlichen Modulen in Python wird standardmäßig pip (Abkürzung "pip installs packages") verwendet. Eigentlich sollte dies bereits installiert sein. Sie werden bemerken, falls dies nicht der Fall sein sollte, wenn die Installation von Spyder (s.u.) via (`python3 -m pip install spyder`) nicht funktioniert.

Sollte es noch nicht installiert sein, führen Sie die installation wie folgt durch: Um pip zu installieren, laden Sie bitte folgendes Python-Skript: [get-pip.py](https://bootstrap.pypa.io/get-pip.py) herunter. Alternativ können Sie curl im Terminal verwenden:

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


# 3) Installation der Entwicklungsumgebung *Spyder*

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


# 4) Installation notwendiger Python-Module 

Um Auswerteverfahren umzusetzen und möglichst gut mit Python arbeiten zu können, verwenden wir frei verfügbare Module (in etwa Pakete in R) sowie die Entwicklungsumgebung Spyder. Zunächst ist es dazu 
erforderlich ein Modul- oder Paketmanager zu haben. Wir verwenden hierfür pip ("Pip installs Packages").

Folgende Module sollten Sie vorab installieren: scikitlearn, umap, hdbscan, sentence-transformers (mit dem Modell 'bert-base-german-cased'), pandas, numpy, matplotlib

Sie können diese Module leicht über pip installieren. Nutzen Sie dazu folgenden Befehl im Terminal/CommandLine:
```
    python3 -m pip install pandas numpy matplotlib seaborn scikit-learn umap hdbscan sentence-transformers
```

Hinweis: ```-m``` steht dafür, dass Python ein Modul ansteuert (in diesem Fall pip).

**Falls die Installation (wahrscheinlich aufgrund von sentence-transformers) fehlschlägt, liegt dies nach unserer Erfahrung an der Python-Version. Um eine andere Python-Version zu installieren, können Sie wie folgt vorgehen (bitte installieren Sie in dem Fall Python 8.2):**

## 4.1 Installieren einer anderen Python-Version (8.2): Windows


## 4.2 Installieren einer anderen Python-Version (8.2): MacOs
Leider kann homebrew nicht Python in einer beliebigen Version installieren. Mithilfe folgender Anleitung können Sie aber eine andere Python-Version zusätzlich installieren. Installieren Sie die dabei bitte Python 8.2. Führen Sie dabei alle Schritte 1-7 der folgenden Anleitung durch:

https://www.chrisjmendez.com/2017/08/03/installing-multiple-versions-of-python-on-your-mac-using-homebrew/

Führen Sie dann im Anschluss noch einmal den folgenden Code im Terminal aus:

```
    python3 -m pip install pandas numpy matplotlib seaborn scikit-learn umap hdbscan sentence-transformers
```

## 4.3 Installieren einer anderen Python-Version (8.2): Linux


# 5) Zugriff auf den Datensatz

Den Datensatz können Sie als csv-Datei unter folgendem Link herunterladen: https://boxup.uni-potsdam.de/index.php/s/2B4ItGqwFexvjvq (password: omt). Beachten Sie, dass dieser 
Datensatz unter einer CC BY-NC Lizenz steht (siehe: https://competitions.codalab.org/competitions/20139#learn_the_details-terms_and_conditions).

Sie können den Datensatz in Python mit dem Modul pandas einlesen. Folgende Funktion kann dazu genutzt werden:
```
    pandas.read_csv('Name-of-dataset')
```



# 6) Testen Sie Ihre Installation

Zuletzt haben wir ein Testskript (Testskript.py) erstellt. 

https://github.com/dbuschhue/intro_nlp_workshop/blob/main/tutorial_installationsanleitung/02_testskript.py

Öffnen Sie dieses in Spyder und führen Sie es aus. Wenn Sie keine Fehlermeldungen bekommen, dann ist Ihr System startbereit für den  Workshop. Alternativ können Sie das Skript über das Terminal/CommandLine ausführen:

```
    python3 02_testskript.py
```

Hinweis: Um das Skript über diesen Befehl ausführen zu können, müssen Sie entsprechend mit dem Terminal/CommandLine im Verzeichnis des Skriptes sein. Sie können das Verzeichnis mit dem Befehl
```cd``` wechseln.

Jetzt können Sie unser Tutorial ausprobieren:

* https://github.com/dbuschhue/intro_nlp_workshop/blob/main/tutorial_installationsanleitung/03c_tutorial.pdf (Leseversion)
* https://github.com/dbuschhue/intro_nlp_workshop/blob/main/tutorial_installationsanleitung/03b_tutorial_python.py (Ausführbar in Spyder)

Wir freuen uns auf Sie!
