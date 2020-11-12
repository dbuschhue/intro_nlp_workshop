# 1) Installation von Python

Im Workshop arbeiten wir mit der freien Software Python (Version 3.8). Je nach Betriebssystem erfolgt die Installation anders. Wichtig für die Installation ist, dass Sie dies mit Admin-Rechten durchführen. Eine Installation ohne Admin-Rechte ist zwar unter bestimmten Umständen möglich, aber unserer Erfahrung nach treten dabei häufig Komplikationen auf, die nicht einfach behoben werden 
können. 

Ziel der Installationsanleitung ist es, dass Sie am Ende ein Testskript für Python in einer Entwicklungsumgebung (Spyder) ausführen können. Darin sind alle erforderlichen Pakete angegeben, sodass Sie testen können, inwieweit Ihr Rechner bereit für den Workshop ist. Sollten Sie die Installation nicht fertigstellen können, können Sie trotzdem am Workshop teilnehmen.

Allgemein ist die Installation von Python nicht trivial. Sollten Sie Fragen an einer Stelle haben, melden Sie sich gerne für macOS-User bei 
buschhue@uni-potsdam.de und für Windows-User bei peter.wulff@uni-potsdam.de.

Hinweis: Zur Installation wird das Terminal (macOS, Linux) oder die CommandLine (Windows) verwendet. Zum Ausführen des Terminals unter macOS geben Sie in der Suchmaschine Spotlight ''Terminal'' ein', bei Windows geben Sie in der Suche ''cmd'' ein.

Für die Installation von Python verweisen wir auf folgende Website: https://docs.python-guide.org/#. Dort finden Sie Anleitungen für die gängigen Betriebssysteme (Linux, macOS, Windows). Bevor Sie damit beginnen, lesen Sie sich bitte die folgenden Punkte für Ihr Betriebssystem durch: Es gibt nämlich einen Versionskonflikt mit der aktuellsten Python-Version und einem der Module, das wir aktuell verwenden. Im Workshop wollen wir Python 3.8.2 verwenden (Version 3.8.5 sollte auch funktionieren).

# Für Windows
Folgen Sie den Schritten auf https://docs.python-guide.org/starting/install3/win/ aber führen Sie anstatt des ersten Befehls `choco install python` den Befehl `choco install python3 --version=3.8.2` aus. So installieren Sie Python in der Version 3.8.2. Den Punkt "Pipenv & Virtual Environments" aus der Anleitung brauchen Sie für den Workshop nicht umzusetzen.

# Für Linux:
Sie können einfach die Anleitung nach https://docs.python-guide.org/starting/install3/linux/ ausführen. Hier wird die Version 3.8.5 installiert. Das sollte auch funktionieren. Den Punkt "Pipenv & Virtual Environments" aus der Anleitung brauchen Sie für den Workshop nicht umzusetzen.

# Für Mac:
Installieren Sie zunächst Version 3.9 entsprechend dem Link https://docs.python-guide.org/starting/install3/osx/. Den Punkt "Pipenv & Virtual Environments" aus der Anleitung brauchen Sie für den Workshop nicht umzusetzen. Dann installieren Sie im Nachhinein die Version Python 3.8.2 entsprechend https://www.chrisjmendez.com/2017/08/03/installing-multiple-versions-of-python-on-your-mac-using-homebrew/. Führen Sie dabei alle Schritte 1-7 der Anleitung aus.

# 2) Installation von pip (Abkürzung "pip installs packages")

Zur Installation von zusätzlichen Modulen in Python wird standardmäßig pip (Abkürzung "pip installs packages") verwendet. Eigentlich sollte dies bereits installiert sein. Sie werden bemerken, falls dies nicht der Fall sein sollte, wenn die Installation von Spyder (s.u.) (via `python3 -m pip install spyder`) nicht funktioniert.

Sollte es noch nicht installiert sein, führen Sie die installation wie folgt durch: Um pip zu installieren, laden Sie bitte folgendes Python-Skript: [get-pip.py](https://bootstrap.pypa.io/get-pip.py) herunter. Alternativ können Sie den Befehl `curl` im Terminal wie folgt verwenden:

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

Um komfortabel Python-Skripte testen und ausführen zu können, empfehlen wir insbesondere für Anfängerinnen und Anfänger die Nutzung einer interaktiven Entwicklungsumgebung (IDE). Als Entwicklungsumgebung empfehlen wir Spyder, da Spyder kostenfrei ist und nützliche Funktionalitäten (u.a., interaktive Konsole) bietet. Außerdem sieht es fast so aus wie RStudio, was vielen von Ihnen bekannt sein könnte. Es können alternativ auch IDLE (die Standard-Entwicklungsumgebung) sowie PyCharm (teilweise kostenpflichtig) verwendet werden.

Die Installation von Spyder erfolgt über pip und den Befehl: 
```
    python3 -m pip install spyder
```

Auch hier sollten Sie sich vergewissern, dass Sie Spyder über Terminal/CommandLine starten können. Geben Sie dazu folgenden Befehl ein:
```
    spyder
```
**Sie können Spyder nun einfach immer auf diese Weise aus dem Terminal/der Commandline starten (wundern Sie sich also nicht, wenn Sie keine Porgramm dazu unter Programme ö.Ä. finden).**

# 4) Installation notwendiger Python-Module 

Um Auswerteverfahren umzusetzen und möglichst gut mit Python arbeiten zu können, verwenden wir frei verfügbare Module (in etwa Pakete in R). Wir verwenden hierfür zur Installation pip.

Folgende Module sollten Sie vorab installieren: pandas, numpy, matplotlib, seaborn, scikit-learn, umap, hdbscan, sentence-transformers (mit dem Modell 'bert-base-german-cased') pyLDAvis, scipy
 
Sie können diese Module leicht über pip installieren. Nutzen Sie dazu folgenden Befehl im Terminal/CommandLine:
```
    python3 -m pip install pandas numpy matplotlib seaborn scikit-learn umap hdbscan sentence-transformers pyLDAvis scipy
```

Hinweis: ```-m``` steht dafür, dass Python ein Modul ansteuert (in diesem Fall pip).



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
