# Python-Kurvendiskussion-Projekt
In diesem Projekt führen wir eine komplette Kurvendiskussion durch. Vorgabe: Objektorientierte Programmierung


Als Eingabe dienen folgende Funktionen:

  -> lineare Funktionen
  -> quadratische Funktion
  


-> Die Eingabe wird durch Input-Validation geprüft und in eine der vorgegebenen Funktions-Kategorien eingeordnet
--> Die Berechnung der Ergebnisse erfolgt in der jeweiligen Klasse
  
  -> Bestandteile der Ergebnisse:
     
      > Ableitungen (Möglichkeit der Anzeige aller, die zur Berechnung verwendet werden)
      > Nullpunkte mit der X-Achse (Anzahl; Koordinaten)
      > Symmetrie vorhanden? 
          - X-Achse
          - Y-Achse
      > Extremstellen  
          - Hochpunkte (Anzahl; ggfs. Koordinaten)
          - Tiefpunkte (Anzahl; ggfs. Koordinaten)
          - Wendepunkte (Anzahl; ggfs. Koordinaten)
      > Krümmungs-Verhalten
      > Monotonie-Verhalten
      > Grenzverhalten (limes) (gegen +/- unendlich)
      
    --> Die Ausgabe erfolgt in einer geordneten übersichtlichen Tabelle

Projekt-Teilnehmer: Stefan Mack, Oliver Polak, Rami Karkaba und David Klumpp


    Optimierung kurz vor der Abgabe-----------------------
    -> Dopplungen abschaffen und zusammenfassen
    -> pylint Pyhton-Code Analyzer
    —> black (code formator)
    —> pytest (code tester)
    —> isort (Sortiert alle Python Module korrekt)


    classes:
      -InputFunction
      -LinearFunction
      -QuadraticFunction
      -CurveDiscussionOutput

    files:
      -main.py
      -input_function.py
      -linear_function.py
      -quadratic_function.py
      -curve_discussion_output.py
      
     test_files:
       -test_lin_func.py
       -test_quad_func.py

Programmablauf:
  main -> input_function -> linear_function | quadratic_function -> curve_discussion_output
